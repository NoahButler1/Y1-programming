print("pick one from the following list of 6 Greek Gods and i will guess which one you pick: ")
print("Zeus, Poseidon, Ares, Aphrodite, Athena, Artemis \n")

Male = input("are they a male, yes or no? ")

if Male.upper() == "YES":
    King = input("are they known as the king of the gods, yes or no? ")
    if King.upper() == "YES":
        print("the god you are thinking of is zeus")

    else:
        Blue = input("are they associated with the colour blue, yes or no? ")
        if Blue.upper() == "YES":
            print("the god you are thinking of is poseidon")

        else:
            print("the god you are thinking of is ares")

elif Male.upper() == "NO":
    Weapon = input("do they have a weapon, yes or no? ")
    if Weapon.upper() == "NO":
        print("the god you are thinking of is aphrodite")

    else:
        Wise = input("are they associated with knowledge and wisdom, yes or no? ")
        if Wise.upper() == "YES":
            print("the god you are thinking of is athena")

        else:
            print("the god you are thinking of is artemis")

else:
    print("user input is invalid")


