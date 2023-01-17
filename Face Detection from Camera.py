import cv2

face_cascade = cv2.CascadeClassifier('.\Data\haarcascade_frontalface_default.xml')

def detect_face(img):
    face_img = img.copy()
    face_rect = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5)

    for (x,y,w,h) in face_rect:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)
    return face_img

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    frame = detect_face(frame)
    cv2.imshow('Face Detection',frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()