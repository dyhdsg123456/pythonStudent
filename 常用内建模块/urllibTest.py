from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    # print('Status:', f.status, f.reason)
    # for k, v in f.getheaders():
        # print('%s: %s' % (k, v))
    # print('Data:', data.decode('utf-8'))

# 模拟iPhone 6去请求豆瓣首页

from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
    # print('Status:', f.status, f.reason)
    # for k, v in f.getheaders():
    #     print('%s: %s' % (k, v))
    # print('Data:', f.read().decode('utf-8'))



 # 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。


from urllib import request,parse
print('Login to weibo.cn...')
# email = input('duyuanhao321@sina.com ')
# passwd = input('13511683293DU')
login_data = parse.urlencode([
    ('username','duyuanhao321@sina.com' ),
    ('password', '13511683293DU'),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

    from urllib import request
    import json


    def fetch_data(url):
        with request.urlopen(url) as f:
            try:
                return json.loads(f.read().decode('utf-8'))
            except ValueError:
                raise '错误'


    URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
    data = fetch_data(URL)
    print(data)