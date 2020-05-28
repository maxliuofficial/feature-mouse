# try to figure out landmark detection in video

import cv2

cap = cv2.VideoCapture(0)
while True:
  # Getting our image by webcam and converting it into a gray image scale
    ret, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # show the gray image
    cv2.imshow("Output", image)
    
    #key to give up the app.
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()