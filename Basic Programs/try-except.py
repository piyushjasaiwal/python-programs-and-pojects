print("Welcome to the try except block in ")
print("enter the two numbers")
a = int(input())
b = int(input())
try:
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print("still in the try block no error")
except Exception as e:
    print(e)
    print("the following error is not allowing the program to function smoothly and the follwing error is raised",e)
finally:
    print("the finally block hs been reached and we are in the endgame nbow!!!!!!!!!")
