import io
import os
import time
from picamera2 import Picamera2
import pprint
import requests

ip = os.getenv("SERVER_IP")
OBJ_DETECTION_URL = f"http://{ip}:5000/v1/vision/detection"
if __name__ == "__main__":
    if os.getenv("CAMERA_ON", "true").lower() == "true":

        picam2 = Picamera2()
        camera_config = picam2.create_preview_configuration()
        picam2.configure(camera_config)
        picam2.start()
        while(True):
            time.sleep(1)
            data = io.BytesIO()
            picam2.capture_file(data, format='jpeg')
            data.seek(0)
            response = requests.post(OBJ_DETECTION_URL, files={"image": data}).json()
            pprint.pprint(response)
    else:
        OBJ_DETECTION_TEST_IMAGE = "image.jpg"
        OBJ_image_data = open(OBJ_DETECTION_TEST_IMAGE, "rb").read()
        while (True):
            time.sleep(1)
            response = requests.post(OBJ_DETECTION_URL, files={"image": OBJ_image_data}).json()
            pprint.pprint(response)