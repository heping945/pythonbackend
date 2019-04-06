__author__ = 'pinge'

# 1		python3 改进
		# '''
		# 1 print成为函数
		# 2 编码问题。 python3 不再有Unicode对象，默认str就是unicode
		# 3 除法变化。 python3 除号返回浮点数

		# 4 类型注解（type hint) 帮助ide实现类型检查
		# 5	优化的super()方便直接调用父类函数
		# 6	高级解包操作 a,b,*rest = range(10)
		# '''
print(3/2,10//3,10%3,sep='|')

def 大写(s):
	return s.upper()
print(大写('abc'))
print('你好'.encode())
#  tip  传输encode 转成字节  操作decode转换成Unicode（utf8）