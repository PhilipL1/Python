 # <QUESTION 1>

    # Given a word and a string of characters, return the word with all of the given characters
    # replaced with underscores

    # This should be case sensitive

    # <EXAMPLES>

    #→ "h_ll_ w_rld"
  # "_i_geri___"
    #→ "punctuation__or_something_"

def one(word, chars):
    for char in chars:
        z = word.replace(char,"_")
    return z
 
print(one("hello world", "aeiou"))   
print(one("didgeridoo", "do"))
print(one("punctation, or something?", ",?"))