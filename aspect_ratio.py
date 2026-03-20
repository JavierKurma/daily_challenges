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
ratio_h=height//gcd
ratio_w=width//gcd
print(f"Aspect Ratio={ratio_w}:{ratio_h}")
if ratio_w==16 and ratio_h==9:
    print("Modern screens ratio")
elif ratio_w==9 and ratio_h==16:
    print("Vertical videos ratio")
elif ratio_w==4 and ratio_h==3:
    print("Old monitor ratio")
elif ratio_w==3 and ratio_h==2:
    print("Usual cameras ratio")
elif ratio_w==1 and ratio_h==1:
    print("Square ratio")
if ratio_w > ratio_h:
    print("Landscape orientation")
elif ratio_w < ratio_h:
    print("Portrait orientation")
