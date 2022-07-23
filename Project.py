import cv2
import numpy as np

video = cv2.VideoCapture("Green2.mp4")
# video = cv2.VideoCapture(0)
image = cv2.imread("bg img.jpg")

def nothing():
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 300, 300)

cv2.createTrackbar("L-H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255, 255, nothing)

while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    l_h = cv2.getTrackbarPos("U-H", "Trackbars")
    l_s = cv2.getTrackbarPos("U-S", "Trackbars")
    l_v = cv2.getTrackbarPos("U-V", "Trackbars")

    l_g = np.array([32, 54, 32])
    u_g = np.array([179, 255, 255])

    mask = cv2.inRange(hsv, l_g, u_g)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    f = frame - res
    green_screen = np.where(f==0, image, f)
    cv2.imshow("final", green_screen)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()