import requests
r = requests.get('https://twitter.com/?lang=ru', auth=('user', 'pass'))
result = r
print(result)