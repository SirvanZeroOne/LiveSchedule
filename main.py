from bs4 import BeautifulSoup
import requests
import eel
import os

response = requests.get("https://www.varzesh3.com")
allInformation = BeautifulSoup(response.text, 'html.parser')
liveSchedule = allInformation.find(attrs={'id': '67'})
broadcastDays = liveSchedule.find_all(class_="date-seprator")
liveScheduleDict = {}
tempDict = {}
liveScheduleDays = []
broadcastDaysCounter = 0
gamesPerDayCounter = 1
widgetbody = liveSchedule.find(class_="widget-body")
for child in widgetbody.children:
   if type(child) == type(liveSchedule):
       for grandChild in child.children:
           if type(grandChild) == type(liveSchedule):
              if grandChild.has_attr("class"):
                  try:
                     tempDict.update({gamesPerDayCounter: {"broadcastMatchTime": grandChild.find(class_="broadcast-match-time").get_text(),
                                       "broadcastMatchHost": grandChild.find(class_="broadcast-match-host").get_text(),
                                       "broadcastMatchGuest": grandChild.find(class_="broadcast-match-guest").get_text(),
                                       "broadcastInfo": grandChild.find(class_="broadcast-info").get_text(),
                                       "broadcastTvs": grandChild.find(class_="broadcast-tvs").get_text()}})
                  except:
                     tempDict.update({gamesPerDayCounter: {"broadcastMatchTime": grandChild.find(class_="broadcast-match-time").get_text(),
                                          "broadcastMatchNoTeams": grandChild.find(class_="broadcast-match-no-teams").get_text(),
                                          "broadcastTvs": grandChild.find(class_="broadcast-tvs").get_text()}})
                  finally:
                     gamesPerDayCounter=gamesPerDayCounter+1
              else:
                  liveScheduleDays.append(grandChild.get_text())
                  liveScheduleDict[liveScheduleDays[broadcastDaysCounter-1]]=tempDict
                  broadcastDaysCounter=broadcastDaysCounter+1
                  gamesPerDayCounter=1
                  tempDict = {}
           liveScheduleDict[liveScheduleDays[broadcastDaysCounter - 1]] = tempDict

for value in liveScheduleDict.values():
    for grandValue in value.values():
         grandValue['broadcastTvs'] = grandValue['broadcastTvs'].replace("\n", '')


eel.init(os.getcwd())

@eel.expose
def GetLiveScheduleDict():
    return liveScheduleDict

eel.start("index.html")
