from django.urls import path
from .views import home
from .views import contact

# 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('', home, name='home'),
    path('contact/', contact, name='contact')
]


