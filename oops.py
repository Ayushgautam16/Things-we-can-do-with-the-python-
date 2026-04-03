# class factory:
#     a = 12 #attribute

#     def hello(self) :     #method
#         print("hello bhaiya kaise ho!")

#     print("hello how are u")


# print(factory().a)
# factory().hello()

# obj = factory()

# obj2 =factory()






# constructor 
# constructor evokes automatically when we call the class 

# class factory:
#     def __init__(self,material,zips,pockets):
#         self.zips =zips
#         self.pockets= pockets
#         self.material = material

# reedbook = factory("leather",3,2)
# campus = factory("nylon",3,3)

# print(reedbook.pockets)
# print(campus.zips)








# types of methods
# class animal:
    
#     def __init__(self,age):
#         self.age=age   #instance attribute
    
#     def show(self):     #instance method 
#         print("how are you")


# class method 
# @classmethod 
# def static():    
#     print("how are u ")

# @staticmethod 
# def static():
#     print("hello how are u")



# obj = animal(12)
# obj.show()
 

# A destructor is a special method that is automatically called when an object is about to be destroyed (i.e., removed from memory).

# In Python, the destructor is defined using:
# __del__()
# ex-
# class ClassName:
#     def __del__(self):
#         # cleanup code


#  inheritance
# single level inheritance 
# One child class inherits from one parent class.


# class factorymumbai:      #parent class
#     a ="hello there here im coding"
#     def hello(self):
#         print("hello buddy ")
# class factorypune(factorymumbai):    #child classs
#     pass
# obj = factorymumbai()
# obj2 = factorypune()
# print(obj.a)  

# ex2 
# class father:
#     def skill(self):
#         print("Driving")

# class me(father):
#     pass
# obj = me()
# obj.skill()




# multiple inheritance 
# One child class inherits from multiple parent classes

# class animal:
#     name1 = "lion"
# class human:
#     name2 = "ayush"
# class robots(animal,human):
#     name3 = "charlie123"
# obj = robots()
# print(obj.name2)



# class grandfather:
#     character1 = "eyes color"
# class father:
#     character2 = "height"
# class me(grandfather,father):
#     character3 = "shape of nose"
# obj = me()
# print(obj.character3)



# multilevel inheritance 
# 👉 A chain of inheritance (grandparent → parent → child)
# class grandfather:
#     def property(self):
#         print("Land")

# class father(grandfather):
#     def skill(self):
#         print("litigation")

# class me(father):
#     def hobby(self):
#         print("Coding")

# obj = me()
# obj.property()
# obj.skill()
# obj.hobby()


# 🔹 4. Hierarchical Inheritance
# 👉 One parent class → multiple child classes

# class father:
#     def skill(self):
#         print("Business")
# class son1(father):
#     pass
# class son2(uncle):
#     pass
# obj1 = son1()
# obj2 = son2()
# obj1.skill()
# obj2.skill()



# What is MRO in Python?
# MRO (Method Resolution Order) defines the order in which Python searches for methods and attributes in a class hierarchy (especially in inheritance).


# 5. Hybrid Inheritance

# class A:
#     def showA(self):
#         print("Class A")

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# obj = D()
# obj.showA()

# ✔ Combines:
# Hierarchical + Multiple inheritance



# 2. Encapsulation
# Encapsulation is binding data + methods together and controlling access.
# class father:
#     def __init__(self):
#         self.name = "Akash"        # public
#         self._age = 21             # protected
#         self.__salary = 50000      # private

#     def get_salary(self):
#         return self.__salary

# obj = father()

# print(obj.name)       # ✅ public
# print(obj._age)       # ⚠️ possible but not recommended
# print(obj.get_salary())  # ✅ controlled access





# 3. abstraction 
# from abc import ABC, abstractmethod

# class Person(ABC):
#     @abstractmethod
#     def work(self):
#         pass

# class Me(Person):
#     def work(self):
#         return "I am coding"

# obj = Me()
# print(obj.work())






# 4. Polymorphism?
# Polymorphism means “one name, many forms”
#  Same function/method behaves differently in different situations.

# 🔸 Types of Polymorphism in Python
# # ✅ 1. Method Overriding 

# 👉 Child class changes the behavior of parent class method

# class father:
#     def skill(self):
#         print("Driving")

# class me(father):
#     def skill(self):
#         print("Coding")

# obj = me()
# obj.skill()

# 2. Method Overloading (Python way ⚠️)
# 👉 Python does NOT support true overloading like Java
# But we achieve it using:
# default arguments
# *args


# a = [1,2,3,4,5,6,7]

# def double(x):
#     return x *2

# result = map(double,a)
# print(list(result))

# 🔹 What is super()?
# super() is used to call methods of the parent class inside the child class.

# 1. Constructor in Python
# 👉 What is Constructor?
# A constructor is a special method that is automatically called when an object is created.
# ✔ Used to initialize variables

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("Constructor called")

# obj = Student("Ayush", 21)
# print(obj.name)
# print(obj.age)

# 1. Default Constructor
# class A:
#     def __init__(self):
#         print("Default constructor")
# obj = A()
# # 2. Parameterized Constructor
# class A:
#     def __init__(self, x):
#         self.x = x
# obj = A(10)
# print(obj.x)


# 2. Destructor in Python
# 👉 What is Destructor?
# A destructor is called when an object is destroyed.
# ✔ Used for cleanup (closing files, releasing memory)

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("Constructor called")

#     def __del__(self):
#         print("Destructor called")
# obj = Student("Ayush")

# 🎯 What is a Decorator?
# A decorator is a function that modifies the behavior of another function without changing its code.
# def greet():
#     print("Hello")
# def my_decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello")
# greet()