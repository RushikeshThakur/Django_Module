"""djmodel URL Configuration

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
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog.views import (form_details_view, blog_model_form, blog_model_form_search, my_form_data, 
	                    dynamic_id, delete_data, list_all_data, list_all_data_url, post_form)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^get/', form_details_view, name="data"),
    url(r'^form/', blog_model_form, name="form"),
    url(r'^search/', blog_model_form_search, name="search"),
    url(r'^data/', list_all_data, name="all_data"),
    url(r'^alldata/', list_all_data_url, name="list_all_data"),
    url(r'^myform/', my_form_data, name="my_form"),
    url(r'^product/(?P<my_id>\d+)/$', dynamic_id, name="id"),
    url(r'^getform/', post_form, name="post_form"),
]

