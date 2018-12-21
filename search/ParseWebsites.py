from bs4 import BeautifulSoup
import re

def parseWikipedia(response):
    soup = soup = BeautifulSoup(response.content, 'html.parser')
    raw = soup.select('.mw-parser-output > *')
    responseTextList = []
    for i in range(len(raw)):
        if(raw[i].name == 'p'):
            responseTextList.append(raw[i].text.strip())
        if(((raw[i].name == 'div') and (raw[i]['class'][0] == 'toc')) or (i > 8)):
            break
    for i in range(len(responseTextList)):    
        responseTextList[i] = re.sub('\[\d*\]', '', responseTextList[i].lstrip())
        responseTextList[i] = re.sub('\[\D*\]', '', responseTextList[i])

    return responseTextList

def parseBallotpedia(response):
    soup = soup = BeautifulSoup(response.content, 'html.parser')
    html = soup.find(class_='infobox person')
    
    return str(html)
    
def parsePolitifact(response):
    statementsList = []
    soup = soup = BeautifulSoup(response.content, 'html.parser')
    statements = soup.find_all(class_='scoretable__item')
    for statement in statements:
        statementText = statement.select('.link')[0].text
        print('\n\n\n\n\n\n\n', statementText, "<<statement Text\n\n\n\n\n")
        verdict = statement.select('.quote')[0].text
        print('\n\n\n\n', verdict, "<<verdict\n\n\n\n\n\n\n")
        imageLink = statement.select('.meter a img')[0]['src']
        statementsList.append([statementText, verdict, imageLink])
    return statementsList

