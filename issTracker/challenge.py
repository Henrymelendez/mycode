#!/usr/bin/python3 

import requests
import datetime

API = "http://api.open-notify.org/iss-now.json"

def main():

    res = requests.get(API)

    rod = res.json()
    time = rod["timestamp"]    
    pod = rod["iss_position"]
    time = datetime.datetime.fromtimestamp(time)
 


    print("CURRENT LOCATION OF THE ISS:")
    print(f'Timestamp: {time}')
    print(f'Lon: {pod["longitude"]}')
    print(f'Lat: {pod["latitude"]}')



if __name__ =="__main__":
    main()
