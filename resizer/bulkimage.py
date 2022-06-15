from PIL import Image
import PIL
import os

def resiz():
	images = [file for file in os.listdir() if file.endswith(('jpeg', 'png', 'jpg'))]
	for image in images:
	    img = Image.open(image)
	    fixed_height=420
	    height_percent = (fixed_height / float(img.size[1]))
	    width_size = int((float(img.size[0]) * float(height_percent)))
	    resized = img.resize((width_size,fixed_height), PIL.Image.NEAREST)
	    resized.save("resized_" + image, optimize=True, quality=40)

resiz()