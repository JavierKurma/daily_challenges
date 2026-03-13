"""
Create a single function (it is important that it is only one) that is capable
of calculating and returning the area of a polygon.
- The function will receive only ONE polygon at a time as a parameter.
- The supported polygons will be Triangle, Square, and Rectangle.
- Print the area calculation of one polygon of each type.

"""
def area_polygon(base,height,sides)->float:
    if sides==3:
        return base*height/2
    else:
        return base*height
print("Input the base and height of a rectangle or triangle: ")
while True:
    try:
        base=int(input("base-> "))
        break
    except ValueError:
        print("Input a valid number")
while True:
    try:
        height=int(input("height-> "))
        break
    except ValueError:
        print("Input a valid number")
while True:
    try:
        side=int(input("side-> "))
        if side ==2 or side ==3:
            break
        else:
            print("Input 2 or 3")
            continue
        break
    except ValueError:
        print("Input a valid number of sides")

area=area_polygon(base,height,side)
print(f"The area of the polygon with (base,height)=({base},{height}) is {area}")
