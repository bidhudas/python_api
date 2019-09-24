#!/usr/bin/python3
'''Zach Feeser || rzfeeser@alta3.com || Using requests with NASA API APOD'''

APOD = "https://api.nasa.gov/planetary/apod55"

# python3 -m pip install requests
import requests
import argparse
from time import gmtime, strftime

def main():

    date = args.date
    if date == "today":
        date = strftime("%Y-%m-%d", gmtime())



    with open("/home/student/nasaapod.cred", "r") as cred:
        apikey = cred.read().rstrip('\n')


    nasa = requests.get(APOD + "?" + "api_key=" + apikey + "&date=" + date)
    if nasa.status_code != 200:
        print("Appears there is an issue with the URL / API resource.\nTransaction not completed.\nExiting...")
        exit()
    
    nasaj = nasa.json()

    print(nasaj.get('date'))

    print(nasaj.get('explanation'))

    print(nasaj.get('hdurl'))


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', help="Date to lookup in YYYY-MM-DD format", nargs='?', default='today', type=str)
    args = parser.parse_args()
    
    main()
