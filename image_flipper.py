import cv2
import imutils
import numpy

def convert_image (url, filename):
# Convert "HTTPS" to "HTTP"
	first_chars = url[0:5]
	if first_chars == "https":
		url = url[5:]
		url = "http" + url
	else:
		url = url

# Declare Filename
	filename = filename + '.jpeg'

# Pull Image from URL
	img = imutils.url_to_image(url)

# Image Size Exceptions
	chwidth = img.shape[1]
	chheight = img.shape[0]
	if chwidth < 800 or chheight < 200:
		status = "Image has a width < 800px or a height < 200px, please process manually!"
	else:
		status = "Success, File on Desktop"

# Adding Alpha Channel to Image
	BGRA = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
	BGRA[:,:,3] = 255

# Resizing
	resized = imutils.resize(BGRA, width=800)

# Mirror
	mirror = cv2.flip(resized, 0)

# Crop Params
	width, height = 800, 200
	x, y = 0, 0

# Crop
	cropped = mirror[y:y+height, x:x+width]

# Design Gradient
	ht, wd = cropped.shape[:2]
	pct = 99
	ht2 = int(ht*pct/100)
	ht3 = ht - ht2
	top = numpy.full((ht3,wd), 255, dtype=numpy.uint8)
	btm = numpy.linspace(200, 0, ht2, endpoint=True, dtype=numpy.uint8)
	btm = numpy.tile(btm, (wd,1))
	btm = numpy.transpose(btm)
	alpha = numpy.vstack((top,btm))

# Assign Gradient to Alpha
	result = cropped.copy()
	result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
	result[:,:,3] = alpha

# Merge Both Images
	final = numpy.concatenate((resized, result), axis=0)
	filename = "/Users/work/Desktop/" + filename

# Convert Alpha to White
	B, G, R, A = cv2.split(final)
	alpha = A / 255
	R = (255 * (1 - alpha) + R * alpha).astype(numpy.uint8)
	G = (255 * (1 - alpha) + G * alpha).astype(numpy.uint8)
	B = (255 * (1 - alpha) + B * alpha).astype(numpy.uint8)

# Print File
	final = cv2.merge((B, G, R))

# Write File
	cv2.imwrite(filename, final)
	return(status)