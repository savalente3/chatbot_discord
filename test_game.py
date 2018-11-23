import pytest
import game

#class TestStringMethods(unittest.TestCase):
    
    
    def test_getRegion(self):
        region = game.getRegion("euw1")
        self.assertIn(region,["br1","eun1", "euw1", "jp1", "kr", "la1", "la2", "na1", "oc1", "tr1", "ru"] )
   




if __name__ == "__main__":
    test_getRegion(self)
    print("Everything passed")
