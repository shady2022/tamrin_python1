import math

a = int(input("andaze zelee a ra vared konid:"))
b = int(input("andaze zelee b ra vared konid:"))
c = int(input("andaze zelee c ra vared konid:"))

if a < (b+c):
    print("momken ast")
else:
    print("na momken ast")

if b < (a+c):
    print("momken ast")
else:
    print("na momken ast")

if c < (a+b):
    print("momken ast")
else:
    print("na momken ast")

