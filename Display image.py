import cv2
img = cv2.imread(r"C:\Users\Dr. C. B. Majumder\Desktop\mrkalopsia.jpg",1)
resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow(r"C:\Users\Dr. C. B. Majumder\Desktop\mrkalopsia.jpg",resized)
cv2.waitKey(210000)
cv2.destroyAllWindows()