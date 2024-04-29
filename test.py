import cv2

# หากใช้กล้อง USB
cap = cv2.VideoCapture(0)

# หากใช้กล้อง Raspberry Pi
# cap = cv2.VideoCapture("video0", cv2.CAP_V4L2)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()