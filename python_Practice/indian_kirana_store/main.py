print("Insert all the numbers and put q at the last")
list_items = []
while(True):
    num = input()
    if(num == 'q'):
        break
    list_items.append(int(num))
print('Total item purchased are')
print(list_items)
print("the total bill is :",sum(list_items))