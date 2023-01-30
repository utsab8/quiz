from django.urls import re_path as url
import quizapp.views as quiz_views


urlpatterns = [
    url("", quiz_views.qpage),
]