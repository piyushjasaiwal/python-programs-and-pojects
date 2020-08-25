def fact(num):
    if num == 1 or num == 0:
        return 1
    return num*fact(num-1)

def trailing_zero(num):
    temp = num
    num_5 = 0
    num_2 = 0
    while temp%2 == 0:
        num_2+=1
        temp/=2

    while temp%5 == 0:
        num_5+=1
        temp/=5
        
    return(min(num_2,num_5))

def count_5(number):
    num_5 = 0
    while number%5 == 0:
        num_5+=1
        number/=5
    return num_5


def count_2(number):
    num_2 = 0
    while number%2 == 0:
        num_2+=1
        number/=2
    return num_2



def trailing_zero_factorial(number):
    num_5 = 0
    num_2 = 0
    for x in range(number,0,-1):
        num_5+=count_5(x)
        num_2+=count_2(x)
    return(min(num_2,num_5))


print("Enter a number")
# number = int(input())
# print(fact(number))    

print(trailing_zero_factorial(10))