#!/usr/bin/env python3

import hashlib

inp = "ojvtpuvg"

outp = ""

i = 0

while len(outp) < 8:
	d = hashlib.md5((inp + str(i)).encode("utf-8")).hexdigest()
	if d[:5] == "00000":
		outp += d[5]
		print(d[5])
		
	i += 1

print(outp)