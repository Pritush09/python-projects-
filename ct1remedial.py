in1 = int(input())
in2 = int(input())
in3 = int(input())
list_for_the_inputs = [in2,in1,in3]
if list_for_the_inputs[0]>list_for_the_inputs[1] and list_for_the_inputs[0]<list_for_the_inputs[2]:
    print(list_for_the_inputs[0])
elif list_for_the_inputs[0]>list_for_the_inputs[2] and list_for_the_inputs[0]<list_for_the_inputs[1]:
    print(list_for_the_inputs[0])

elif list_for_the_inputs[1]>list_for_the_inputs[0] and list_for_the_inputs[1]<list_for_the_inputs[2]:
    print(list_for_the_inputs[1])
elif list_for_the_inputs[1]>list_for_the_inputs[2] and list_for_the_inputs[1]<list_for_the_inputs[0]:
    print(list_for_the_inputs[1])
else:
    print(list_for_the_inputs[2])


print("\n")






import math
def checkprime(n):
    if n==1:
        return False
    elif n==2:
        return  True
    elif n>2 and n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True
intr = int(input())
for m in range(intr,0,-1):
    if checkprime(m)==True:
        print(m)
        break








