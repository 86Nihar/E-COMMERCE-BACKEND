from django.urls import path
from .views import (
    RegisterView, ProductListCreateView,
    ProductRetrieveUpdateDestroyView, OrderListCreateView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
]
