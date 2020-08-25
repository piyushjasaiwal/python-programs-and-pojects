print("Enter the two numbers you with a space in between")
a,b = map(int,input().split(" "))

print("Enter the Operator")
op = input()

if(((a == 45  and b == 3) or (a == 3  and b == 45)) and op == '*'):
    print(555)
elif(((a == 56  and b == 9) or (a == 9  and b == 56)) and op == '+'):
    print(77)
elif((a == 56  and b == 6) and op == '/'):
    print(4)

else:
    try:
        if op == '+':
            print(a+b)
        elif op == '*':
            print(a*b)
        elif op == '-':
            print(a-b)
        elif op == '/':
            print(a/b)
        else:print("Wrong Choice")

    except Exception as e:
        print(e)