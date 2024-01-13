import requests
r = requests.get('https://russianwarship.rip/api/v2/war-info')
r.json()
result = r.json()
print(result)


a = requests.get('https://russianwarship.rip/api/v2/war-info/status/en')
a.json()
result2 = a.json()
print(result2)