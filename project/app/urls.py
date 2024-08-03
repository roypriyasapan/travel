from django.urls import path
from .views import*

urlpatterns = [
    path('',home,name='home'),
    path('pakages/',pakages,name='pakages'),
    path('gallery/',gallery,name='gallery'),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
    path('review/',review,name='review'),
]
