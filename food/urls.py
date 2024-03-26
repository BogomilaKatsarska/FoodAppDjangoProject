from django.urls import path
from food.views import  update_item, delete_item, IndexClassView, FoodDetail, ItemCreate

app_name = 'food'

urlpatterns = (
    # path('', index, name='index'),
    path('', IndexClassView.as_view(), name='index'),
    # path('<int:item_id>/', detail, name='detail'),
    path('<int:pk>/', FoodDetail.as_view(), name='detail'),
    # path('add/', create_item, name='create_item'),
    path('add/', ItemCreate.as_view(), name='create_item'),
    path('update/<int:id>/', update_item, name='update_item'),
    path('delete/<int:id>/', delete_item, name='delete_item'),
)