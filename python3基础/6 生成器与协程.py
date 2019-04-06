__author__ = 'pinge'

# 1		什么是生成器

def xx():
	yield 'hello'
	yield 'world'
x=xx()
print(next(x))
print(next(x))

# 2		基于生成器的协程（python2）
def coro():
	hello = yield 'hello'			#yield 在右作为表达式，可以被send值
	yield hello
c = coro()
print(next(c))						#输出hello ，这里调用next产出第一个值hello 之后函数暂停
print(c.send('world'))				#调用send发送值，此时hello变量赋值为'world'，然后yeild产出hello的值'world'
									#之后协程结束，后续在send值会抛出异常StopIteration

# 3		协程装饰器
from functools import wraps
def outer(func):
	@wraps(func)
	def inner(*args,**kwargs):
		gen = func(*args,**kwargs)
		next(gen)
		return gen
	return inner

# 4		py3.5引入原生协程(async/await)