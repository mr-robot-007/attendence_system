import os
import face_recognition

def Encoder():
    known_face_encodings = []
    known_face_names = []

    base_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.getcwd()
    image_dir = os.path.join(base_dir, "{}\{}\{}".format(
        'static', 'images', 'Student_Images'))

    for root, dirs, files in os.walk(image_dir):

        for file in files:
            if file.endswith('jpg') or file.endswith('png'):
                path = os.path.join(root, file)
                img = face_recognition.load_image_file(path)
                label = file[:len(file)-4]
                img_encoding = face_recognition.face_encodings(img)[0]
                known_face_names.append(label)
                known_face_encodings.append(img_encoding)
    return known_face_encodings,known_face_names 


