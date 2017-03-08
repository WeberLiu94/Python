# g=(x*x for x in range(10))
# for n in g:
# 	print(n)

#Learning Statrt at 2017-2-26 
#........偏函数.......
#关键字 functools.partial 在已有的函数上定义新函数
# import functools
# int_2=functools.partial(int,base=2) #在Int()强制转换的类型上定义一个2进制转为十进制的函数
# print(int_2('1'))

# ---------使用模块-----------------
# ---------标准格式-----------------
#!/usr/bin/env python3
#-*- coding utf-8 -*-
# 'a test module'
# __author__='Weber'
# # ---------代码区----------------
# import sys
# def test():
# 	args=sys.argv
# 	if len(args)==1:
# 		print("hello" )
# 	elif len(args)==2:
# 		print("hello,%s" %args[1])
# 	else:
# 		print("Too many arguments")
# if __name__=="__main__":
# 	test()
# # ---------代码区----------------
# -----加载第三方图形处理模块------
# from PIL import Image
# im = Image.open('test.png')
# print(im.format, im.size, im.mode)

# im.thumbnail((200, 100))
# im.save('thumb.jpg', 'JPEG')
#-------------------------------------
#类和实例 class and instance
#-------------------------------------------
# class Student(object):

# 	def __init__(self,name,score): #相当于构造函数 self 相当于this指针
# 		self.__name=name
# 		self.__score=score
# 	def print_score(self):
# 		print("%s %s" %(self.__name,self.__score))
# 	def set(self,name,score):
# 		self.__score=score
# 		self.__name=name

# bart=Student('Weber',99)
# bart.print_score()
# bart.set("Feng",100)
# bart.print_score()
#-------------------------------------------
#继承与多态 is a 关系
# class Animal(object):
# 	def run(self):
# 		print("Animal")
# class Dog(Animal):
# 	def run(self):
# 		print("Dog")
# class Cat(Animal):
# 	def run(self):
# 		print("Cat")

# def cout(Animal):
# 	Animal.run()
# A=Animal()
# D=Dog()
# C=Cat()
# cout(A)
# cout(D)
# cout(C)
#--------------------------------------------
#面向对象高级编程
#动态绑定属性与方法
# class Student(object):
# 	pass
# s=Student()
# s.name="Weber" #给实例动态绑定一个属性
# print(s.name)
# def set_age(self,age): #定义个一个函数作为实例的方法
# 	self.age=age
# from types import MethodType  #给实例动态绑定一个方法
# s.set_age=MethodType(set_age,s)
# s.set_age(25) #调用实例
# print(s.age)

# #给一个实例动态绑定的属性或者方法，只对改实例有效
# #为了给所有实例都绑定，可以直接给class绑定方法
# def set_score(self,score):
# 	self.score=score
# Student.set_score=set_score

# s.set_score(100)
# print(s.score)
#使用__slots__
#限制实例的的属性，只允许对Student添加某几项属性,
class Student(object):
	__slots__=('name','age') #只允许绑定name与age
s=Student()
s.name="Weber"
s.age=25
s.score=100
