from bs4 import BeautifulSoup
import urllib2
import json


import mechanize
import re

br = mechanize.Browser()
br.addheaders = [('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0')]
response = br.open("http://archrecord.construction.com/projects/portfolio/ProjectArchive.aspx")


linkList = []
nameList = []


soup = BeautifulSoup(response)


urlM = 'http://archrecord.construction.com'
for link in soup.findAll("a", {"class":"titleLink"}):
    wLink = link.get('href')
    linkList.append(urlM+wLink)
    wName = wLink.split('/')[-1].replace('-',' ')[5:-4]
    nameList.append(wName)
    

names = []
portfolioData = {}

for i in linkList:
    
    response = br.open(i)

    soup = BeautifulSoup(response)


    prInfo = soup.find("div",{"id":"projectInfo"})

    MetaData = {}
    MetaData.update({'Name': prInfo.find("h1").get_text()})
    names.append(prInfo.find("h1").get_text())
    portfolioData[names[-1]] = {}
    
    MetaData.update({'Architect':prInfo.find("h2").get_text()})
    MetaData.update({'Location': prInfo.find("span",{"id":"location"}).get_text()})

    prBody = soup.find("div",{"id":"articleBodyText"})
    Body = ''
    for p in prBody.findAll("p")[1:]:
        Body = Body + p.get_text()+'\n'

    MetaData.update({'Author':prBody.find("p",{"class":"authorCredit"}).get_text()})

    Body = ''
    for p in prBody.findAll("p")[1:]:
        Body = Body + p.get_text()
        more = p.find("span",{"class":"mainboldBlue"})
        if more != None and more != 'Architect:':
            try:
                MetaData.update({more.get_text()[:-1]:p.get_text().split(':')[-1]})
            except:
                pass
    portfolioData[names[-1]]['MetaData'] = MetaData
    portfolioData[names[-1]]['BodyText'] = Body

    
