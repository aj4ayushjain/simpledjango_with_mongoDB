
# Create your models here.
import mongoengine

class Ingredient(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    quantity = mongoengine.IntField(required=True)
    unit = mongoengine.StringField(required=True)

    def __str__(self):
        return self.name
    

class Item(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    price = mongoengine.FloatField(required=True)
    ingredients = mongoengine.ListField(mongoengine.ReferenceField(Ingredient, reverse_delete_rule=mongoengine.DENY))
    def __str__(self):
        return self.name
    


class Customer(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True)
    phone = mongoengine.StringField()

    def __str__(self):
        return self.name

class Order(mongoengine.Document):
    quantity = mongoengine.IntField(required=True)
    total_price = mongoengine.FloatField(required=True)
    customer = mongoengine.ReferenceField(Customer)
    order_date = mongoengine.DateTimeField()

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}" 


