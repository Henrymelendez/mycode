#!/usr/bin/env python3

import requests
import urllib
def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    
    
    
    print(pokeapi["sprites"]["front_default"])


    
    for poke in pokeapi["moves"]:

        print(poke["move"]["name"])

    print(len(pokeapi["game_indices"]))
    
    count = 0;

    for poke in pokeapi["game_indices"]:

        count += 1
    
    print(count)



if __name__ == "__main__":

    main()

