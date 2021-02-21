num1 = int(input("Enter the 1st Number --> "))
num2 = int(input("Enter the 2nd Number --> "))
num3 = int(input("Enter the 3rd Number --> "))
num4 = int(input("Enter the 4th Number --> "))


if (num1>num2):
    f1 = num1
else:
    f1 = num2

if (num2>num3):
    f2 = num2
else:
    f2 = num3



if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")