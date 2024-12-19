#!/bin/bash

# Wait for MongoDB to start
until nc -z mongo 27017; do
  echo "Waiting for MongoDB to start..."
  sleep 2
done

# Restore the database from the .agz file
echo "Restoring MongoDB from transactions.agz..."
mongorestore --gzip --archive=/data/transactions.agz

# Keep the container running
tail -f /dev/null

