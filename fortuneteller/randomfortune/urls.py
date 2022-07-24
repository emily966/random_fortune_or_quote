from django.urls import include, path
# from randomfortune import views
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('fortune/', views.fortune, name = 'fortune'),
    path('quote', views.quote, name="quote")
]