import string
from random import randint 



def main():
    length = int(input("How many characters in password? [8-25]: "))
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    numeral = list(string.digits)
    special = ["!", "?", "$", "&", "/", "-", "="]
    final= []

    for x in range(length):

        answer= randint(1,4)
        if answer == 1:
            char= lower[randint(0,len(lower))]
            final.append(char)
        elif answer== 2:
            char = upper[randint(0,len(upper))]
            final.append(char)
        elif answer == 3:
            char = numeral[randint(0,len(numeral))]
            final.append(char)
        elif answer == 4: 
            char = special[randint(0,len(special))]
            final.append(char)
    return print("".join(final))



main()
