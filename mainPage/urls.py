from django.urls import path,include
from .views import home, about

app_name = 'mainPage'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),

]
