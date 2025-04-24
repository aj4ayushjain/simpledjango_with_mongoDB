from rest_framework import serializers



from .models import Ingredient, Item, Order, Customer


class IngredientSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    unit = serializers.CharField(max_length=50)


    def create(self, validated_data):
        """
        Create and return a new `Ingredient` instance, given the validated data.
        """
        return Ingredient(**validated_data).save()
    
    def update(self, instance, validated_data):

        """
        Update and return an existing `Ingredient` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.unit = validated_data.get('unit', instance.unit)
        instance.save()
        return instance


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    ingredients = IngredientSerializer(many=True)

    def create(self, validated_data):
        """
        Create and return a new `Item` instance, given the validated data.
        """
        ingredients_data = validated_data.pop('ingredients')
        item = Item(**validated_data).save()
        for ingredient_data in ingredients_data:
            ingredient = Ingredient(**ingredient_data).save()
            item.ingredients.append(ingredient)
        item.save()
        return item
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Item` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        
        # Update ingredients
        ingredients_data = validated_data.pop('ingredients')
        for ingredient_data in ingredients_data:
            ingredient = Ingredient(**ingredient_data).save()
            instance.ingredients.append(ingredient)
        
        instance.save()
        return instance
    

class OrderSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    total_price = serializers.FloatField()
    customer_name = serializers.CharField(max_length=100)
    order_date = serializers.DateTimeField()
    
    
    def create(self, validated_data):
        """
        Create and return a new `Order` instance, given the validated data.
        """
        return Order(**validated_data).save()
    
class CustomerSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15, allow_blank=True, required=False)
    
    def create(self, validated_data):
        """
        Create and return a new `Customer` instance, given the validated data.
        """
        return Customer(**validated_data).save()
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Customer` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance