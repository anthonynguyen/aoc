#include <stdio.h>
#include <stdlib.h>

void part1() {
	FILE *f = fopen("input.txt", "r");
	char c;
	char pad[3][4] = {"123", "456", "789"};
	char code[6] = {0};
	int l = 0;
	int x = 1, y = 1;
	
	while ((c = fgetc(f)) && l < 5) {
		if (c == '\n' || c == EOF) {
			code[l++] = pad[y][x];
		} else if (c == 'U' && y > 0) {
			y--;
		} else if (c == 'R' && x < 2) {
			x++;
		} else if (c == 'D' && y < 2) {
			y++;
		} else if (c == 'L' && x > 0) {
			x--;
		}
	}
	
	printf("%s\n", code);
	fclose(f);
}

void part2() {
	FILE *f = fopen("input.txt", "r");
	char c;
	char pad[5][6] = {
		"--1--",
		"-234-",
		"56789",
		"-ABC-",
		"--D--"
	};
	char code[6] = {0};
	int l = 0;
	int x = 1, y = 1;
	
	while ((c = fgetc(f)) && l < 5) {
		if (c == '\n' || c == EOF) {
			code[l++] = pad[y][x];
		} else if (c == 'U' && y > 0 && pad[y - 1][x] != '-') {
			y--;
		} else if (c == 'R' && x < 4 && pad[y][x + 1] != '-') {
			x++;
		} else if (c == 'D' && y < 4 && pad[y + 1][x] != '-') {
			y++;
		} else if (c == 'L' && x > 0 && pad[y][x - 1] != '-') {
			x--;
		}
	}
	
	printf("%s\n", code);
	fclose(f);
}