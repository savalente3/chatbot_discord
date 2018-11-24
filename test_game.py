import pytest
import game

summoner_Name = "wrborges"
list_of_regions = ["br1","eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "tr1", "ru"]

def test_summonerbyname():
    assert game.summonerbyname() == "wrborges"



