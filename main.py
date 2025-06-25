import random
from characters import *
from combat import *
from rooms import *

def main():
    print ("Welcome adventurer!\nPlease select a character!")
    while True:
        character = input("Would you like to play as: Toby or Asterion?")
        if character == "Toby":
            print("You have selected the Gnomish Wizard, Toby Sprinkledust!")
            input("Press Enter to Begin!")
            combat_encounter(Toby_Sprinkledust, Asterion)
            break
        if character == "Asterion":
            print("You have selected the vamperic rogue Asterion!")
            input("Press enter to continue")
            combat_encounter(Asterion, Toby_Sprinkledust)
            break
        else:
            print("That character is not playable")
            
    
    
            
    
main()
    
    
    