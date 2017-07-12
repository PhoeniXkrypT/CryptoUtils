
from django.conf.urls import url, include

import views

urlpatterns = [
    url(r'^$', views.mainview),
    url(r'^rsa1/', views.RSA1.as_view()),
    url(r'^rsa2/', views.RSA2.as_view()),
]
