#asks user for the temperature and what they want to conver it to
TempConversion = input("are you converting to celsius or fahrenheit? ")
Temp = int(input("what is the current temperature? "))

#makes the conversion type uppercase
Conversion = TempConversion.upper()

#checks if the user entered celsius
if Conversion == "CELSIUS": 
    #converts the temperature to celsius
    TempCelsius = float((Temp - 32) / 1.8)

    #rounds the calculated temp
    TempCelsius = round(TempCelsius,2)

    #outputs the calculated temperature
    print(Temp, "degrees fahrenheit is ", TempCelsius, "degrees celsius")

#checks if user entered fahrenheit
elif Conversion == "FAHRENHEIT":

    #converts the temperature to fahrenheit
    TempFahrenheit = float((Temp * 1.8) + 32)

    #outputs the calculated temperature
    print(Temp, "degrees celsius is ", TempFahrenheit, "degrees fahrenheit")

#if the user enters something that isnt celsius or fahrenheit, displays and error message    
else:
    print("sorry i didn't understand that")