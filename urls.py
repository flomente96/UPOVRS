
R&Xg  �               @   sl   d  Z  d d l m Z m Z d d l m Z e d e d � � e d e d � � e d e j j � g Z d	 S)
ay  upovrs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
�    )�include�url)�adminz^main/z	main.urlsz^home/z	home.urlsz^admin/N)	�__doc__�django.conf.urlsr   r   Zdjango.contribr   �site�urls�urlpatterns� r
   r
   �2C:\Users\User\Desktop\UPOVRS\UPOVRS\upovrs\urls.py�<module>   s
   