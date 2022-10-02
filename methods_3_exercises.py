internet_celebrities = {"DrDisrespect": "YouTube", 
                        "ZLaner": "Facebook", 
                        "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
print(internet_celebrities)
print("internet_celebrities")
third_var = internet_celebrities.copy()
print (third_var)
print ("third_var")
internet_celebrities.clear()
print(internet_celebrities)
print("internet_celebrities")
print (third_var)