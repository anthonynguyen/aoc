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

	char password[9];
	int passlen = 0;

	char md5sum[24];
	char *h;

	while (passlen < 8) {
		sprintf(buffer, "%s%i", in, index++);
		MD5(buffer, strlen(buffer), md5sum);
		h = hexdigest(md5sum);

		if (strncmp(h, "00000", 5) == 0) {
			password[passlen] = h[5];
			passlen++;
		}
	}
	password[passlen] = 0;

	printf("%s\n", password);
	return 0;
}