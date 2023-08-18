from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS

import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS

password = "admin123"  # replace this with the actual password
client = MongoClient(f"mongodb+srv://admin123:{password}@iiith-silverjubliee.a497uaa.mongodb.net/?retryWrites=true&w=majority")
db = client["iiith_events"]
collection = db["schedule"]

db1 = client["event_calendar_db"]
collection1 = db1["events"]


@app.route('/api/events', methods=['GET'])
def get_events():
    events = list(collection.find())
    for event in events:
        event["_id"] = str(event["_id"])
        
        # Check if the "date" key exists in the document
        if "date" in event:
            event["date"] = event["date"].strftime('%Y-%m-%d')
        else:
            event["date"] = "Unknown"  # or any other default value you'd like
    
    return jsonify(events)

@app.route('/api/events1', methods=['GET'])
def get_event1():
    events1 = list(collection1.find({}, {"_id": 0}))  # excluding _id from the result
    return jsonify(events1)

if __name__ == '__main__':
    app.run(port=8080)

