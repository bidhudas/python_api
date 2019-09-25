#import urllib.request
#import json

#astros = urllib.request.urlopen("http://api.open-notify.org/astros.json")
#payload = astros.read()

#print(type(payload))

#astrosdecoded = json.loads(payload)

#print(type(astrosdecoded))

import requests
astros = requests.get("http://rzfeeser.com")

print(astros.json())
