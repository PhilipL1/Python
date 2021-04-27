a = int(input( "Enter lower bound ranging from 10-99: "))
b = int(input( "Enter upper bound ranging from 10-99: "))
def even_number(x,y):
    if x>y:
        x, y = y, x
    items = []
    for integer in range(x,y+1):
        string = str(integer)
        for char in string:
            if (int(char)%2==0):
                pass
            else : 
                break
        else:
            items.append(string)
    return items
print(even_number(a,b))
