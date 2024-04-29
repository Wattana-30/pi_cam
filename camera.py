import cv2

# เปิดกล้อง USB
usb_cam = cv2.VideoCapture(0)  # 0 หมายถึงกล้องแรกที่ถูกตรวจจับโดยระบบ

# เปิดกล้อง Pi
# pi_cam = cv2.VideoCapture(1)  # 1 หมายถึงกล้องที่สองที่ถูกตรวจจับโดยระบบ

while True:
    # อ่านภาพจากกล้อง USB
    ret, frame_usb = usb_cam.read()
    if not ret:
        print("ไม่สามารถเปิดกล้อง USB ได้")
        break

    # อ่านภาพจากกล้อง Pi
    ret, frame_pi = pi_cam.read()
    if not ret:
        print("ไม่สามารถเปิดกล้อง Pi ได้")
        break

    # แสดงผลภาพ
    cv2.imshow('USB Camera', frame_usb)
    cv2.imshow('Pi Camera', frame_pi)

    # รอการกดปุ่ม ESC เพื่อออก
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ปิดการใช้งานกล้องและปิดหน้าต่าง
usb_cam.release()
pi_cam.release()
cv2.destroyAllWindows()
