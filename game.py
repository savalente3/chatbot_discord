
from lol_api.settings import settings
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt


""" Info for APIs KEYS"""

#REgion endpoint
#EUNE	// EUN1	// eun1.api.riotgames.com
#API for private project(I've applied, but doesnt work)
API_KEY = "RGAPI-51bc5f2d-b295-41aa-8c5a-4a7325b195e5"
#API for developers has durantion of 24h
personalAPI_KEY = "RGAPI-65d69b8f-305e-492d-8dea-da690394c08d"


"""URL APIs LOL"""

#*get summoner by summoner name
#summoner_Name = "sofiarocks" #(creat an input)
#URL_summonerbyname = "https://eun1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summoner_Name + "?api_key=" + personalAPI_KEY


#get summoner by account id (returned value of summoner by summoner name)
#account_ID = "2070081094595296"
#URL_summonerbyID = "https://eun1.api.riotgames.com/lol/summoner/v3/summoners/by-account/" + account_ID + "?api_key=" + personalAPI_KEY

#*Get all champion mastery entries sorted by number of champion points descending
#summoner_ID = "76605785" 
#URL_mastery1 = "https://eun1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/"+ summoner_ID + "?api_key=" + personalAPI_KEY



#*Get a player's total champion mastery score, which is the sum of individual champion mastery levels.
#URL_mastery2 = "https://eun1.api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/"+ summoner_ID + "?api_key=" + personalAPI_KEY


#Get match by match ID
#match_ID = 
#URL_match = "https://eun1.api.riotgames.com/lol/match/v3/matches/"+ match_ID + "?api_key=" + personalAPI_KEY


#*Get matchlist for games played on given account ID and platform ID and filtered using given filter parameters, if any
#URL_matchByAccountID = "https://eun1.api.riotgames.com/lol/match/v3/matchlists/by-account/"+ account_ID + "?api_key=" + personalAPI_KEY


#Get match timeline by match ID.
#URL_matchTimeline = "https://eun1.api.riotgames.com/lol/match/v3/timelines/by-match/" + match_ID + "?api_key=" + personalAPI_KEY

#Get match IDs by tournament code
#tornementCode = 
#URL_matchIDByTonermentCode = "https://eun1.api.riotgames.com/lol/match/v3/matches/by-tournament-code/" + tornementCode + "?api_key=" + personalAPI_KEY

#Get League of Legends status for the given shard
#URL_status = "https://eun1.api.riotgames.com/lol/status/v3/shard-data" + "?api_key=" + personalAPI_KEY

#Get list of featured games
#"https://eun1.api.riotgames.com//lol/spectator/v3/featured-games" + "?api_key=" + personalAPI_KEY 

