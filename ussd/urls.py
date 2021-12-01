from  django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *
urlpatterns = [
    path('', views.welcome, name='welcome') ,
    path('ussd/', views.ussdApp, name='ussd')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
