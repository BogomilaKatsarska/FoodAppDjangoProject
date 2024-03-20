from django.urls import path
from food.views import index, item, detail

app_name = 'food'

urlpatterns = (
    path('', index, name='index'),
    path('<int:item_id>/', detail, name='detail'),
    path('item/', item, name='item'),
)