my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
l= []
for item in my_list:
    if item%2 ==0:
        l.append(item)
print(l)

rl= [x for x in my_list if not x%2]
print(rl)