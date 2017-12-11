import requests

r = requests.get('https://www.douban.com/',params={'q': 'python', 'cat': '1001'})
# print(r.status_code)
# print(r.text)
print(r.url)
print(r.encoding)
print(r.content)
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())