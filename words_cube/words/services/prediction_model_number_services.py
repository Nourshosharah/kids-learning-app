import os
import json
import pickle
import numpy as np
from PIL import Image
from skimage.transform import resize
from skimage.io import imread,imsave
from skimage import data
from skimage.color import rgb2gray
import cv2
import pytesseract
import io
from django.http import HttpResponse

services_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.dirname(services_dir))
new_root=os.path.abspath(os.path.dirname(project_root))

path_data = os.path.join(project_root, 'resources\\')






def predict_number(request_data):
    
    if request_data.FILES["image"]:
        print("hello from if")
        im_file = request_data.FILES["image"]
        im_bytes = im_file.read()
        im = Image.open(io.BytesIO(im_bytes))

    print("finsish read request dataaa")
    # path_hubconfig=r'E:\words_cube\words_cube\yolov5'
    # path_weightfile=r'E:\words_cube\words_cube\yolov5\models\yolov5s.pt'
    
    data=np.array(im)
    imsave("out1.jpg",data)
    img=imread('out1.jpg')
    

    # Cvt to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get binary-mask
    msk = cv2.inRange(hsv, np.array([0, 0, 175]), np.array([179, 255, 255]))
    krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
    dlt = cv2.dilate(msk, krn, iterations=1)
    thr = 255 - cv2.bitwise_and(dlt, msk)

    # OCR
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\NOUR\AppData\Local\Tesseract-OCR\tesseract.exe'
    d = pytesseract.image_to_string(thr, config="--psm 10")
    print(d)



    
    
    return {'data':d}
    # return results.pandas().xyxy[0].to_json(orient="records")
