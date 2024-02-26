"""Turn image into ascii art"""

from PIL import Image
import os

chars = ["@", "#", "D", "%", "*", "?", "+", "R", "$", ",", "."]
img = None

def pixel_to_ascii(img_2, W):
    pixels = list(img_2.getdata())
    ascii_pixel = [chars[pixel_values//W] for pixel_values in pixels]

    return "".join(ascii_pixel)

def image_to_ascii(img_2, W):
    pixels_to_chars = pixel_to_ascii(img_2, W)
    len_pixels_to_chars = len(pixels_to_chars)
    image_ascii = [pixels_to_chars[index: index + W] for index in range(0, len_pixels_to_chars, W)]
    return "\n".join(image_ascii)

def main():

    try:
        img = Image.open("button.jpg")
    except IOError:
        pass

    W, H = img.size

    new_size = (int(W/4), int(H/4))
    

    img2 = img

    img2 = img.resize(new_size)

    img2 = img2.convert("L")

    image_ascii = image_to_ascii(img2, new_size[0])

    f = open(os.path.splitext("button.jpeg")[0]+'.txt','w')
    f.write(image_ascii)
    f.close()

main()