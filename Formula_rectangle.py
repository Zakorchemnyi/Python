length = int(input("First Side"))
width = int(input("Second Side"))
height = int(input("Third Side"))

def calculate_the_volume_of_a_rectangular_prism(length, width, height):
    volume = length*width*height
    return volume 

print("The volume of the rectangular prism is " + str(calculate_the_volume_of_a_rectangular_prism(2, 2, 1)) + " cubic feet.")