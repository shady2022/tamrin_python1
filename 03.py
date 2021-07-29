import math

name = input()
family = input()

a = float(input("please enter the number of first exam:"))
b = float(input("please enter the number of second exam:"))
c = float(input("please enter the number of third exam:"))

avarage = (a+b+c)/3

if avarage >= 17:
    print("GREAT!!!")

if avarage >= 12 and avarage <17:
    print("NORMAL")

if avarage < 12:
    print("FAIL")    