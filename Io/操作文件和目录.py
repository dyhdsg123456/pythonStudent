import os
print(os.name)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join('E:/python/Io','testdir'))
# os.mkdir('E:/python/Io/testdir')
# os.rmdir('E:/python/Io/testdir')
print(os.path.split('/Users/michael/testdir/file.txt'))
print(os.path.splitext('/path/to/file.txt')[1])

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
