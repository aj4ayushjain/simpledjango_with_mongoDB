## Installation

Follow these steps to set up the project locally using Docker:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/badmoham/simpledjango_with_mongoDB.git
2. **make sure you have docker and docker-compose installed on you machine**

3. **build docker image**
   ```bash
   docker compose up --build

now everythign shoudl be prepared!

postman collection: ```simpledjango_with_mongodb.postman_collection.json```

django command to make tranaaction_summary: ```
python manage.py aggregate_transactions ```

or if you want to run that command in docker: ```docker-compose exec web python manage.py aggregate_transactions ```
