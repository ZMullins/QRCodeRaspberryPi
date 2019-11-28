# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
 
# construct the argument parser and parse the arguments

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
# vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
 
# open the output CSV file for writing and initialize the set of
# barcodes found thus far
# loop over the frames from the video stream
while True:
    # grab the frame from the threaded video stream and resize it to
    # have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # find the barcodes in the frame and decode each of the barcodes
    barcodes = pyzbar.decode(frame)
    # loop over the detected barcodes
    #for barcode in barcodes:
    # extract the bounding box location of the barcode and draw
    # the bounding box surrounding the barcode on the image
    if len(barcodes)>0:
	#(x, y, w, h) = barcodes.rect
	#cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# the barcode data is a bytes object so if we want to draw it
	# on our output image we need to convert it to a string first
	barcodeData = barcodes[0].data.decode("utf-8")
	barcodeType = barcodes[0].type

	# draw the barcode data and barcode type on the image

	# if the barcode text is currently not in our CSV file, write
	# the timestamp + barcode to disk and update the set
	print("Found!")
	print(barcodeData)
	f =open("currentuser.txt","w")
	f.write(barcodeData)
	f.close()
	break


# close the output CSV file do a bit of cleanup

vs.stop()	
			
                
