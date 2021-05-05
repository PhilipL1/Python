for i in range(1,51):
    rs=''
    if not i%3:
        rs+='Fizz'
    if not i%5:
        rs='Buzz'
    if rs:
        print(rs)
    else :
        print(i)