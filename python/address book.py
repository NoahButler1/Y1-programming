found = "false"
file = open("address book.csv" , "r")
line = file.readline()
SearchTerm = str(input("enter a name/postcode/town/phone number to search by: "))

while(line):
    data = line.split(",")
    
    if data[0] == SearchTerm:
        print("Name: ", data[0])
        print("Postcode: ", data[1])
        print("Town: ", data[2])
        print("Phone number: ", data[3])
        found = "true"
       

    elif data[1] == SearchTerm:
        print("Name: ", data[0])
        print("Postcode: ", data[1])
        print("Town: ", data[2])
        print("Phone number: ", data[3])
        found = "true"
 

    elif data[2] == SearchTerm:
         print("Name: ", data[0])
         print("Postcode: ", data[1])
         print("Town: ", data[2])
         print("Phone number: ", data[3])
         found = "true"
    

    elif  SearchTerm.isdigit() == True:
        if int(data[3]) == int(SearchTerm):
            print("Name: ", data[0])
            print("Postcode: ", data[1])
            print("Town: ", data[2])
            print("Phone number: ", data[3])
            found = "true"

   
    line = file.readline()




if found != "true":
    print("item not found")
