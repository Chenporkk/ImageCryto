from os import pipe 
import cv2
from PIL import Image
import numpy as np
from encrypt import AESCipher

imageName = 'dataset.jpg'
photo = Image.open(imageName)
photo = photo.convert('RGB')

im = Image.new(mode = "RGB", size = photo.size)
pixels = im.load()

arr = np.empty(photo.size, dtype=object)

width = photo.size[0] 
height = photo.size[1]
key = input("Enter Key: ")
print("Encrypting Image... \nPlease wait!")
AES1 = AESCipher(key)
for y in range(0, height):
    row = ""
    for x in range(0, width):

        RGB = photo.getpixel((x,y))
        R,G,B = RGB  
        piS = str(R)+"s"+str(G)+"s"+str(B)
        arr[x,y] = AES1.encrypt(piS)

np.savetxt(imageName, arr, fmt="%s")
print("Encrypt Successful!!")