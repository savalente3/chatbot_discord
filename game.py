
from lol_api.settings import settings
import requests


API_KEY = "RGAPI-6e6f822b-1921-46ff-a908-ba4ad48012d6"

#get summoner by summoner name

URL_summoner = "https://eun1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + sofiarocks





def game():
  print("Im totally running")

  def URLLOL (summonerName):

     URL = "https://eun1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + summonerName
     print (URL)
     response = requests.get(URL)
     return response.json()
     
  URLLOL("sofiarocks")


game()







