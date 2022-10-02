a = input("Чи в вас є автомобіль(ТАК або НІ)")
if a=="ТАК":
    b = float(input("Кількість бензину в бензобаку в вашому авто(Введіть число)"))
    if b>0:
        print("Ви можете їхати")
    else:
        print("Ви не можете їхати бо у вас немає бензини")
else:
    print("Ви не можете їхати бо нема машини")
# if a >= 3.7:
#     if b == "YES":
#         print("Selected Yes")
#     else: print("Selected NO")
#     print("Number is equal or greater of 7")
# else:
#     print("Has not enough grades and qualify")
#    print("It is >=3,7")
#if b=="YES":
#    print("It is NO")
#else:print("It is NO no")
#else:
#    print("Ni to ni to")