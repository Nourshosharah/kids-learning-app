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
import cv2
import pandas as pd
import numpy as np
import io
from django.http import HttpResponse



services_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.dirname(services_dir))
new_root=os.path.abspath(os.path.dirname(project_root))

path_data = os.path.join(project_root, 'resources\\')






def predict_color(request):
    x_req = request.GET.get('x_req', '')
    y_req = request.GET.get('x_req', '')
    print("x",x_req)
    print("y",y_req)

    print("finsish read rquest dataaa")
    print("lets read data ")
    if request.FILES["image"]:
        print("hello from if")
        im_file = request.FILES["image"]
        im_bytes = im_file.read()
        im = Image.open(io.BytesIO(im_bytes))
        filename=path_data+"saveimagecolor.jpg"
        cv2.imwrite(filename,im_file)
        

   
    # declaring global variables (are used later on)
    clicked = False
    r = g = b = x_pos = y_pos = 0

    # Reading csv file with pandas and giving names to each column
    index = ["color", "color_name", "hex", "R", "G", "B"]
    csv = pd.read_csv(path_data+'training.csv', names=index, header=None)


    # function to calculate minimum distance from all colors and get the most matching color
    def get_color_name(R, G, B):
        minimum = 10000
        for i in range(len(csv)):
            d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
            if d <= minimum:
                minimum = d
                cname = csv.loc[i, "color_name"]
        return cname


    # function to get x,y coordinates of mouse double click
    # def draw_function(event, x, y, flags, param):
   
    y=y_req
    x=x_req
    def draw_function(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            global b, g, r, x_pos, y_pos, clicked
            clicked = True
            x_pos = x
            y_pos = y
            b, g, r = img[y, x]
            b = int(b)
            g = int(g)
            r = int(r)
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_function)



    
    

    # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
    cv2.rectangle(im, (20, 20), (750, 60), (b, g, r), -1)

    # Creating text string to display( Color name and RGB values )
    text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

    # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
    cv2.putText(im, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    # For very light colours we will display text in black colour
    if r + g + b >= 600:
        cv2.putText(im, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    
    filename=path_data+"saveimagecolor.jpg"
    cv2.imwrite("filename.png",im)
    # image = Image.open(filename)
    

    
    f = open(filename, "rb")
    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] = 'image/png'
    response['Content-Length'] = os.path.getsize(filename)
    return response
        # Break the loop when user hits 'esc' key
      


    # return results.pandas().xyxy[0].to_json(orient="records")
