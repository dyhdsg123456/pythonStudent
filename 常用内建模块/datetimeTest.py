from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015, 4, 19, 12, 20)
print(dt)
print(dt.timestamp())

print(datetime.fromtimestamp(dt.timestamp()))
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(datetime.now().strftime('%a, %b %d %H:%M'))
