import random
import math

gallons = random.randint(10, 25)
miles = random.randint(200, 400)
mpg = miles/gallons
print(math.floor(mpg))
print(gallons)
print(miles)