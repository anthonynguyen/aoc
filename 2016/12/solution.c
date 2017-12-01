#include <stdio.h>
#include <string.h>

#include "../util.h"

int solve(int a, int b, int c, int d) {
	FILE *f = fopen("input.txt", "r");
	int numInstructions = 0;
	char **instructions = malloc(sizeof(char *));
	char *ins;
	int pc = 0;

	int n, m;
	char p, q;

	int registers[4];
	registers[0] = a;
	registers[1] = b;
	registers[2] = c;
	registers[3] = d;

	// read all lines into instructions array
	while ((ins = readline(f)) != NULL) {
		instructions[numInstructions++] = ins;
		instructions = realloc(instructions, (numInstructions + 1) * sizeof(char *));
	}
	fclose(f);

	while (pc < numInstructions) {
		ins = instructions[pc];

		if (!strncmp(ins, "cpy", 3)) {
			if (ins[4] < 'a') { // is a number
				sscanf(ins, "%*s %i %c", &n, &p);
				registers[p - 'a'] = n;
			} else {
				sscanf(ins, "%*s %c %c", &p, &q);
				registers[q - 'a'] = registers[p - 'a'];
			}
		} else if (!strncmp(ins, "inc", 3)) {
			registers[ins[4] - 'a']++;
		} else if (!strncmp(ins, "dec", 3)) {
			registers[ins[4] - 'a']--;
		} else if (!strncmp(ins, "jnz", 3)) {
			if (ins[4] < 'a') { // is a number
				sscanf(ins, "%*s %i %i", &n, &m);
			} else {
				sscanf(ins, "%*s %c %i", &p, &m);
				n = registers[p - 'a'];
			}

			if (n != 0) {
				pc += m;
				continue;
			}
		}

		pc++;
	}

	for (n = 0; n < numInstructions; n++) {
		free(instructions[n]);
	}
	free(instructions);

	return registers[0];
}

void part1() {
	printf("%i\n", solve(0, 0, 0, 0));
}

void part2() {
	printf("%i\n", solve(0, 0, 1, 0));	
}
