import math
import cmath 

a = float(input())
b = float(input())
degrees = float(input())
z = complex (a,b);

radians = degrees/360.0*2*math.pi


op = input()

if op== "cos":
    print(cmath.cos(z))
    print(math.cos(radians))

if op== "sin":
    print(cmath.sin(z))
    print(math.sin(radians))

if op== "cot":
    print(cmath.cot(z))
    print(math.cot(radians))

if op == "tan":
    print(cmath.tan(z))
    print(math.tan(radians))


if op == "+":
    print(a+b)

if op == "-": 
    print(a-b)    

if op == "/":
    if b == 0:
        print("khata!!")
else:
    print(a/b)

if op== "*":
    print(a*b)

print()

def factorial(n): 

    if n == 0:
      return 1
    else:
      return n * factorial(n-1)
number = int(input("please Enter integer number: "))
result = factorial(number)
print("The factorial is: {}".format(number, result))

x=math.sqrt()
print(x)
i = input()












print()       
