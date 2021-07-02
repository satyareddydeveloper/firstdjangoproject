from django.urls import path
from webpages.views import homepage
from webpages.views import aboutpage




urlpatterns = [
    path('',homepage,name="home"),
    path('about', aboutpage, name="about")
    

]