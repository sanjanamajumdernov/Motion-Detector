import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread (r"C:\Users\Dr. C. B. Majumder\Desktop\F.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05 , minNeighbors=5)
print(faces)
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,277,0),2)
cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
