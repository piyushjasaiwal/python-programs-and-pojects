with open('converter_file.txt') as f:
    a = f.readlines()
    
country_from = input("Enter the counntry of which the currency you have : ")
country_to = input("Enter the country of which currency you want to convert to : ")
money = int(input("Enter the amount of money you want to"))
fro = 0
to = 0
flag = False
for i in range(0,len(a)):
    list = a[i].split("\t")
    if list[0] == country_from:
        flag = True
        fro = float(list[1])
    if list[0] == country_to:
        to = float(list[1])


if(not flag):
    print("Country Not Found")
else:
    money_convert = (to/fro)*money
    print(money_convert)