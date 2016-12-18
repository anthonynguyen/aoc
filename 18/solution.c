#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define INPUT_LENGTH 100

static uint8_t buffer[INPUT_LENGTH];

void read() {
	static uint8_t initialized = 0;

	if (!initialized) {
		uint8_t i;
		FILE *f = fopen("input.txt", "r");
		for (i = 0; i < INPUT_LENGTH; i++) {
			buffer[i] = (fgetc(f) == '.');
		}
		fclose(f);
		initialized = 1;
	}
}

void solve(int rows) {
	int i, safe = 0;
	uint8_t a, c, j;
	uint8_t rrow[INPUT_LENGTH], nnext[INPUT_LENGTH];
	uint8_t *row = rrow, *next = nnext, *swap;

	read();

	for (i = 0; i < INPUT_LENGTH; i++) {
		row[i] = next[i] = buffer[i];
		safe += row[i];
	}

	for (i = 0; i < rows - 1; i++) {
		for (j = 0; j < INPUT_LENGTH; j++) {
			a = ((!j) | row[j-1]);
			c = ((j == (INPUT_LENGTH - 1)) | row[j+1]);

			next[j] = (a == c);
			safe += next[j];
		}

		swap = row;
		row = next;
		next = swap;
	}

	printf("%i\n", safe);
}

void part1() {
	solve(40);
}

void part2() {
	solve(400000);
}
