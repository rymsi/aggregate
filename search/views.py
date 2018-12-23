from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
from google.cloud import datastore
from requests import get
from .models import namesTree, repStatesDict, senStatesDict
from .ParseWebsites import parseWikipedia, parseBallotpedia, parsePolitifact, parsePropublica
from .getLinks import getWikipediaLink, getBallotpediaLink, getPolitifactLink, getPropublicaLink
import os 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Junaid/Documents/Aggregate/Scraper/Aggregate-f1762ced81c5.json"
client = datastore.Client('aggregate-223323')

# Create your views here.
def search(request):
    return render(request, 'search/index.html')

def results(request, search_query):
    searchQueryList = search_query.split('+')
    for word in searchQueryList:
        if ((word.lower()) == 'rep'): 
            if(not searchQueryList.index(word)):
                state = searchQueryList[-1].lower()
                if(not repStatesDict.isState(state)):
                    state = searchQueryList[-2] + ' ' + searchQueryList[-1]                        
            else:
                state = searchQueryList[0].lower()

                if(not repStatesDict.isState(state)):
                    state = searchQueryList[0] + ' ' + searchQueryList[1]
                    
                    
            representatives = []
            for rep in repStatesDict.get(state):
                representatives.append([rep, rep.replace(' ', '_')])
            return render(
                            request, 
                            'search/results.html', 
                            {
                                'results':representatives,
                            })
                                            
            
        elif ((word.lower()) == 'sen'):
            if(not searchQueryList.index(word)):
                state = searchQueryList[-1].lower()
                if(not senStatesDict.isState(state)):
                    state = searchQueryList[-2] + ' ' + searchQueryList[-1]                        
            else:
                state = searchQueryList[0].lower()

                if(not senStatesDict.isState(state)):
                    state = searchQueryList[0] + ' ' + searchQueryList[1]
                                    
                    
            senators = []
            for sen in senStatesDict.get(state):
                senators.append([sen, sen.replace(' ', '_')])
            return render(
                            request, 
                            'search/results.html', 
                            {
                                'results':senators,
                            })

#   match name
    name = namesTree.search(search_query.replace('+', ' ')) 
    return HttpResponseRedirect('/person/{}'.format(name.replace(' ', '_')))
                    
    
def person(request, person_name):

    person = {
                'Wikipedia':getWikipediaLink(person_name),
                'Ballotpedia':getBallotpediaLink(person_name),
                'Politifact':getPolitifactLink(person_name),
                'Propublica':getPropublicaLink(person_name),
            }
    if(person['Wikipedia']):
        wikipedia = parseWikipedia(get(person['Wikipedia']))
    else:
        wikipedia = ''
    
    ballotpedia = parseBallotpedia(get(person['Ballotpedia']))
    
    if(person['Politifact']):    
        politifact = parsePolitifact(get(person['Politifact']))
    else:
        politifact = ''
    if(person['Propublica']):
        propublica = parsePropublica(get(person['Propublica']))
    else:
        propublica = ''
    return render(request, 
                  'search/person.html', 
                  {
                          'title': person_name.replace('_', ' '),
                          'wikipedia':wikipedia,
                          'ballotpedia':ballotpedia,
                          'politifact':politifact,
                          'propublica':propublica
                  })
        
