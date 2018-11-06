#First we need to import requests. Installing this is a bit tricky. I included a step by step process on how to get requests in readme.txt which is included in the file along with this program.
import requests


def requestSummonerData(region, summonerName, APIKey):

    #Here is how I make my URL.  There are many ways to create these.
    
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    print (URL)
    #requests.get is a function given to us my our import "requests". It basically goes to the URL we made and gives us back a JSON.
    #response = requests.get(URL)
    #Here I return the JSON we just got.
    #return response.json()

requestSummonerData("pt","sofiarocks", "456780")