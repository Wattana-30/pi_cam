from picamera import PiCamera
from time import sleep

camera = PiCamera()

# กำหนดค่าสำหรับการแสดงตัวอย่างให้เป็น YUV420
camera.resolution = (960, 720)
camera.framerate = 30
camera.start_preview()

# รอเป็นเวลา 5 วินาที
sleep(5)

# ปิดกล้อง
camera.stop_preview()
