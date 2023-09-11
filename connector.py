import argparse
import pprint
import json
from pymongo.mongo_client import MongoClient

class Connetion:
    def __init__(self):
        dict_json = json.load(open('config.json'))
        self.uri = dict_json['uri']
        self.client = MongoClient(self.uri)
        self.database = self.client['todoPy']
        self.collection = self.database['todos'] 

    def test(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def post_todo(self, task: str):
        if not task:
            print("error")
            return 

        post = {
            "task": task,
            "status": "not done"
        }

        self.collection.insert_one(post)

    def get_todos(self):
        for doc in self.collection.find({"status": "not done"}):
            pprint.pprint(doc['task'])


    def delete_todo(self, task: str):
        self.collection.delete_one({"task": task})












