celsius_temperature = int(input("Please enter an integer value."))

def fahrenheit(C):
    F=1.8*C+32
    return F

#print(fahrenheit(celsius_temperature))
print("The Fahrenheit equivalent of " + str(celsius_temperature) + " degrees Celsius is " + str(round(fahrenheit(celsius_temperature), 1)))
