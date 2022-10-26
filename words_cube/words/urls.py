"""trial URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from words_cube.words import views
from django.urls import path
urlpatterns = [
    path('predict_model_speech', views.predicting_model),
    path('predict_model_speech_words', views.predicting_words_speech),
    path('predict_model_color', views.predicting_color),
    path('predict_model_numers', views.predicting_numbers),
    path('predict_Arabic_fruit', views.predicting_fruits),
    path('predict_Arabic_Furn_transport', views.predicting_Furn_transport),
]
