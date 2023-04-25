import face_recognition
import cv2
import os
from flick import settings

def processor():
    files_dict = {}
    files = os.listdir(os.path.join(settings.STATIC_DIR, "img/actors"))
    files_dict['files'] = files

    unkown_image = face_recognition.load_image_file('screenshot.png')

    try:
        unkown_encoding = face_recognition.face_encodings(unkown_image)[0]
    except IndexError as e:
        return None
    
    for index,file in enumerate(files_dict['files']):
        known_image = face_recognition.load_image_file(f"static/img/actors/{file}")
        known_encoding = face_recognition.face_encodings(known_image)[0]

        results = face_recognition.compare_faces([known_encoding], unkown_encoding)
        if results[0] == True:
            return file.strip('.jpeg')
        else:
            if index == len(files_dict['files'])-1:
                return None
        
        

def face_drawer():
    # Read the image
    image = cv2.imread('screenshot.png') 

    faces = face_recognition.face_locations(image)

    # Draw a rectangle around the faces
    for (top, right, bottom, left) in faces:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imwrite('faces.png', image)

