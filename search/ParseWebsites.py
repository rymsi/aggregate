from bs4 import BeautifulSoup
import re

def parseWikipedia(response):
    soup = BeautifulSoup(response.content, 'html.parser')
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
    soup = BeautifulSoup(response.content, 'html.parser')
    html = soup.find(class_='infobox person')
    return str(html)
    
def parsePolitifact(response):
    statementsList = []
    soup = BeautifulSoup(response.content, 'html.parser')
    statements = soup.find_all(class_='scoretable__item')[:6]
    for statement in statements:
        statementText = statement.select('.link')[0].text
        verdict = statement.select('.quote')[0].text
        imageLink = statement.select('.meter a img')[0]['src']
        source = statement.select('.statement__source a')[0].string
        statementsList.append([statementText, verdict, imageLink, source])
    return statementsList

def parsePropublica(response):
    try:
        soup =  BeautifulSoup(response.content, 'html.parser')
    
               
        committees = str(soup.find(id='member-committees'))
        
        billSubjects= soup.find(id='member-bill-subjects')
        aTagsInBillSubjects = billSubjects.findAll('a')
        for tag in aTagsInBillSubjects:
            tag.replaceWithChildren()
        billSubjects = str(billSubjects)
        
        stats = soup.find(id='robot-avatar-container') 
        
        aTagInStatsTextShowAll = stats.findAll(string='Show All Policy Areas')
        for tag in aTagInStatsTextShowAll:
            tag.replace_with('')
        
        aTagInStatsTextLearnMore = stats.findAll(string='Learn more')    
        for tag in aTagInStatsTextLearnMore:
            tag.replace_with('')
        
        aTagsInStats = stats.findAll('a')
        for tag in aTagsInStats:
            tag.replaceWithChildren()
        
        h4TagInStats = stats.findAll('h4')
        for tag in h4TagInStats:
            new_tag = soup.new_tag("h4")
            new_tag.string = tag.text
            tag.replace_with(new_tag)
        
        stats = str(stats)
        return [committees, billSubjects, stats]
    except:
        return ['', '', '']
    

