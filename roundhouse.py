import json
import requests

url = "http://api.chucknorris.io/jokes/random"

payload = {}
headers = {
  'Cookie': '__cfduid=de3969405b80ca385f3fe23ac544eff291600016091'
}

response = requests.request("GET", url, headers=headers, data = payload)

resp = response.json()

print(resp["value"])