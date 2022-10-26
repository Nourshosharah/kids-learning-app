
import os
import json
import numpy as np
import pickle
import numpy as np
from PIL import Image
from skimage.transform import resize
from skimage.io import imread,imsave
from skimage import data
from skimage.color import rgb2gray
# import matplotlib.pyplot as plt
import torch
import io
from django.http import HttpResponse
 


services_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.dirname(services_dir))
new_root=os.path.abspath(os.path.dirname(project_root))
print('new_root',new_root)
path_data = os.path.join(project_root, 'resources\\')
path_hubconfig= os.path.abspath(os.path.dirname(new_root)) +'\yolov5'
print("****path_hubconfig***", path_hubconfig)
path_weightfile=path_hubconfig+'\models\\yolov5s.pt'
print("******path_weightfile******",path_weightfile)



def predict_fruit(request_data):
    print("finsish read rquest dataaa")
    model = torch.hub.load(path_hubconfig, 'custom',path=path_weightfile, source='local')
    print("lets read data ")
    if request_data.FILES["image"]:
        print("hello from if")
        im_file = request_data.FILES["image"]
        im_bytes = im_file.read()
        im = Image.open(io.BytesIO(im_bytes))
        

        results = model(im, size=640)
        results.save(path_data+"image1.png")
    print(results.pandas().xyxy[0].to_json(orient="records"))
    for img1 in results.imgs:
        img_base64 = Image.fromarray(img1)

        img_base64.save(path_data+"image1.jpg", format="JPEG")
    


    filename=path_data+"image1.jpg"
    image = Image.open(filename)
    
 
    
    f = open(filename, "rb")
    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] = 'image/png'
    response['Content-Length'] = os.path.getsize(filename)
    return response
    # return results.pandas().xyxy[0].to_json(orient="records")



