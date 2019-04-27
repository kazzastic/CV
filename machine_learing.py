import face_recognition
from PIL import Image, ImageDraw


#Load the image and learn to recognize it
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

#load second image and learn it
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

#third image
saad_image = face_recognition.load_image_file("asad.jpeg")
saad_face_encoding = face_recognition.face_encodings(saad_image)[0]

#Create arrays of known face encodings and thier names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    saad_face_encoding
    ]
known_face_names = [
    "Barak Boi" ,
    "Biden Darling" ,
    "Saad"
    ]

#load an image of an unknown face
unknown_image = face_recognition.load_image_file("saadbhai.jpeg")

#find all the faces and face encodings in the unknown image
face_loc = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_loc)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
pil_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(pil_image)

#Loop thorugh each face found in unknown image
for (top, right, bottom, left), face_encoding in zip(face_loc, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    text_width , text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
del draw
pil_image.show()
