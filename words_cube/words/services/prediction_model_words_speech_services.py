
import os
import json
import numpy as np
import pickle
import pandas as pd
from django.http import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import FileResponse
import io
from django.http import HttpResponse
from wsgiref.util import FileWrapper



services_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.dirname(services_dir))
new_root=os.path.abspath(os.path.dirname(project_root))
print('new_root',new_root)
path_data = os.path.join(project_root, 'resources\\data\\all_data_words\\')




def predict_speech_words(predict_model_request):

    data = predict_model_request
    data=data.data
    data=data["data"]
    print("finsish read rquest dataaa")
 
    print(data)

    data_df=pd.read_csv(path_data+"all_data_words.csv",names=["word","path"])
    
    fname=path_data+data+".mp3"
 
    
    f = open(fname, "rb")
    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] = 'audio/mp3'
    response['Content-Length'] = os.path.getsize(fname)
    return response
    
    



