__author__ = 'pinge'

# 1		python3 改进
		# '''
		# 1 print成为函数
		# 2 编码问题。 python3 不再有Unicode对象，默认str就是unicode
		# 3 除法变化。 python3 除号返回浮点数

		# 4 类型注解（type hint) 帮助ide实现类型检查
		# 5	优化的super()方便直接调用父类函数
		# 6	高级解包操作 a,b,*rest = range(10)

		# 7 keyword only arguments 限定关键字参数
		# 8 chained expections py3重新抛出异常不会丢失栈信息
		# 9 一切返回迭代器 range zip map dict.values  are all iterators
		# '''
print(3/2,10//3,10%3,sep='|')

def 大写(s):
	return s.upper()
print(大写('abc'))
print('你好'.encode())
#  tip  传输encode 转成字节  操作decode转换成Unicode（utf8）
a,b,*rest = range(10)
print(a,b,rest)

def add(a,b,*,c):
	return a+b+c
add(1, 2, c=3)

# 2		python3 新增
		# '''
		# 1 yield from 链接子生成器
		# 2 asyncio 内置库，async/await原生协程支持异步编程
		# 3 新的内置库enum，mock，asyncio，ipaddress，concurrent.futures
		# '''
import asyncio
print(asyncio.__doc__)

# import inspect
# print(inspect.__doc__)
# import concurrent
# print(concurrent.futures)

# 3		python3 修改
		# '''
		# 1 生成的pyc文件统一放到__pycache__
		# 2 一些内置库的修改 urllib，selector
		# 3 性能优化
		# '''
# 4		py2/3工具
		# six工具
		# __future__
		# 2to3等工具转换代码