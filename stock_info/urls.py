from django.contrib import admin
from django.urls import path,re_path
from stock_info import views

''' All URLS used for webpages are customized or created here. '''
urlpatterns = [
    re_path(r'^$', views.index,name='home'),
    re_path(r'^nse$',views.nse,name="nse_indices"),
    re_path(r'^stock/(.*)$',views.stock,name='stock'),
    re_path(r'^indices/(.*)$',views.indices,name='index'),
    re_path(r'^news$',views.news,name='news')
]