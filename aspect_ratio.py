"""
Create a program that calculates the aspect ratio of an
image from a URL.
- Example URL:
  https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
- By ratio we refer, for example, to the "16:9" of an
  image with a resolution of 1920*1080px.

"""
import requests
from PIL import Image
from io import BytesIO
import math

url= "https://i.pinimg.com/originals/49/dc/85/49dc8564e17e811fcbcfe076144d5082.jpg"

response=requests.get(url)

image=Image.open(BytesIO(response.content))

width,height=image.size
print(width)
print(height)
gcd=math.gcd(height,width)
height=height//gcd
width=width//gcd

print(f"The ratio from the image is {width}:{height}")
#image.show()


