import cv2
# Install the CMake library first before dlib library
import dlib

# What number of camera do you use
cam = cv2.VideoCapture(0)
# Get the face coordinates
detect = dlib.get_frontal_face_detector()

# Continously playing
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = detect(gray)
# counting faces
    i = 0
    for face in face:
        # Get coordinates faces
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        i = i + 1

        # Displaying faces
        cv2.putText(frame, 'face' + str(i), (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(face, 1)

    # Result
    cv2.imshow('box', frame)
    # this command will let you quit if you press "r" button keyboard
    if cv2.waitKey(1) & 0xFF == ord('r'):
        break

cam.release()
cv2.destroyAllWindows()
