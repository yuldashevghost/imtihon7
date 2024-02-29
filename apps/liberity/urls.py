from django.urls import path
from .views import item_list, explore, CreateItemView, item_detail, author

app_name = 'liberity'
urlpatterns = [
    path('', item_list, name='home'),
    path('explore/', explore, name='explore'),
    path('details/<int:pk>/', item_detail, name='details'),
    path('create/', CreateItemView.as_view(), name='create'),
    path('author/', author, name='author'),
]