#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>

char *in = "ngcjuoqr";

static char *hexdigest(unsigned char *in) {
	static char hex[] = "0123456789abcdef";
	static int i, pos = 0;

	char *out = malloc(sizeof(char) * 33);

	pos = 0;
	for (i = 0; i < 16; i++) {
		out[pos++] = hex[in[i] >> 4];
		out[pos++] = hex[in[i] & 0xF];
	}
	out[pos] = 0;

	return out;
}

static char *hash(const char *s) {
	static unsigned char md5bytes[24];
	MD5((unsigned char*)s, strlen(s), md5bytes);
	return hexdigest(md5bytes);
}

static char *getHash1(int n) {
	static char **calculated = NULL;
	static int len = 0;
	static char buffer[32];
	static int i, s;

	if (calculated == NULL) {
		calculated = malloc(sizeof(char *));
	}

	s = n - len + 1;

	if (n >= len) {
		for (i = 0; i < s; i++) {
			sprintf(buffer, "%s%i", in, len);
			calculated[len++] = hash(buffer);
			calculated = realloc(calculated, sizeof(char *) * (len + 1));
		}
	}

	return calculated[n];
}

static char *getHash2(int n) {
	static char **calculated = NULL;
	static int len = 0;
	static char buffer[32];
	static int i, j, s;
	static char *h;

	if (calculated == NULL) {
		calculated = malloc(sizeof(char *));
	}

	s = n - len + 1;

	if (n >= len) {
		for (i = 0; i < s; i++) {
			sprintf(buffer, "%s%i", in, len);
			h = hash(buffer);

			for (j = 0; j < 2016; j++) {
				h = hash(h);
			}
			calculated[len++] = h;
			calculated = realloc(calculated, sizeof(char *) * (len + 1));
		}
	}

	return calculated[n];
}

int compare (const void *a, const void *b) {
  return (*(int *)a - *(int *)b);
}

void solve(int p) {
	int index = 0;

	int keys[64];
	int numk = 0;

	int f, i, j, k;

	char *h, *hh;
	char c;

	while (numk < 64) {
		if (p == 2) {
			h = getHash2(index);
		} else {
			h = getHash1(index);
		}
		
		for (i = 0; i < strlen(h) - 2; i++) {
			if (h[i] == h[i+1] && h[i+1] == h[i+2]) {
				c = h[i];

				f = 0;
				for (j = 1; j <= 1000; j++) {
					if (p == 2) {
						hh = getHash2(index + j);
					} else {
						hh = getHash1(index + j);
					}
					for (k = 0; k < strlen(hh) - 4; k++) {
						if (c == hh[k] &&\
								hh[k] == hh[k+1] && hh[k+1] == hh[k+2] &&\
								hh[k+2] == hh[k+3] && hh[k+3] == hh[k+4]) {
							f = 1;
							keys[numk++] = index;
							break;
						}
					}

					if (f) {
						break;
					}
				}

				break;
			}
		}

		index++;
	}

	// for (i = 0; i < numk; i++) {
	// 	if (i == numk - 1) {
	// 		printf("[%i] %i\n", i, keys[i]);
	// 	} else {
	// 		printf("[%i] %i, ", i, keys[i]);
	// 	}
	// }

	printf("%i\n", keys[63]);
}

void part1() {
	solve(1);
}

void part2() {
	solve(2);
}
