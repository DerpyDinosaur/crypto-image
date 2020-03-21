# Imports
from PIL import Image
import hashlib

"""
	Encryption Algorthim

	- Get users key
	- hash key and add digest to the beggining of key

	- Get Pixel
	139, 195, 74, 255

	- Add a letter to RGB and modular by 42
	139, 195, 74, 255
	118,  46, 53, 255
	
	- Permutate RGB == BRG
	53, 118, 46
"""

# Image to encrypt
imagePath = input("Where is the image you would like to encrypt\n> ")

try:
	image = Image.open(imagePath)
except:
	print("\nError: Image was not found!!!")
	exit()

px = image.load()
newColour = [0,0,0,255]
keyCount = 0

# Enter a password
key = input("\nPlease enter your password\n> ")

# This increases strength for basic keys
# It also prevents users using repetitive passwords
hashKey = hashlib.md5(key.encode())
key = hashKey.hexdigest()

# Change key into a decimal
key = [ord(c) for c in key]

# Get width and height of image
width, height = image.size

for x in range(width):
	for y in range(height):
		lastColour = list(px[x,y])
		###################################################################
		# Encryption algorithm goes here

		# Permutate
		newColour = [lastColour[2], lastColour[0], lastColour[1], 255]


		# Encrypt pixel
		for i in range(3):
			# Reset keyCount if out of bounds
			if keyCount == len(key): keyCount = 0

			newColour[i] = (key[keyCount] + newColour[i]) % 128
			keyCount = keyCount+1
		###################################################################
		px[x,y] = tuple(newColour)

image.save('encrypted.png')
print("\nEncryption complete!")
print("The image will be located where this python script is")
print("The name should be 'encrypted.png'")