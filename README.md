## Installation

Follow these steps to set up the project locally:

1. **Make Sure you have python3 & virtual env installed**

2. **Setup the Virtual Env**

   ```bash
   python3 -m venv virtual_env

3. **Activate the Virtual Env**

   ```bash
   source virtual_env/bin/activate

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt

4. **Setup the docker and then mongodb locally** 
   ```
   docker pull mongo:latest  
   docker run -d -p 27017:27017 --name=mongodb mongo:latest     

5. **now everything should be prepared!**

   ```bash
   python manage.py runserver

## CURL Requests

### **CREATE INGREDIENTS**
```bash
curl -X POST http://127.0.0.1:8000/api/ingredient/ \
-H "Content-Type: application/json" \
-d '{"name": "Rice", "quantity": 200, "unit": "grams"}'
```

### **LIST INGREDIENTS**
```bash
curl -X GET \
http://127.0.0.1:8000/api/ingredient/ \
-H "accept: */*"
```

### **UPDATE INGREDIENTS**
```bash
curl -X PATCH http://127.0.0.1:8000/api/ingredient/<ingredient_id>/ \
-H "Content-Type: application/json" \
-d '{
    "quantity": 500
}'
```

### **DELETE INGREDIENT**
```bash
curl -X DELETE http://127.0.0.1:8000/api/ingredient/<ingredient_id>/ \
-H "accept: */*"
```


### **LIST ITEMS**
```bash
curl -X GET http://127.0.0.1:8000/api/item/
```

### **CREATE ITEMS**
```bash
curl -X POST http://127.0.0.1:8000/api/item/ \
-H "Content-Type: application/json" \
-d '{
    "name": "Sourdough Bread",
    "price": 5.99,
    "ingredients": [
        { "name": "Rye Flour", "quantity": 400, "unit": "gms" },
        { "name": "Water", "quantity": 300, "unit": "ml" }
    ]
}'
```

### **UPDATE ITEMS**
```bash
curl -X PATCH http://127.0.0.1:8000/api/item/<item_id>/ \
-H "Content-Type: application/json" \
-d '{
    "price": 6.99
}'
```

### **DELETE ITEM**
```bash
curl -X DELETE http://127.0.1:8000/api/item/<item_id>/ \
-H "accept: */*"
```


