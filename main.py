import requests
import json
import urllib.request as urllib2



u='username'
p='userpass'
url='https://api.github.com/users/username'

# simple wrapper function to encode the username & pass
def encodeUserData(user, password):
    return "Basic " + (user + ":" + password).encode("base64").rstrip()

# create the request object and set some headers
req = urllib2.Request(url)

req.add_header('Host', 'www.google.com/')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.5')
req.add_header('Accept', '*/*')
req.add_header('Referer', 'https://www.google.com/')
req.add_header('Cookie', 'NID=146=p-KPB8sQ6nqjr8I56LiEJzjdcsk7Wh91oDwr0jU0rfwOfN4Y_l9T4j_5uaSDg_6tDMSEXmPdhueoxwYM4w6meuHTK1R-Mej8-9Fm4kiEb8kFw8wVPnrgtaefkgNPq3W9ro81wpyImN-QtPVKILiNYq5UN07oTQWarcfgEXHOl0w6PR7uE4Xh14o; 1P_JAR=2018-11-12-04; OGP=-5061451:; DV=AwAhS-7BuJMeYH8oIYu_J3hJpKxjcBY')
req.add_header('Connection', 'keep-alive')
req.add_header("Content-type", "application/x-www-form-urlencoded")
req.add_header('Authorization', encodeUserData(u, p))
# make the request and print the results
res = urllib2.urlopen(req)
