my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
l= []
for item in my_list:
    if item%2 ==0:
        l.append(item)
print(l)

rl= [x for x in my_list if not x%2]
print(rl)


z= True 
while z == True:
    a = int(input("Enter mark: "))
    if a > 85:
         print('distinction')
    elif 65 <= a <= 85:
        print('pass')
    elif a == 0:
        z=False
        print("finished")
    else:
        print('Fail')
