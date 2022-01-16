import json
import requests
import sys

url="https://phalanx.herokuapp.com/subs"
tkn=open("slack.token", "r")
with open('{}'.format(sys.argv[2])) as f:
    lines = f.read().splitlines()

subs = {"domain":"{}".format(sys.argv[1]),"subdomains":lines}

payload = json.dumps(subs)
headers = {
  'Authorization': 'Bearer {}'.format(tkn.readline().strip('\n')),
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))

