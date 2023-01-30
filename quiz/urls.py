"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import re_path as url, include
from django.contrib import admin
from quiz import views as index_views
from rest_framework.urlpatterns import format_suffix_patterns
from quizapi import views

urlpatterns = [
	url(r'^$', index_views.index),
	url(r'^login/$', index_views.login),
	url(r'^questions/', include('quizapp.urls')),
	url(r'^quizapi/', views.QuizApiList.as_view()),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)