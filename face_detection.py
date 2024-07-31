import cv2

#Create casacde classifier object
face_cascade = cv2.CascadeClassifier(r"C:\Users\augus\Desktop\openCV\harry.jpg")

# reading the image as it is
img = cv2.imread(r"C:\Users\augus\Desktop\openCV\harry.jpg")
                 
# reading img as gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# search the co ordinated of the image
faces = face_cascade.detectMultiScale (gray_img, scaleFactor = 1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)

#resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0])))

cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()