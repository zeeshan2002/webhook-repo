from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

try:
    print(client.server_info())
    print("✅ Connected to MongoDB")
except Exception as e:
    print("❌ Connection failed")
    print(e)
db = client["webhookdb"]
# db = client.get_default_database()
events = db.events
print("db: ", db)
print("events: ", events)

def insert_event(event):
    return events.insert_one(event)

def get_latest_events(limit=20):
    return list(events.find()) 

# .sort('timestamp', -1).limit(limit)