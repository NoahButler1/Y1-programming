complete = "no"

while complete != "yes":
    feathers = input("does it have feathers? ")
    if  feathers.upper() == "NO":
    
        weapons = input("does it have spines/thorns/horns? ")
        if weapons.upper() == "YES":
        
            club = input("does it have a club like tail? ")
            if club.upper() == "NO":
                print("it is a spinosaurus, you are not safe, run and hide")
                complete = "yes"
            
            elif club.upper() == "YES":
                print("it is an ankylosaurus, you are safe")
                complete = "yes"

            else:
                print("unrecognised answer, must be yes or no")

        elif weapons.upper() == "NO":
            
            neck = input("does it have a long neck? ")
            if neck.upper() == "NO":
                
                print("it is a t rex, you are not safe, run and hide")
                complete = "yes"

            elif neck.upper() == "YES":
                print("it is a brachiosaurus, you are safe")
                complete = "yes"

            else:
                 print("unrecognised answer, must be yes or no")

        else:
            print("unrecognised answer, must be yes or no")

    elif feathers.upper() == "YES":
        
        small = input("is it small? ")
        if small.upper() == "NO":
            
            print("it is a deinonychus, you are not safe, run and hide")
            complete = "yes"

        elif small.upper() == "YES":
            print("it is a dodo, you are safe")
            complete = "yes"

        else:
            print("unrecognised answer, must be yes or no")

    else:
        print("unrecognised answer, must be yes or no")
