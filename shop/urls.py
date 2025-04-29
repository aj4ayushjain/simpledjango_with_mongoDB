from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet, ItemViewSet, CustomerViewSet, OrderViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'ingredient', IngredientViewSet, basename='ingredient')
router.register(r'item', ItemViewSet, basename='item')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'customer', CustomerViewSet, basename='customer')

# Include the router's URLs in urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]