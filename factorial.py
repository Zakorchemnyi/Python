def factorial():
    counter = 0
    sum = 1
    some_number = int(input("Enter positive integer"))
    while counter<some_number:
        counter += 1
        sum *= counter
        #print(counter)
    print(sum)
factorial()
