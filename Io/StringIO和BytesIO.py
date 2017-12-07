from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))

print(f.getvalue())

ff = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=ff.readline()
    if s=='':
        break
    print(s.strip())


from io import BytesIO
k=BytesIO()

print(k.write('中文'.encode('utf-8')))
print(k.getvalue())

l=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(l.read())