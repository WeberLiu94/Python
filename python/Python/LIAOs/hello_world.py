# print('我日你','妈卖批')
# name=input('草拟吗快点告诉我你的名字')
# print('原来的你的名字叫',name);
# -----------------------------------

# s1=72
# s2=85
# r=(85-72)/72*100//1
# print('小明今年的成绩提高了: %r %%' %r)
# -----------------------------------

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])
# -----------------------------------

# weight=80.5
# height=1.75
# BMI=80.5/1.75/1.75
# if BMI>32:
# 	print('严重肥胖')
# elif BMI>28:
# 	print('肥胖')
# elif BMI>25:
# 	print('过重')
# elif BMI>18.5:
# 	print('正常')
# else: 
# 	print('过轻')

# -----------------------------------
# L = ['Bart', 'Lisa', 'Adam']
# for X in L:
# 	print('hello',X)
# for s in L:
# 	print('hello %s' %s)
# -----------------------------------

# n1=25
# n2=1000
# n1_hex=hex(n1)
# n2_hex=hex(n2)
# print(n1_hex,n2_hex)
# -----------------------------------

# import math
# def quadratic(a,b,c):
# 	x1=(math.sqrt(b*b-4*a*c)-b)/(2*a)
# 	x2=(-math.sqrt(b*b-4*a*c)-b)/(2*a)
# 	return x1,x2
# result=quadratic(1,-4,4)
# print("result is",result)
# -----------------------------------

# 汉诺塔移动
# def move(n,a,b,c):
#     if n == 1:      # 只有一个盘子时，直接从a移动到c
#         print(a,'-->',c)
#         return
#     move(n-1,a,c,b)     # 大于一个盘子时，开始递归，首先将n-1个盘子从a移到辅助区b
#     move(1,a,b,c)       # 然后将最后一个大盘子从a移动到c
#     move(n-1,b,a,c)     # 最后将原来移动到b的盘子移动到c

# move(3,'A','B','C')     # 收工实验
# -----------------------------------

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if(isinstance(s,str)==True)]
# print(L2)
# ---------------------------------------
# def fib(max):
# 	n,a,b=0,0,1
# 	while n<max:
# 		yield b #print(b)
# 		a,b=b,a+b
# 		n=n+1
# 	return 'done'
# def odd():
# 		print('step 1')
# 		yield 1
# 		print('step 2')
# 		yield 3
# 		print('step 3')
# 		yield 5
# g=fib(6)
# while True:
# 	try:
# 	    x=next(g)
# 	    print('g=',x)
# 	except StopIteration as e:
# 		print('Generator return value',e.value)
# 		break
# -------------------------------------------
# 杨辉三角
# def Yang(max):
# 	L=[1]
# 	n=0
# 	while(n<=max):
# 		yield L
# 		L.append(0)	# 在末尾添加一个0
# 		L=[L[i-1]+L[i] for i in range(len(L))]
# 		# 下一行的数字都是前一行
# 		# 对应位置数字与前面的位置的数字相加
# 		# 首位是上一行的首位与新添加末尾（0）相加
# 		n=n+1
# 	return 'done'

# Triangle=Yang(9)
# for x in Triangle:
# 	print('L',x)
# ------------------------------------------
# 用isinstance()判断是否为可迭代对象
# from collections import Iterable
# isinstance([],Iterable)
# isinstance({},Iterable)
# isinstance('ABV',Iterable)
# isinstance(range(10),Iterable)
# isinstance(199,Iterable)
#-------------------------------------------
# iterator 可以被next()不断调用 
# 也可以用Isinstance()来判断
#通过iter()来将iterable 变成iterator
# for x in [1,2,3,4,5]:
# 	print(x)
# # 等价于：
# it=iter([1,2,3,4,5])
# while True:
# 	try:
# 			x=next(it)
# 			print(x)
# 	except StopIteration:
# 			break
# ----------------------------------------------
# 高阶函数--传入函数
# f=abs
# print(f(-10))
# def add(x,y,f):
# 	return f(x)+f(y)
# num=add(-5,6,f)
# print(num)
# ----------------------------------------------
# map/reduce
# map实现f(x)=x^2
# def f(x):
# 	return x*x
# L=range(10)
# r=map(f,L)
# print(list(r))
# -----------------------------------------------
# reduce实现求和运算
# from functools import reduce
# def add(x,y):
# 	return x+y
# l=range(10)
# r=reduce(add,l)
# s=sum(l) #也可以使用sum来求和
# print(r,s)
#------------------------------------------------
#使用reduce变换数组
#将【1,3,5,7,9】变成13579
# from functools import reduce
# def fun(x,y):
# 	return x*10+y
# r=reduce(fun,[1,3,5,7,9])
# print(r)
# ------------------------------------------------
# 使用reduce与map实现字符串转int函数
# from functools import reduce

