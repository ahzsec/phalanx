import json
import requests
import sys

url="https://phalanx.herokuapp.com/subs"

with open('{}'.format(sys.argv[2])) as f:
    lines = f.read().splitlines()

subs = {"domain":"{}".format(sys.argv[1]),"subdomains":lines}

payload = json.dumps(subs)
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZjdhYWIwN2Q4MWE5YjNlYzRlNDVlY2YiLCJpYXQiOjE2MDE4ODg3Mjh9.CFULuwc-GjFJSOIy7YNnMlTsOGhaPpBwt5gHYoVigBM',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))

