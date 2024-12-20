#!/bin/bash

# start mongod
nohup mongod --bind_ip_all
# Restore the database from the .agz file
echo "Restoring MongoDB from transactions.agz..."
mongorestore --gzip --archive=/data/transactions.agz

