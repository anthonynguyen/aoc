#include <stdio.h>
#include <stdlib.h>

#define CHUNK_SIZE 4

char *readline(FILE *f) {
	int size = CHUNK_SIZE, len = 0;
	char *buffer = malloc(size * sizeof(char));
	char c;
	
	while ((c = fgetc(f))) {
		if (c == '\n' || c == EOF) {
			if (!len && c == EOF) {
				return NULL;
			}
			
			buffer[len] = 0;
			return buffer;
		} else {
			buffer[len++] = c;
			if (len + 1 == size) {
				size += CHUNK_SIZE;
				buffer = realloc(buffer, size * sizeof(char));
			}
		}
	}
	
	// Uh, we should never reach this
	buffer[len] = 0;
	return buffer;
}