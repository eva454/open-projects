# this project is done in collaboration with Jorge Henriquez (https://github.com/penguingovernor)
from PIL import Image
import argparse
import sys


# Get the photo from the command line
parser = argparse.ArgumentParser(description="turns a photo into a ppm file")
parser.add_argument('--photo', dest="photo", metavar='p', type=str)
parser.add_argument('--output', dest="output", metavar='o', type=str)

args = parser.parse_args()
photoStr = args.photo
ppmFile = args.output

# Check if a photo was a passed in.
if photoStr == None:
    print("Give me a photo please.")
    # In UNIX, exiting with a
    # non zero status means that an error occurred.
    error = 1
    exit(error)
else:
    # open the image.
    image = Image.open(photoStr)

    # gets the ppm header ready
    # bytearray is an array of binary values
    # encode utf 8 makes sure that the string gets converted correctly from decimal to binary
    # They need to be in str
    p6 = bytearray("P6\n", "utf-8")
    w_h = bytearray("32 32\n", "utf-8")
    max_color_brightness = bytearray("255\n", "utf-8")

    # New file_file contains the ppmFile
    # ppmFile is the ppm file passed in from arguments in the command line
    # open the ppmFile and write to it in binary (hence the "wb")
    new_file = open(ppmFile, "wb")

    # writes to ppmFile to new_file
    new_file.write(p6)
    new_file.write(w_h)
    new_file.write(max_color_brightness)
    new_file.flush()

    # resize it
    image_resized = image.resize((32, 32))
    # image_resized.save("whatever.ppm")

    # tPixel gets the pixel values of the 32x32 photo
    # tPixel is a list of lists, where each sublist contains the [r,g,b] value
    # of each individual pixel
    tPixel = list(image_resized.getdata())

    # iterating through the list of lists in tPixel
    # so each pix will contain a sublist i.e. [r,g,b]
    for pix in tPixel:
        # bytearray turns a decimal sublist into a binary sublist
        byt = bytearray(pix)
        # and writes it to the new_file
        new_file.write(byt)
