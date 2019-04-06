__author__ = 'pinge'

# 1		可变参数/不可变参数（可变参数引用传递，不可变参数值传递？？->共享传参）
# 2			可变对象					/			不可变对象
# 				|									|
# 		list/set/dict					bool/int/float/str/frozenset/tuple

# tip     可变参数作为默认参数？(默认参数只计算一次)
def xx(l=[1]):
	print(id(l))
	l.append(1)
	print(l)
xx()
xx()

# 3		*ags/**kwargs(用来处理可变参数)，args打包成tuple，kwargs打包成dict
def print_multiple_args(*args):
	print(type(args),args)
	for index,val in enumerate(args):
		print(index,val)
print_multiple_args('c','a','b')
print_multiple_args(*(1,2,3,4))

def print_kwargs(**kwargs):
	print(type(kwargs),kwargs)
	for k,v in kwargs.items():
		print('{}:{}'.format(k,v))
print_kwargs(a=1,b=2)
print_kwargs(**dict(c=3,d=4))