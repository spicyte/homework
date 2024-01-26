import requests

response = requests.get('https://russianwarship.rip/api/v2/war-info')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Помилка:', response.status_code)
