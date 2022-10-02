
some_string = "Anilorak"
reversed_string = ""
some_range = range(len(some_string) - 1, -1, -1)
for letters in some_range:
    print(some_string[letters])
    reversed_string+=some_string[letters]
   
print(reversed_string) 