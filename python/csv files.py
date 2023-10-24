file = open("gamerscore.csv" , "r")
line = file.readline()
SearchScore = int(input ("Please enter a score: "))

while(line):
    data = line.split(",")
    
    if int(data[1]) < SearchScore:
        print("Handle: ", data[0])
        print("Gamerscore: ", data[1])
   

    line = file.readline()
file.close()
