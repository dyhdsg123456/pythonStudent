import chardet
print(chardet.detect(b'Hello, world!'))
# data = '离离原上草，一岁一枯荣'.encode('gbk')
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))
