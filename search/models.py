from django.db import models
import os
from .SearchTree import SearchTree
from google.cloud import datastore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Junaid/Documents/Aggregate/Scraper/Aggregate-f1762ced81c5.json"
client = datastore.Client('aggregate-223323')
query = client.query(kind='senators')
senatorsIteratorList = list(query.fetch())
namesList = []

#create a list of names to add to the search tree
for i in range(len(senatorsIteratorList)):
    namesList.append(senatorsIteratorList[i]['Name'])

class searchTree:
    def __init__(self):
        self.tree = SearchTree()
        for i in range(len(namesList)):
            self.tree.push(namesList[i], i)

