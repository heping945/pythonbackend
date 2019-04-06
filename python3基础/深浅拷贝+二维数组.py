__author__ = 'pinge'

class A1():
	pass
a = A1()
print('is and =='.center(120,'*'))
b = A1()
print(id(a),a)
print(id(b),b)
print(a is b)
print(a == b)
# is 比较的是两个实例对象是不是完全相同，它们是不是同一个对象，
# 占用的内存地址是否相同。莱布尼茨说过：“世界上没有两片完全相同
# 的叶子”，这个is正是这样的比较，比较是不是同一片叶子（即比较的i
# d是否相同，这id类似于人的身份证标识）。

# == 比较的是两个对象的内容是否相等，即内存地址可以不一样，
# 内容一样就可以了。这里比较的并非是同一片叶子，可能叶子的种类
# 或者脉络相同就可以了。默认会调用对象的 __eq__()方法。
'''
1、is 比较两个对象的 id 值是否相等，是否指向同一个内存地址；
2、== 比较的是两个对象的内容是否相等，值是否相等；
3、小整数对象[-5,256]在全局解释器范围内被放入缓存供重复使用；
4、is 运算符比 == 效率高，在变量和None进s行比较时，应该使用 is。
'''
# 1		深浅拷贝
a = ["i", "love", "Python"]
b = a
print(a is b)							# 赋值
c = a[:]								# 浅拷贝
print(c)
print(id(a),id(b),id(c))
print(c is a)

# 深浅拷贝
print('深浅copy'.center(120,'*'))
import copy
a = ['a',['age',12]]
b = a
c = a[:]						#切片会创造新的对象地址，是浅copy  只copy外部容易，内部元素继续原容器引用
d = copy.deepcopy(a)			#深copy一个新的对象，所有元素创建新的地址
b[0]='b'
b[1][1]=13
print(a,b,a is b)				
c[0]='c'
c[1][1]=14
d[0]='d'
d[1][1]=16
print(a,b,c,d,sep='\n')
print(id(a),id(b),id(c),id(d))
print('a:',[id(x) for x in a])
print('b:',[id(x) for x in b])
print('c:',[id(x) for x in c])
print('d:',[id(x) for x in d])

#  总结：  python 中的 = 赋值  是把   变量 指向对象（值）；

# 2		二维数组
# errtest
examlist = [1,2,3]
errlist = [examlist]*3				# 创建引用
print(errlist)
errlist[0].append(5)
print(errlist)

# coretst
l = [1,2,3]
corlist = [[x for x in l]for i in range(3)]
print(corlist)

