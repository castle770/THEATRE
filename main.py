from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
mongo_uri = "MONGO_URI"
client = MongoClient(mongo_uri)
db = client['sample_mflix']
collection = db['theaters']

# API route to fetch theaters data
@app.route('/theaters', methods=['GET'])
def get_theaters():
    pipeline = [{"$limit": 10}]
    results = list(collection.aggregate(pipeline))

    for doc in results:
        doc['_id'] = str(doc['_id'])

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
