from rest_framework.response import Response

# from words_cube.words.dto.requests.predict_model_request import PredictModelRequest
from words_cube.words.services.prediction_model_speech_services import predict
from words_cube.words.services.prediction_model_words_speech_services import predict_speech_words
from words_cube.words.services.prediction_model_color_services import predict_color
from words_cube.words.services.prediction_model_number_services import predict_number
from words_cube.words.services.prediction_model_fruits_services import predict_fruit
from words_cube.words.services.prediction_model_furn_trans_services import predict_furn_tran
# from words_cube.words.dto.requests.predict_model_request import GettRequest


def predict_model_spech_con(request):
    # predict_request = PredictModelRequest(request.data)
    predict_response = predict(request)
    return predict_response


def predicting_words_speech_con(request):
    # predict_request = PredictModelRequest(request.data)
    predict_response = predict_speech_words(request)
    return predict_response




def predict_model_colo_con(request):
    # data = request.data
    # products_request = GettRequest(data)
    products_response = predict_color(request)
    return predict_response



def predict_model_numb_con(request):
    # predict_request = PredictModelRequest(request.data)
    predict_response = predict_number(request)
    return Response(predict_response)


def predict_model_fruit_con(request):
    # predict_request = PredictModelRequest(request.data)
    predict_response = predict_fruit(request)
    return predict_response


def predict_model_Furn_transport_con(request):
    # predict_request = PredictModelRequest(request.data)
    predict_response = predict_furn_tran(request)
    return predict_response