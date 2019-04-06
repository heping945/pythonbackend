__author__ = 'pinge'

# 1		什么是Cpython GIL(全局解释器锁)Global Interpreter Lock
# 		'''
# 		Cpython解释器的内存管理并不是线程安全的
# 		保护多线程情况下对python对象的访问
# 		Cpython使用简单的锁机制避免多个线程同时执行字节码
# 		'''
# 2		影响（限制了程序的多核执行）
# 		'''
# 		同一个时间只能有一个线程执行字节码
# 		cpu密集程序难以利用多核优势
# 		io期间会释放GIL,对io密集程序影响不大
# 		'''
# 3		如何规避GIL影响（区分CPU和IO密集程序）
# 		'''
# 		cpu密集可以使用多进程＋进程池
# 		io密集使用多线程/协程
# 		Cpython扩展
# 		'''
# 4		原子操作（一步执行完）
# 		dis模块分析字节码

# 5		剖析程序性能
# 		使用profile/cprofile模块

# 6		服务端性能优化措施（web应用一般语言不会成为瓶颈）
# 		'''
# 		数据结构与算法优化
# 		数据库层：索引优化，慢查询消除，批量操作减少io NoSQL
# 		网络IO：批量操作，pipline（管道）操作，减少IO
# 		缓存：使用内存数据库 redis/memcached
# 		异步：asyncio/celery
# 		并发：gevent/多线程
# 		'''