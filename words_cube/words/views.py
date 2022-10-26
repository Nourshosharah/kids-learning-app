from rest_framework.decorators import api_view

from words_cube.words.controllers.prediction_model_controller import predict_model_spech_con,predict_model_colo_con,predict_model_numb_con,predict_model_Furn_transport_con,predict_model_fruit_con,predicting_words_speech_con


@api_view(['GET','POST'])
def predicting_model(request):
    return predict_model_spech_con(request)


@api_view(['GET','POST'])
def predicting_words_speech(request):
    return predicting_words_speech_con(request)

@api_view(['GET','POST'])
def predicting_color(request):
    return predict_model_colo_con(request)


@api_view(['GET','POST'])
def predicting_numbers(request):
    return predict_model_numb_con(request)


@api_view(['GET','POST'])
def predicting_fruits(request):
    return predict_model_fruit_con(request)

@api_view(['GET','POST'])
def predicting_Furn_transport(request):
    return predict_model_Furn_transport_con(request)


