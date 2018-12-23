from django.db import models
import os
from .SearchTree import SearchTree
from google.cloud import datastore
from requests import get
from bs4 import BeautifulSoup

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Junaid/Documents/Aggregate/Scraper/Aggregate-f1762ced81c5.json"
client = datastore.Client('aggregate-223323')
query = client.query(kind='senators')
senatorsIteratorList = list(query.fetch())

        
class Politician:
    def __init__(self, name, state):
        self.name = name
        self.state = state
    
    def __str__(self):
        return self.state
                     
class states:
    def __init__(self):
        self.states = {}
        self.statesList = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
        for i in range(len(self.statesList)):
            self.statesList[i] = self.statesList[i].lower()
        
        for state in self.statesList:
            self.states[state.lower()] = []
    
    def isState(self, candidate):
        return (candidate.lower() in self.statesList)
    
    def get(self, state):
        return self.states[state.lower()]
    
    def add(self, politician, state):
        self.states[state.lower()].append(politician)
    
    
response = get('https://en.wikipedia.org/wiki/List_of_current_members_of_the_United_States_House_of_Representatives')
soup = BeautifulSoup(response.content, 'html.parser')
repList = soup.select('#votingmembers tbody tr')
representatives = []
for rep in repList:
    repState = rep.select_one('td a')
    repName = rep.select_one('.fn a')
    if(repState and repName):
        repName = str(repName.string)
        repState = (str(repState.string)).split(' ')[:-1]
        if(repState[-1] == 'at'):
            del repState[-1]
        repState = ' '.join(repState)
        
        representatives.append(Politician(repName, repState))
    
response = get('https://en.wikipedia.org/wiki/List_of_current_members_of_the_United_States_Senate')
soup = BeautifulSoup(response.content, 'html.parser')
senList = soup.select('#senators tbody tr')
senators = []
for sen in senList:
    senState = sen.select_one('td a')
    senName = sen.select_one('.fn a')
    if(senState and senName):
        senName = str(senName.string)
        senState = str(senState.string)
        if(senState == 'None'):
            senState = prevSenState
        senators.append(Politician(senName, senState))    
    prevSenState = senState 


namesTree = SearchTree()
repStatesDict = states()
senStatesDict = states()

for polName in senators:
    namesTree.push(polName.name)
    senStatesDict.add(polName.name, polName.state)
    
for polName in representatives:
    namesTree.push(polName.name)
    repStatesDict.add(polName.name, polName.state)

print(repStatesDict)