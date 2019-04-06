__author__ = 'pinge'

# 1		python使用异常处理错误
		# '''
		# BaseException
		# SystemExit/KeyboardInterrupt/GeneratorExit
		# Exception
		# '''
# 2		使用异常常见场景
		# '''
		# 网络请求（超时，连接错误）
		# 资源访问（权限问题，资源不存在）
		# 代码逻辑（越界访问，KeyError）
		# '''
# tip
	# '''
	# 	try:
	# 		func									可能会抛出异常的代码
	# 	except(Exception1,Except2)as e:				可以捕获多个异常并处理
	# 		异常处理的代码
	# 	else:
	# 		else处理的代码							异常没有发生的时候的代码逻辑
	# 	finally:
	# 		最终处理的代码							必定执行的代码逻辑

	# '''

# 3		自定义异常
class MyExcept(Exception):
	print(55)
try:
    raise MyExcept
except Exception as e:
	print(e)
else:
	pass
finally:
	pass

class PricePolicyInvalid(Exception):
    def __init__(self,msg):
        self.msg = msg
try:
    raise PricePolicyInvalid('自定义的错误')
except Exception as e:
	print(e.msg)
else:
	pass
finally:
	pass