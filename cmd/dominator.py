import sys
import json
import requests
requests.packages.urllib3.disable_warnings()

services = '{"Agile CRM": "Sorry, this page is no longer available", "Anima": "If this is your website and you\'ve just created it, try refreshing in a minute", "AWS/S3":"The specified bucket does not exist", "Bitbucket":"Repository not found", "Campaign Monitor":"Trying to access your account?", "Cargo Collective":"404 Not Found", "Fastly":"Fastly error: unknown domain:", "Fly.io":"404 Not Found", "Gemfury":"404: This page could not be found", "Ghost":"The thing you were looking for is no longer here, or never was", "Github":"There isn\'t a Github Pages site here", "HatenaBlog":"404 Blog is not found", "Help Juice":"We could not find what you\'re looking for", "Help Scout":"No settings were found for this company:", "Heroku":"No such app", "Intercom":"Uh oh. That page doesn\'t exist.", "JetBrains":"is not a registered InCloud YouTrack", "Kinsta":"No Site For Domain", "LaunchRock":"It looks like you may have taken a wrong turn somewhere. Don\'t worry...it happens to all of us", "Mashery":"Unrecognized domain", "Ngrok":"Tunnel *.ngrok.io not found", "Pantheon":"404 error unknown site!", "Pingdom":"This public report page has not been activated by the user", "Readme.io":"Project doesnt exist... yet!", "Shopify":"Sorry, this shop is currently unavailable", "SmartJobBoard":"This job board website is either expired or its domain name is invalid", "Strikingly":"page not found", "Surge.sh":"project not found", "Tumblr":"Whatever you were looking for doesn\'t currently exist at this address", "Tilda":"Please renew your subscription", "Uberflip":"Non-hub domain, The URL you\'ve accessed does not provide a hub", "Unbounce":"The requested URL was not found on this server", "Uptimerobot":"page not found", "UserVoice":"This UserVoice subdomain is currently available!", "Webflow":"The page you are looking for doesn\'t exist or has been moved", "Wordpress":"Do you want to register *.wordpress.com?", "Worksites":"Hello! Sorry, but the website you&rsquo;re looking for doesn&rsquo;t exist"}'
dict = json.loads(services)
o=0

tkn = open("slack.token", "r")
with open("{}".format(sys.argv[1]), "r") as f:
    for s in f:
        r = requests.get("http://{}".format(s.strip('\n')), verify=False)
        for k in dict:
            if r.text.find(dict[k]) != -1:
                print("\e[33m[*] Potential http://{} {} Takeover\e[0m".format(s.strip('\n'), k))
                files = {
                    'token': (None, '{}'.format(tkn.readline())),
                    'channel': (None, 'dominator'),
                    'text': (None, '🌟 Potential http://{} {} Takeover 🌠'.format(s.strip('\n'), k)),
                }
                requests.post('https://slack.com/api/chat.postMessage', files=files)
                o+=1
if o==0:
    print("\e[33m[*] No Potential Subdomain Takeover\e[0m")
