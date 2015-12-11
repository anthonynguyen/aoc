#!/usr/bin/env python3

f = open("input1.txt")
c = f.read()
f.close()
print(c.count("(") - c.count(")"))