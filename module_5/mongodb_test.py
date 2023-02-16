# Import the MongoClient from the pymongo package
from pymongo import MongoClient

# Set the MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.n37za4m.mongodb.net/pytech"

# Create a MongoClient instance using the connection string
client = MongoClient(url)

# Access the "pytech" database using the client
db = client.pytech

# Print the names of all the collections in the "pytech" database
print(db.list_collection_names())
