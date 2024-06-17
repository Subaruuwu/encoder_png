import cv2
from PIL import Image
import numpy as np


def save_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)
    return filename


def capture_image_from_camera():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


def load_image_from_disk(path):
    image = Image.open(path)
    return np.array(image)
