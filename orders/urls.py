from django.urls import path
from . import views

urlpatterns = [
    path('<int:order_id>/recommend/', views.recommend_order_box, name='recommend_order_box'),
    path('place/', views.place_order, name='place_order'),
]