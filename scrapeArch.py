from bs4 import BeautifulSoup
import urllib2
import json



# scraping whiskycast.com
linkList = []
nameList = []


print i
url = "http://archrecord.construction.com/projects/portfolio/ProjectArchive.aspx"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())


urlM = 'http://archrecord.construction.com'
for link in soup.findAll("a", {"class":"titleLink"}):
    wLink = link.get('href')
    linkList.append(urlM+wLink)
    wName = wLink.split('/')[-1].replace('-',' ')[5:-4]
    nameList.append(wName)
    


wName = nameList
wLink = linkList

portfolioData = {}

for i in linkList:
    page = urllib2.urlopen(i)
    soup = BeautifulSoup(page.read())


    prInfo = soup.find("div",{"id":"projectInfo"})

    MetaData = {}
    MetaData.update({'Author':prBody.find("p",{"class":"authorCredit"}).get_text()})
    MetaData.update({'Name': prInfo.find("h1").get_text()})
    MetaData.update({'Architect':prInfo.find("h2").get_text()})
    MetaData.update({'Location': prInfo.find("span",{"id":"location"}).get_text()})

    prBody = soup.find("div",{"id":"articleBodyText"})
    Body = ''
    for p in prBody.findAll("p")[1:]:
        Body = Body + p.get_text()+'\n'

    
    Body = ''
    for p in prBody.findAll("p")[1:]:
        Body = Body + p.get_text()
        more = p.find("span",{"class":"mainboldBlue"})
        if more != None and more != 'Architect:':
            try:
                MetaData.update({more.get_text()[:-1]:p.get_text().split(':')[-1]})
            except:
                pass