list_of_regions = ["br1","eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "tr1", "ru"]

print ("Tell me your Summoner Name, please")
summoner_Name = input("")

def getRegion():
  print ("Select region")

  br = "br1"	
  eune = "eun1"	
  euw	= "euw1"	
  jp	= "jp1"	
  kr	= "kr"	
  lan = "la1"	
  las = "la2"	
  na = "na1" 
  oce = "oc1"	
  tr	= "tr1"	
  ru	= "ru"	

  print(br.center (40))
  print(eune.center (40))
  print(euw.center (40))
  print(jp.center (40))
  print(kr.center (40))
  print(lan.center (40))
  print(las.center (40))
  print(na.center (40))
  print(oce.center (40))
  print(tr.center (40))
  print(ru.center (40))

  region = input("")

  return region

region = getRegion()


def summonerbyname():
 #get summoner by summoner name

  if region in list_of_regions:  
    URL_summonerbyname = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summoner_Name + "?api_key=" + personalAPI_KEY
    
    #http://docs.python-requests.org/en/master/ (exemple on how to use requests lib)
    response = requests.get(URL_summonerbyname)
    data = response.json()
  

    #print the info and store summoner ID and account ID
    summonerbyname.summoner_ID = (data["id"])
    summonerbyname.account_ID = (data["accountId"])
    print ("Summoner Level: ", data["summonerLevel"])
    print ("summoner ID: ", data["id"])
    print ("Account ID: ", data["accountId"])
   

summonerbyname()
summoner_ID = summonerbyname.summoner_ID
account_ID = summonerbyname.account_ID


def mastery1 (summoner_ID):
 
   #Get all champion mastery entries sorted by number of champion points descending 
   URL_mastery1 = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/"+ summoner_ID + "?api_key=" + personalAPI_KEY
   
   #get the champion name from champion id 
   URL_championName = "http://ddragon.leagueoflegends.com/cdn/8.22.1/data/en_US/champion.json" 

   
   
   
   #pandas library: organizes info from API into table 
   #https://pandas.pydata.org/pandas-docs/stable/install.html (used to organanize info into tables)
   data = pd.read_json(URL_mastery1)
   data1 = pd.read_json(URL_championName)
   champ = data1 ["data"]
   #champIM = pd.read_json(URL_championImage)

   #formating List from json 
   #https://stackoverflow.com/questions/30522724/take-multiple-lists-into-dataframe
   mastery = data[0:15]


   championLevel = mastery.championLevel
   championPoints = mastery.championPoints
   tokensEarned = mastery.tokensEarned
   championId = mastery.championId
   championPointsUntilNextLevel = mastery.championPointsUntilNextLevel
   
   championImage = []
   championName = []
   
   for id in championId:
     for i in champ:
       if str(id) == i["key"]:
         championName.append(i["name"])

   
   for i in champ:
     for id in championId:
       if i["key"] == str(id):
        #get the image of each champion by champion name 
        championImage.append("http://ddragon.leagueoflegends.com/cdn/8.22.1/img/champion/" + i["image"]["full"])
   
   
   table = pd.DataFrame({"Champion":championImage,"champion Name":championName, "champion Level": championLevel,"champion Points": championPoints,"tokens Earned": tokensEarned,"championPointsUntilNextLevel": championPointsUntilNextLevel})
   

   print(table)

#######################################################################################
 

mastery1 (str(summoner_ID))


def mastery2 (summoner_ID):
  #Get a player's total champion mastery score, which is the sum of individual champion mastery levels.
  
  URL_mastery2 = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/"+ summoner_ID + "?api_key=" + personalAPI_KEY
  response = requests.get(URL_mastery2)
  data = response.json()
  
  print ("Your total champion mastery score: ", data)

 

mastery2 (str(summoner_ID))


def matchList(account_ID):
 #Get matchlist for games played on given account ID and platform ID and filtered using given filter parameters, if any
   
 URL_match = "https://" + region + ".api.riotgames.com/lol/match/v3/matchlists/by-account/" + account_ID + "?api_key=" + personalAPI_KEY
 data = pd.read_json(URL_match)
 data1 = data[0:1]
 matches = data[0:16]["matches"]

 lane = []
 champion = []
 season = []
 role = []

 i = 1
 while i < len(matches):

   lane.append(matches[i]["lane"])
   champion.append(matches[i]["champion"])
   season.append(matches[i]["season"])
   role.append(matches[i]["role"])
   i = i + 1

 #get the champion name from champion id 
 URL_championName = "http://ddragon.leagueoflegends.com/cdn/8.22.1/data/en_US/champion.json" 
 data2 = pd.read_json(URL_championName)
 champ = data2 ["data"]

 championImage = []
 championName = []

 for id in champion:
   for i in champ:
     if str(id) == i["key"]:
       championName.append(i["name"])


 for i in champ:
     for id in champion:
       if i["key"] == str(id):
         #get the image of each champion by champion name 
         championImage.append("http://ddragon.leagueoflegends.com/cdn/8.22.1/img/champion/" + i["image"]["full"])
   

 table = pd.DataFrame({"Champion":championImage, "champion Name": championName,"lane": lane, "season":season, "role": role})
 print (table)

 
 #Total of games
 print("Total Games")
 print(data1.totalGames)
 
      
matchList(str(account_ID))




