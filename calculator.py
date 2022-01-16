# calculator using python

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
print("If choosen subtract the second number is subtracted from the first "
      "if divide first number is divided by second ")
operator = input("operation ," "+" + " -"+ " *" + " / : ")
if operator == '+':
    num3 = num2+num1
elif operator == "-":
    num3 = num1-num2
elif operator == "*":
    num3 = num1*num2
else:
    num3 = num1/num2
print(num3)


