from  collections import namedtuple

point = namedtuple('Point', ['x', 'y'])
p = point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p,point))
print(isinstance(p,tuple))

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque

d = deque(['a', 'b', 'c'])
d.append('x')
d.appendleft('g')
print(d)

#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda :'N/a')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

# 如果要保持Key的顺序，可以用OrderedDict：

from collections import OrderedDict

ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(ordered_dict)#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

from collections import Counter
c = Counter()
for ch in 'programming':
  c[ch] = c[ch] + 1

print(c)
Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
