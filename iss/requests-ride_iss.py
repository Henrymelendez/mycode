#!/usr/bin/python3

import urllib.request
import requests


MAJORTOM = "http://api.open-notify.org/astros.json"


def main():

    groundctrl = requests.get(MAJORTOM)
    
    helmetson = groundctrl.json()

    print("\n\Converted Python data")

    print(helmetson)

    print('\n\nPeople in space: ', helmetson['number'])
    people = helmetson['people']
    print(people)
    
    for people in helmetson["people"]:

        print(people["name"] + " on the " + people["craft"])

    


if __name__ == "__main__":

    main()
