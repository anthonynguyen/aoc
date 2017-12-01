#!/usr/bin/env python3

import hashlib

inp = "ojvtpuvg"

outp = ""

i = 0

while len(outp) < 8:
	d = hashlib.md5((inp + str(i)).encode("utf-8")).hexdigest()
	if d[:5] == "00000":
		outp += d[5]
	i += 1

print(outp)


# -----------------------------

outp = ["*", "*", "*", "*", "*", "*", "*", "*"]

i = 0

while outp.count(0) > 0:
	i += 1
	d = hashlib.md5((inp + str(i)).encode("utf-8")).hexdigest()
	if d[:5] == "00000":
		if d[5] not in "01234567" or outp[int(d[5])] != "*":
			continue
		outp[int(d[5])] = d[6]

print("".join(outp))
