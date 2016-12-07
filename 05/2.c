#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>

char *hexdigest(unsigned char *in) {
	static char hex[] = "0123456789abcdef";
	static char out[9];
	static int i, pos = 0;

	pos = 0;
	for (i = 0; i < 4; i++) {
		out[pos++] = hex[in[i] >> 4];
		out[pos++] = hex[in[i] & 0xF];
	}

	out[pos] = 0;

	return out;
}

int main() {
	char *in = "ojvtpuvg";
	char buffer[24];
	int index = 0;

	char password[9] = "********";
	int found = 0;

	char md5sum[24];
	char *h;

	int i = 0;

	while (found < 8) {
		sprintf(buffer, "%s%i", in, index++);
		MD5(buffer, strlen(buffer), md5sum);
		h = hexdigest(md5sum);

		if (strncmp(h, "00000", 5) == 0) {
			i = h[5] - '0';
			if (i >= 0 && i < 8 && password[i] == '*') {
				password[i] = h[6];
				found++;
			}
		}
	}

	printf("%s\n", password);
	return 0;
}