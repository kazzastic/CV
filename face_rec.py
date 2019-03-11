from PIL import Image
import face_recognition
import numpy as np
import argparse
import cv2


# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])

#find all the faces in the image
face_loc = face_recognition.face_locations(image)

#printing the nimber of itens in the array
print("I have found {} faces in this photo".format(len(face_loc)))

for face_loc in face_loc:
    top, right, bot, left = face_loc
    print("A face is located at pixel location Top:{}, Left:{}, Bottom:{}, Right:{}".format(top,left,right,bot))

    face_image = image[top:bot, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()






          
