 # <QUESTION 3>

    # Given a dictionary mapping keys to values, return a new dictionary mapping the values
    # to their corresponding keys

    # <EXAMPLES>

    # three({'hello':'hola', 'thank you':'gracias'}) → {'hola':'hello', 'gracis':'thank you'}
    # three({101:'Optimisation', 102:'Partial ODEs'}) → {'Optimisation':101, 'Partial ODEs':102}

    # <HINT>

    # Dictionaries have methods that can be used to get their keys, values, or items

def three(dictionary):
    new_dict ={}
    for key, value in dictionary.items():
        new_dict[value]=key
    return new_dict

print(three({'hello':'hola', 'thank you':'gracias'}))
print(three({101:'Optimisation', 102:'Partial ODEs'}))
   

    