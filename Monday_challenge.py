
a = int(input( "type a number ranging from 0-99: "))
b = int(input( "type a number ranging from 0-99: "))
def even_number(x,y):
    items = []
    for i in range(x,y):
        s = str(i)
        if (int(s[0])%2==0) and (int(s[1])%2==0): 
            items.append(s)
    return items

print(even_number(a,b))


    
    