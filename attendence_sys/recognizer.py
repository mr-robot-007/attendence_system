import face_recognition
import numpy as np
import cv2

""" Recognizer() - capture frames from webcam and compares faces with the known faces and returns the red_id, names of the matched faces """


def Recognizer(known_face_encodings, known_face_names):

    # capture video via webcam at port 0
    video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    names = []
    face_locations = []
    face_encodings = []

    while True:
        # reads video being captures
        check, frame = video.read()

        # resizes the camera frame
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        rgb_small_frame = small_frame[:, :, ::-1]

        # generates location and encodings for faces in the webcame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)
        face_names = []

        # compares generated encodings with known_face_encodings
        # if matches - adds names of  best match face from  known_face_names[] to names[]
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(
                known_face_encodings, np.array(face_encoding), tolerance=0.6)
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding)

            try:
                matches = face_recognition.compare_faces(
                    known_face_encodings, np.array(face_encoding), tolerance=0.6)

                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    face_names.append(name)
                    if name not in names:
                        names.append(name)
            except:
                pass

        # shows rectangle over the detected faces in the webcam
        # if rectangle = red -> unknown face
        # if rectangle = green -> known and shows reg_id of the face
        if len(face_names) == 0:
            for (top, right, bottom, left) in face_locations:
                top *= 2
                right *= 2
                bottom *= 2
                left *= 2
                cv2.rectangle(frame, (left, top),
                              (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, 'Unknown', (left, top),
                            font, 0.8, (255, 255, 255), 1)
        else:
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 2
                right *= 2
                bottom *= 2
                left *= 2
                cv2.rectangle(frame, (left, top),
                              (right, bottom), (0, 255, 0), 2)
                # cv2.rectangle(frame, (left, bottom - 30), (right,bottom - 30), (0,255,0), -1)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left, top),
                            font, 0.8, (255, 255, 255), 1)

        cv2.imshow("Face Recognition Panel", frame)

        # to stop the webcam press 's' - saves attendance
        if cv2.waitKey(1) == ord('s'):
            break

    # closes webcam and destroy webcam window and return the names[]
    video.release()
    cv2.destroyAllWindows()
    return names
