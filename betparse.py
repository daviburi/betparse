from urllib.request import urlopen
import sys
from bs4 import BeautifulSoup
import re

#Getting page source
def getPageSource(url):
	page = urlopen(url)
	html = page.read()
	return BeautifulSoup(html)

def getTeamNamesWilliamhill(pageSource):
	pageTitle = pageSource.html.head.title.string
	divider1 = pageTitle.find(' v ')
	divider2 = pageTitle.find(' betting')
	team1 = pageTitle[:divider1]
	team2 = pageTitle[divider1+3:divider2]
	return team1, team2

def getTeamCoefficients(pageSource):
	marketStart = pageSource.find('<span>Match Betting</span>')
	print(pageSource[:marketStart])


soup = getPageSource("http://sports.williamhill.com/bet/en-gb/betting/e/4416890/Chelsea%2dv%2dEverton.html").prettify()
#soup = unicode(soup, "utf-8")
#marketStart = soup.find('<span>Match Betting</span>')
print(soup)

#print(soup)
#getTeamCoefficients(soup)
#team1 = getTeamNamesWilliamhill(soup)[0]
#team2 = getTeamNamesWilliamhill(soup)[1]

#print(team1)
#print(team2)