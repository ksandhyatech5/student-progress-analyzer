from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://127.0.0.1:27017")

# FORCE correct DB and collection
db = client["studentDB"]        # 👈 MUST match Compass
collection = db["marks"]        # 👈 MUST match Compass

print("✅ Connected to:", db.name, "->", collection.name)
