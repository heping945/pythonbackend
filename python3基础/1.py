__author__ = 'pinge'

#  语言特性

# 1		python 是动态强类型语言（不能发生强势类型转换）  1+'1' ？
# 2		为什么要用python（优缺点）
		# '''
		# 1 胶水语言，轮子多，应用广泛
		# 2 语言灵活，生产力高
		# 3 性能问题，代码维护问题，python2/3 兼容问题
		# '''
# 3 	鸭子类型（关注点是对象的行为，而不是类型）
# 4     monkey patch(猴子补丁)    （运行时 能替换）
import time
print(time.time())
def _time():
	return 66
time.time = _time
print(time.time())
# 5		什么事自省（运行时判断一个对象的类型的能力）python 一切皆对象，用type，id，isinstance 获取对象类型信息
		# （inspect(/ɪn'spekt/)模块提供了获取更多对象信息的函数）
# 6		列表和字典推导
l = [i for i in range(10) if i % 2 ==0]
print(l)
l1 = 'dict'
l2 = [1,2,3,4,5]
d1 = {k:v for k,v in zip(l1,l2)}
print(d1)
		#  生成器
g = (range(10))
