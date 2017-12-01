#include <stdio.h>

#include "../util.h"

void part1() {
	FILE *f = fopen("input.txt", "r");
	char *line;
	int a, b, c, r, valid = 0;
	
	while ((line = readline(f)) != NULL) {
		r = sscanf(line, "%i %i %i", &a, &b, &c);
		free(line);
		
		if (r != 3)
			break;
		
		if (a + b > c && a + c > b && b + c > a) {
			valid++;
		}
	}
	
	printf("%i\n", valid);
	fclose(f);
}

void part2() {
	FILE *f = fopen("input.txt", "r");
	char *group[3];
	int i, r, valid = 0;
	int n[3][3];
	
	while ((group[0] = readline(f)) != NULL) {
		// Hope there are the right number of lines
		group[1] = readline(f);
		group[2] = readline(f);

		r = sscanf(group[0], "%i %i %i", n[0], n[1], n[2]);
		r += sscanf(group[1], "%i %i %i", n[0] + 1, n[1] + 1, n[2] + 1);
		r += sscanf(group[2], "%i %i %i", n[0] + 2, n[1] + 2, n[2] + 2);
		
		free(group[0]);
		free(group[1]);
		free(group[2]);
		
		if (r != 9)
			break;
		
		for (i = 0; i < 3; i++) {
			if (n[i][0] + n[i][1] > n[i][2] && n[i][0] + n[i][2] > n[i][1] && n[i][1] + n[i][2] > n[i][0]) {
				valid++;
			}
		}
	}
	
	printf("%i\n", valid);
	fclose(f);
}