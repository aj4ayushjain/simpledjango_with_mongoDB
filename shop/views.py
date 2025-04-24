from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ingredient, Item, Order, Customer # MongoEngine model
from .serializers import IngredientSerializer, ItemSerializer, OrderSerializer, CustomerSerializer
from rest_framework import status
from .permissions import IsAdminUserOrReadOnly

class IngredientView(APIView):
    """
    API view to retrieve, update and list ingredients.
    """
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request, *args, **kwargs):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, *args, **kwargs):
        ingredient_id = kwargs.get('pk')
        try:
            ingredient = Ingredient.objects.get(id=ingredient_id)
        except Ingredient.DoesNotExist:
            return Response({"error": "Ingredient not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = IngredientSerializer(ingredient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def detail(self, request, *args, **kwargs):
        ingredient_id = kwargs.get('pk')
        try:
            ingredient = Ingredient.objects.get(id=ingredient_id)
        except Ingredient.DoesNotExist:
            return Response({"error": "Ingredient not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

class ItemView(APIView):
    """
    API view to handle CRUD operations for Items.
    """

    def get(self, request, *args, **kwargs):
        # Retrieve all items
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Create a new item
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        # Update an existing item
        item_id = kwargs.get('pk')
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        # Delete an item
        item_id = kwargs.get('pk')
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        

class OrderView(APIView):
    """
    API view to handle CRUD operations for Orders.
    """

    def get(self, request, *args, **kwargs):
        # Retrieve all orders
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Create a new order
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomerView(APIView):
    """
    API view to handle CRUD operations for Customers.
    """

    def get(self, request, *args, **kwargs):
        # Retrieve all customers
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Create a new customer
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)