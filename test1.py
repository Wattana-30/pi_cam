import cv2
import threading

# ฟังก์ชันสำหรับอ่านภาพจากกล้อง USB
def usb_camera_thread():
    cap_usb = cv2.VideoCapture(0)
    while True:
        ret, frame = cap_usb.read()
        cv2.imshow('USB Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap_usb.release()

# ฟังก์ชันสำหรับอ่านภาพจากกล้อง CSI
def csi_camera_thread():
    cap_csi = cv2.VideoCapture(1)
    while True:
        ret, frame = cap_csi.read()
        cv2.imshow('CSI Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap_csi.release()

# สร้างเธรดสำหรับกล้อง USB
usb_thread = threading.Thread(target=usb_camera_thread)

# สร้างเธรดสำหรับกล้อง CSI
csi_thread = threading.Thread(target=csi_camera_thread)

# เริ่มเธรด
usb_thread.start()
csi_thread.start()

# รอให้เธรดทำงานเสร็จสิ้น
usb_thread.join()
csi_thread.join()

cv2.destroyAllWindows()
