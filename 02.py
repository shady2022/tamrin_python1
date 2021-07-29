import math 

weight = int(input("please enter your weight in kg:"))
height = int(input("please enter your height in m:"))

BMI = (weight/height*2)

if BMI == "25.29,9":
    print("YOU ARE OVERWEIGHT")

if BMI == "30.34,9":
    print("YOU ARE OBESE") 

else: 
    if BMI < 35:
        print("extra obese")