from pymongo import MongoClient

import json
import pprint

# Json Lines
# http://jsonlines.org

if __name__ == "__main__":
	client = MongoClient("mongodb://localhost:27017")
	db = client.local
	collection = db.test_collection
	
	# Just one insert and read
	post = json.loads('{"FirstName": "Bruce", "LastName": "Wayne", "Email": "bwayne@Wayneenterprises.com"}')
	post_id = collection.insert_one(post).inserted_id
	print(post_id)
	pprint.pprint(collection.find_one({"_id": post_id}))

    # Load file
	with open('data.jsonl') as f:
		for line in f:
			item = json.loads(line)
			collection.insert_one(item).inserted_id
			print("inserted " + str(item))

	# Search
	result = collection.find({"LastName": "Wayne", "FirstName": {'$regex': 'B*1.'}})
	for post in result:
		pprint.pprint(post)

	"""
	Result:
	{'Email': 'bwayne@Wayneenterprises.com',
	'FirstName': 'Bruce14',
	'LastName': 'Wayne',
	'_id': ObjectId('5ab323c2f9c696b7b7b29680')}
	{'Email': 'bwayne@Wayneenterprises.com',
	'FirstName': 'Bruce15',
	'LastName': 'Wayne',
	'_id': ObjectId('5ab323c2f9c696b7b7b29681')}
	{'Email': 'bwayne@Wayneenterprises.com',
	'FirstName': 'Bruce16',
	'LastName': 'Wayne',
	'_id': ObjectId('5ab323c2f9c696b7b7b29682')}		
	"""

	db.close