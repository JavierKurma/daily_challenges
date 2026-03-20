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

url= " https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

response=requests.get(url)

image=Image.open(BytesIO(response.content))

height,widht=image.size

print(image.size)
#print(image.show())
print(f"Altura= {height}, Largo= {widht}")

