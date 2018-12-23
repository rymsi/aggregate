# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from requests import get

def getWikipediaLink(person_name):
    response = get('https://en.wikipedia.org/w/index.php?search={}&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%22namespaces%22%3A%5B0%5D%7D&ns0=1'.format((person_name.replace('_', '+')).lower()))
    soup = BeautifulSoup(response.content, 'html.parser')
    link = 'https://en.wikipedia.org{}'.format(soup.select('.mw-search-result-heading a')[0]['href'])
    return link

def getBallotpediaLink(person_name):
    response = get('https://ballotpedia.org/wiki/index.php?search={}&title=Special:Search&profile=default&fulltext=1&searchToken=89yz47qepsxuq4zn1jgc935p2'.format((person_name.replace('_', '+')).lower()))
    soup = BeautifulSoup(response.content, 'html.parser')
    link = 'https://ballotpedia.org{}'.format(soup.select('.mw-search-result-heading a')[0]['href'])
    return link

def getPolitifactLink(person_name):
    response = get('https://www.politifact.com/search/?q={}'.format((person_name.replace('_', '+')).lower()))
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        link = 'https://www.politifact.com{}'.format(soup.select('.search-results_people a')[0]['href'])
    except:
        return None
    return link

def getPropublicaLink(person_name):
    response = get('https://www.google.com/search?q={}+propublica'.format((person_name.replace('_', '+')).lower()))
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find(class_='g').find('cite').text
    if(results.find('...') != -1):
        results = soup.find(class_='g').select('.r a')[0]['href'][7:].split('&')[0]
    print(results)
    return results

getPropublicaLink('Tim_Kaine')