from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Ingredient, Item, Order, Customer # MongoEngine model
from .serializers import IngredientSerializer, ItemSerializer, OrderSerializer, CustomerSerializer
from rest_framework import status
from .permissions import IsAdminUserOrReadOnly

class IngredientViewSet(ModelViewSet):
    """
    API view to retrieve, update and list ingredients.
    """
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

    def destroy(self, *args, **kwargs):
        ingredient = self.get_object()
        # Check if the ingredient is referenced by any items
        if Item.objects.filter(ingredients=ingredient).count() > 0:
            return Response(
                {"error": "Cannot delete ingredient as it is referenced by items."},
                status=status.HTTP_400_BAD_REQUEST
            )
        self.perform_destroy(ingredient)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemViewSet(ModelViewSet):
    """
    API view to handle CRUD operations for Items.
    """

    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
    
class OrderViewSet(ModelViewSet):
    """
    API view to handle CRUD operations for Orders.
    """

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    

class CustomerViewSet(ModelViewSet):
    """
    API view to handle CRUD operations for Customers.
    """

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
