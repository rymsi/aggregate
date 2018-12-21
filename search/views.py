from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from google.cloud import datastore
from requests import get
from .models import searchTree
from .ParseWebsites import parseWikipedia, parseBallotpedia, parsePolitifact
import os 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Junaid/Documents/Aggregate/Scraper/Aggregate-f1762ced81c5.json"
client = datastore.Client('aggregate-223323')

# Create your views here.
def search(request):
    return render(request, 'search/index.html')

def results(request, search_query):
    search_query = search_query.replace('+', ' ')
    tree = searchTree()
    query = client.query(kind='senators')
    
#    add search functionality
    index = tree.tree.search(search_query)    
    query.add_filter("Index", "=", int(index))
    resultsPrelim = list(query.fetch())
    results = []
    
    for iter in range(len(resultsPrelim)):
        results.append([resultsPrelim[iter], resultsPrelim[iter]['Name'].replace(' ', '_')])   
    
    return render(
            request, 
            'search/results.html', 
            {
                'results':results,
            })
def person(request, person_name):
    query = client.query(kind='senators')
    query.add_filter('Name', '=', person_name.replace('_', ' '))
    person = list(query.fetch())[0]
    
    wikipedia = '' #parseWikipedia(get(person['Wikipedia']))
    ballotpedia = '' #parseBallotpedia(get(person['Ballotpedia']))
    politifact = parsePolitifact(get(person['Politifact']))
#    propublica = get(person['Propublica'])
    
    
    
    return render(request, 
                  'search/person.html', 
                  {
                          'title': person_name.replace('_', ' '),
                          'wikipedia':wikipedia,
                          'ballotpedia':ballotpedia,
                          'politifact':politifact,
                  }
                  )