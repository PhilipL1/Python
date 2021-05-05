from dice import roll_dice as first_dice

def second_dices():
    a=[]
    for i in range(2):
       a.append(first_dice())
    return a
print(second_dices())