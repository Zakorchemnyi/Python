some_dictionary = {"Queen": "Bohemian Rhapsody", 
                   "Bee Gees": "Stayin' Alive", 
                   "U2": "One", 
                   "Michael Jackson": "Billie Jean", 
                   "The Beatles": "Hey Jude", 
                   "Bob Dylan": "Like A Rolling Stone"
                   }
print(len(some_dictionary))
print(some_dictionary.keys())
for key in some_dictionary.keys():
    print(key)
for values in some_dictionary.values():
    print(values)
for key, value in some_dictionary.items():
    print(key, value)
print(some_dictionary.get("Promise of the Real", " the key is not found"))