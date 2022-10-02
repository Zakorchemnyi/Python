two_inputs = range(1, 51)
for num in two_inputs:
    if num%3!=0 and num%5!=0:
        print(num)
    if num%3==0 and num%5==0:
        print(str(num) +"FizzBuzz")
    elif num%3==0:
        print(str(num) + "FIZZ")
    elif num%5==0:
       print(str(num) + "BUZZ")


    #else: 
    #    print(num)