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
while
