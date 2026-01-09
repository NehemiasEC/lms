from django.urls import path
from .views import HomePageView
from .views import index,test
urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('', HomePageView.as_view(), name='homepageview'),
    path('test',test, name='test'),
]