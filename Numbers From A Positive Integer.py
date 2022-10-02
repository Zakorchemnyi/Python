positive_integer = int(input("Please enter a number"))
# counter = 0
# while positive_integer > counter:
#     counter+=positive_integer
#     positive_integer -=1

# print(positive_integer)
# print(counter)
sum = 0
a = 1
b = positive_integer
while a<=b:
#    print("hello")
#    print(b)
    sum+=b
    b-=1
print("the sum found by the while loop." + str(sum))
print("user entered integer is " + str( positive_integer))