import random
Cnumber= random.randrange(1,101)
UserNumber=int(input("ENTER YOUR NUMBER :-"))
if UserNumber>Cnumber:
    print("COMPUTER NUMBER",Cnumber)
    print("YOU GUESSED HIGHER NUMBER")
    print("PLEASE TRY AGAIN")
elif  UserNumber<Cnumber:
    print("COMPUTER NUMBER",Cnumber)
    print("YOU GUESS LOWER NUMBER")
    print("PLEASE TRY AGAIN")
else:
    print("COMPUTER NUMBER",Cnumber)
    print("YOUR GUESS IS RIGHT ")
    print("YOU WON THE GAME")
