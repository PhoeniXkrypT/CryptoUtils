
from django.conf.urls import url, include

import views

urlpatterns = [
    url(r'^$', views.mainview),
    url(r'^rsa1/', views.RSA1.as_view()),
]
