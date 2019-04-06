__author__ = 'pinge'

数据结构与算法='''
数据结构/算法					语言内置							内置库
线性结构						list(列表)/tuple(元组)			array(数组，不常用)/collections.namedtuple
链式结构														collections.deque(双端队列)
字典结构						dict(字典)						collections.Counter(计数器)/OrderedDict(有序字典)
集合结构						set(集合)/frozenset(不可变结合)
排序算法						sorted
二分算法														bisect模块
堆算法														heapq模块
缓存算法														functools.lru_cache(Least Recent Used，python3)
'''
from collections import Counter,namedtuple,deque,OrderedDict,defaultdict

a= 'xzxzcscs'
print(Counter(a).get('x'))
print(Counter(a).most_common())

Point = namedtuple('Point', 'x,y')
p = Point(1,2)
print(p.x,p.y,p[0],sep='|')

d1 = deque()
d1.append(1)
d1.appendleft(2)
print(d1)
d1.popleft()
print(d1.popleft())
print(d1)

ord = OrderedDict()
ord['c'] = 1
ord['a'] = 0
ord['b'] = 6
print(ord.keys())

ded = defaultdict(int)
print(ded['a'])

# 2		py dict底层结构（底层使用的哈希表)
# 		'''
# 		为了支持快速查找使用了哈希表作为底层结构
# 		哈希表平均查找时间复杂度O(1)
# 		Cpython解释器使用二次探查解决哈希冲突问题
# 		'''
print(hash(111))
print(hash('sxassd'))
# print(hash(['1']))			#不可哈希类型
print(hash((1,2,)))

# tip			hash类型不可变

# 3		lrucache实现