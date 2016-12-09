#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void move(int d, int n, int *x, int *y) {
	if (d == 0) {
		*y += n;
	} else if (d == 1) {
		*x += n;
	} else if (d == 2) {
		*y -= n;
	} else {
		*x -= n;
	}
}


void part1() {
	int d = 0; // 0 - North, 1 - East, 2 - South, 3 - West
	int x = 0, y = 0;
	
	int n;
	
	int state = 0; // 0 - between instructions, 1 - reading turn/number
	
	FILE *input = fopen("input.txt", "r");
	char c;
	
	while ((c = fgetc(input)) != EOF) {
		if (state == 0) {
			if (c == 'L') {
				d = (d - 1 + 4) % 4;
				state = 1;
				n = 0;
			} else if (c == 'R') {
				d = (d + 1) % 4;
				state = 1;
				n = 0;
			}
		} else {
			if (c >= '0' && c <= '9') {
				n = n * 10 + (c - '0');
			} else {
				// transition from state 1 to 0
				move(d, n, &x, &y);
				
				n = 0;
				state = 0;
			}
		}
	}
	move(d, n, &x, &y);
	printf("%i, %i -> %i\n", x, y, abs(x) + abs(y));
	
	fclose(input);
}

typedef struct node {
	int x, y;
	struct node *next;
} node;

int find(node *head, int x, int y) {
	node *cur = head;
	while (cur) {
		if (cur->x == x && cur->y == y) {
			return 1;
		}
		
		cur = cur->next;
	}
	return 0;
}

int move2(node *head, int d, int n, int *x, int *y) {
	int i = 0;
	int dx = 0, dy = 0;
	node *tail = head;
	
	if (d == 0) {
		dy = 1;
	} else if (d == 1) {
		dx = 1;
	} else if (d == 2) {
		dy = -1;
	} else {
		dx = -1;
	}
	
	while (tail->next) {
		tail = tail->next;
	}
	
	for (i = 0; i < n; i++) {
		*x += dx;
		*y += dy;
		
		if (find(head, *x, *y)) {
			return 1;
		} else {
			tail->next = malloc(sizeof(node));
			tail = tail->next;
			tail->x = *x;
			tail->y = *y;
		}
	}
	
	return 0;
}

void part2() {
	node *head = malloc(sizeof(node));
	
	head->x = 0;
	head->y = 0;
	
	int d = 0; // 0 - North, 1 - East, 2 - South, 3 - West
	int x = 0, y = 0;
	
	int n, r;
	
	int state = 0; // 0 - between instructions, 1 - reading turn/number
	
	FILE *input = fopen("input.txt", "r");
	char c;
	
	while ((c = fgetc(input)) != EOF) {
		if (state == 0) {
			if (c == 'L') {
				d = (d - 1 + 4) % 4;
				state = 1;
				n = 0;
			} else if (c == 'R') {
				d = (d + 1) % 4;
				state = 1;
				n = 0;
			}
		} else {
			if (c >= '0' && c <= '9') {
				n = n * 10 + (c - '0');
			} else {
				// transition from state 1 to 0
				r = move2(head, d, n, &x, &y);
				if (r) {
					break;
				}
				
				n = 0;
				state = 0;
			}
		}
	}
	if (!r) {
		move2(head, d, n, &x, &y);
	}
	printf("%i, %i -> %i\n", x, y, abs(x) + abs(y));
	
	fclose(input);
}