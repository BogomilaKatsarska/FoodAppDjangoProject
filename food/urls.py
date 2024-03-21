from django.urls import path
from food.views import index, detail, create_item, update_item, delete_item

app_name = 'food'

urlpatterns = (
    path('', index, name='index'),
    path('<int:item_id>/', detail, name='detail'),
    path('add/', create_item, name='create_item'),
    path('update/<int:id>/', update_item, name='update_item'),
    path('delete/<int:id>/', delete_item, name='delete_item'),
)