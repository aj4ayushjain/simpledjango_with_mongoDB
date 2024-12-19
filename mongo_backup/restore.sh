#!/bin/bash

# start mongod
nohup mongod
# Restore the database from the .agz file
echo "Restoring MongoDB from transactions.agz..."
mongorestore --gzip --archive=/data/transactions.agz

