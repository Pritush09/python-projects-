
#seeing wether the number is an armstrong number
# 3899 = 3**4 + 8**4 +9**4 + 9**4 if equal then is an armstrong number





s = int(input("Enter the number: "))
b = len(str(s))
sum = 0
c = s
while (s > 0):
    digit = s % 10
    s = s // 10
    sum += digit ** b

if sum == c:
    print("it is a armstrong number ")
else:
    print("not an armstrong number")
