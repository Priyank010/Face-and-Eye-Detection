import cv2

eye_cascade = cv2.CascadeClassifier('.\Data\haarcascade_eye.xml')
nadia = cv2.imread('./Data/Nadia_Murad.jpg',0)

def detect_eyes(img):
    face_img = img.copy()
    eyes = eye_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5) 
    
    for (x,y,w,h) in eyes: 
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10) 
    return face_img

result = detect_eyes(nadia)

while True:
    cv2.imshow('',result)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break