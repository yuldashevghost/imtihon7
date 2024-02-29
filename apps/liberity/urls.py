from django.urls import path
from .views import home_page, explore, details, create, author

app_name = 'liberity'
urlpatterns = [
    path('', home_page, name='home'),
    path('explore/', explore, name='explore'),
    path('details/', details, name='details'),
    path('create/', create, name='create'),
    path('author/', author, name='author'),
]