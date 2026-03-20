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
url= "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
response=requests.get(url)
image=Image.open(BytesIO(response.content))
width,height=image.size
gcd=math.gcd(height,width)
height=height//gcd
width=width//gcd
print(f"Aspect Ratio={width}:{height}")
if width==16 and height==9:
    print("Modern screens ratio")
elif width==9 and height==16:
    print("Vertical videos ratio")
elif width==4 and height==3:
    print("Old monitor ratio")
elif width==3 and height==2:
    print("Usal cameras ratio")
elif width==1 and height==1:
    print("Square ratio")
if width>height:
    print("Work for landscape")
elif width<height:
    print("Work for portrait")
