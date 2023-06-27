#!/usr/bin/env python3

import sys
import os
import requests
from argparse import ArgumentParser

# print(requests.__file__)
# openweathermap.org for api key
#  OWN_API_KEY=129d0d48abc002e4b5e118211e11767f weather 20171


parser = ArgumentParser(description='Get the current weather information')
parser.add_argument('zip', help='zip/postal code to get the weather for')
parser.add_argument('--country', default='us', help='county zip/postal belongs to, default is "us"')

args = parser.parse_args()

url = "http://api.openweathermap.org/data/2.5/weather?zip=%s,%s&APPID=%s" % (
        args.zip,
        args.country,
        os.getenv("OWN_API_KEY"))

res = requests.get(url)

if res.status_code != 200:
    print("Error talking to weather provider : %s" % res.status_code)
    sys.exit(1)

print(res.json())
