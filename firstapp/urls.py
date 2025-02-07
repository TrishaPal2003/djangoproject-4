from django.urls import path,include
from .views import index1


urlpatterns = [
    
    path('',index1),
]
