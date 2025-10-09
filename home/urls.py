from django.urls import path
#from .views import HomePageView
from .views import index
urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('index', index, name='index'),
]