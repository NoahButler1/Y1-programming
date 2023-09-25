#defines variables for later use and creates the list the sequence is stored in
sequence = [1 , 1]
x = 0
y = 1
num3 = 0

#loops code until num3 is greater than 50 then stops
while num3 < 50:

    #aquires the previous two numbers in the sequence
    num1 = sequence[x]
    num2 = sequence[y]

    #adds the previous two numbers to get the next in the sequence
    num3 = num1 + num2

    #adds num3 to the end of the list
    sequence.append(num3)

    #iterates throught to keep the sequence going
    x = x + 1
    y = y + 1

#prints the finsihed sequence to the terminal
print(sequence)