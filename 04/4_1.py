#!/usr/bin/env python3
import hashlib

inpt = "bgvyzdsv"
i = 0

while (i < 100000000):
	s = inpt + str(i)
	if hashlib.md5(s).hexdigest()[:5] == "00000":
		print(i)
		break

	i += 1