# def strint(s):
# 	def fn(x,y):
# 		return x*10+y
# 	def char(s):
# 		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# 	return reduce(fn,map(char,s))
# q=strint("192464654654894165421564132168764")
# print(q)
# --------------------------------------------------
# 规范人名的大小写
# def strpro(s): 
# 	s=s[0].upper()+s[1:].lower() #str类型不能修改，使用切片
# 	return s
# l=['weber','jack','lily']
# r=list(map(strpro,l))
# print(r)
# ---------------------------------------------------
# 利用reduce求累乘
# from functools import reduce
# def prod(l):
# 	def func(x,y):
# 		return x*y
# 	return reduce(func,l)
# l=[1,2,3,4,5,6]
# print(prod(l))
#----------------------------------------------------
# 字符串转化为浮点数
# from functools import reduce
# def Str_to_float(s):
# 	i=0
# 	j=0
# 	s_2=s[::-1]
# 	while i<len(s):        #基本思路是小数点两边的数字分别相乘再相加
# 		if s[i]=='.':      #但是步骤太过于繁琐，将字符转为int也繁琐
# 			j=i
# 		i=i+1
# 	L_1=s[:j]
# 	k=len(s)-j-1
# 	L_2=s_2[:k]
# 	def divert(x,y):
# 		return x*10+y
# 	def divert_2(x,y):
# 		return x*0.1+y	
# 	def char(s):
# 		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# 	return reduce(divert,map(char,L_1))+0.1*reduce(divert_2,map(char,L_2))
# A='154864.262'
# print(Str_to_float(A))
# 更加简便的方法
# ------------------------------------------------------
# from functools import reduce
# def str2float(s):
#     L = [int(r) for r in s if r != '.']  #直接将字符串中除了的数字转化为Int
#     z = reduce(lambda x, y: x * 10 + y, L) #先直接相乘加
#     n = len(L) - s.index('.') #计算小数点有后几位
#     z = z / pow(10, n)#用总数除以这个位数
#     return z
# print('str2float(\'123.456\') =', str2float('123.456'))
#------------------------------------------------------------\
#sorted排序
#根据人名
# def by_name(t):
# 	return t[:][0]
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(sorted(L,key=by_name))
#根据成绩
# def by_score(t):
# 	return t[:][1]
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(sorted(L,key=by_score))
#更加简单得语句 使用lambda
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(sorted(L,key=lambda x:x[0]))
# print(sorted(L,key=lambda x:x[1]))
#--------------------------------------------------------------

#decorator 装饰器 
# 不带参数
# import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# 带参数
# import functools
# ------------------------------------------------------
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# ------------------------------------------------------
# import functools
# def log(func):
# 	@functools.wraps(func)
# 	def wrapper(*args,**kw):
# 		print('begin call:')
# 		return func(*args,**kw)
# 	return wrapper
# @log
# def hello():
# 	print('call hello')
# 	print('end call') 
# hello()

import functools
def log(args):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print(text,'%s'%func.__name__)
			return func(*args,**kw)
		return wrapper
	if isinstance(args,str):  #函数从这里开始执行
		text=args
		return decorator
	else:
		text="CALL"
		return decorator(args)

@log
def hello():
	print('hello')
hello()