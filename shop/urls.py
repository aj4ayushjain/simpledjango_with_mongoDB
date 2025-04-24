from django.urls import path, include
from .views import IngredientView, ItemView, CustomerView


urlpatterns = [
    path('ingredient/', IngredientView.as_view()),
    path('ingredient/<str:pk>/', IngredientView.as_view()),  # For patching

    path('item/', ItemView.as_view()),
    path('customer/', CustomerView.as_view()),
]