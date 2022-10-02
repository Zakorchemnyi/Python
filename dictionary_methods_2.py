some_dict = {}.fromkeys("bcd", "consonants")
#print(some_dict)
for key in some_dict.items():
    print(key)

fast_food_items = {"McDonald's": "Big Mac", 
                   "Burger King": "Whopper", 
                   "Chick-fil-A": "Original Chicken Sandwich"}
fast_food_items.pop("McDonald's")
print(fast_food_items["Burger King"])
fast_food_items.popitem()
print(fast_food_items)