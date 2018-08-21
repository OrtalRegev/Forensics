import requests
params = {'apikey': '57e95031da06b72c7430b1b653d477d258db9226e28e4f8a4c4389db3dfac0c8', 'resource': 'f5ebbde3539c7816f737bf77dbaa0cab'}
headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent": "gzip,  My Python requests library example client or username"
  }
response = requests.post('https://www.virustotal.com/vtapi/v2/file/report', params=params)
json_response = response.json()
print(str(json_response['positives']) + ' from ' + str(json_response['total']))
