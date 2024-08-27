from django.urls import path
from .views import ProductDetelisView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name = 'product-list-view'),
    path('<int:pk>/', ProductDetelisView.as_view(), name='product-detail'),

]
