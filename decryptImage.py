import numpy as np
from encrypt import AESCipher
from PIL import Image
from sys import exit

def DecrypImg(img):
    img = np.loadtxt(imageName, dtype=str)
    height = len(img[0])
    width = len(img)

    im = Image.new(mode = "RGB", size = (width, height))
    pixels = im.load()
    key = input("Enter Key: ")
    AES2 = AESCipher(key)
    print("Decrypting Image... \nPlease wait!")
    for y in range(0, height): 
        for x in range(0, width):
            try:
                getstr = AES2.decrypt(img[x,y])
                arrstr = getstr.split("s")
                pixels[x,y] = (int(arrstr[0]), int(arrstr[1]), int(arrstr[2]))
            except:
                return "";
    return im

imageName = 'dataset.jpg'
im = DecrypImg(imageName)
if(im):
    im.save(imageName)
    print("Decrypt Successful!!")
else:
    print("Wrong Key!!")
