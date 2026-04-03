"""variables"""

# sher = "harsh bhaiya"
# SheryiansSchool = "students" #pascal case
# sheryiansSchool = "students" #camel case
# sheryians_school = "students" #snake case




"""data types"""

# a = -34
# b = 56.8
# c = 12/3
# v = 34j
# print(type(v))



# st = '1231243235 dsagaiogiaeb !@#$%^&*'
# print(type(st))
# b = True
# t = False
# print(type(b))


# """strings"""
# a = "SHER CODER"
# print(a[::])



# a = 12  bbb
# print(12/3)

# name = "akarsh"
# age = "23"
# print(f"my name is {name} and my age is {age}")



# age = int(input("hello what is your age"))
# print(age)


# a = 5
# b = 32
# print(a + b)
# print(b - a)
# print(a * b)
# print(b//a)
# print(b/a)
# print(5**100)
# print(32%5)


# print(12+4/2)


#assignment operators 
# a = 23

#compound assignmet operations
# a = 20
# a += 20
# a += 60
# a-=
# a*=
# a/=
# a//=
# a**=

# print(a)




# a = 12.1
# b = 12 
# print(a == b)
# print(a != b)
# print(a > b)
# print(45 < 67)
# print(23 >= 23)
# print(45 <= 45)


# print(ord("A"))
# print(ord("B"))

# print("ABC" > "ACD")
# print("A" > 34)
# print(12 >20 and 123 > 100 and 34 == 34 and 45 < 90)
# print(12 !=12 or 23 ==45 or 67 == 56 or 10 > 5)
# print(not 12 == 12)



#IF else 
# a = 6
# if a > 10:
#     print("I will do task A")

# else:
#     print("I will do task B")

# money = int(input("please provide me the money :- "))

# if money == 10:
#     print("I will have a choco bar icecream")

# elif money == 20:
#     print("I will have a mangodolly")

# elif money == 30:
#     print("I will have a frosty")
    
# else:
#     print("I will have a cone")


# take two num and then find which one is larger
# num1 = int(input("pleae tell your first number "))
# num2 = int(input("pleae tell your second number "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("Both the numbers are same")


# gen = input("please tell your gender as character (M or F):-")
# if gen == 'M' or gen == 'm':
#     print("Good morning SIR")
# elif gen == "F" or gen == 'f':
#     print("Good morning MAM")
# else:
#     print("Unidentified gender")


# num = int(input("please tell your number :- "))
# if num%2 == 0:
#     print("even number")
# else:
#     print("Odd number")


# name = input("please tell your name : - ")
# age = int(input("now tell your age :- "))
# if age >=18 :
#     print(f"hello {name} you are a valid vote")
# else:
#     print(f"hello {name} you are not a valid vote")


# year = int(input("tell your year :- "))
# if year %100 == 0 and year %400 == 0:
#     print("Its a leap year")
# elif  year %100 != 0 and year %4 ==0:
#     print("Its a leap year")
# else:
#     print("its a normal year")




# t = int(input("please tell the temprature :- "))
# if t < 0:
#     print("Freezing cold")
# elif t >= 0 and t <10:
#     print("very cold")
# elif t >= 10 and t <20:
#     print("cold")
# elif t >= 20 and t <30:
#     print("plesant")
# elif t >= 30 and t <40:
#     print("hot")
# else:
#     print("temprature is very hot ")




#For loop

#lets print a table of 5
# n = int(input("Which table you want ? "))
# for i in range(n,(n*10)+1,n):
#     print(i)



# a = "SHERYIANS TEACHES INDUSTRY THINGS"
# print(len(a))
# for i in range(len(a)):
#     print(a[i])


# a = "SHERYIANS IS COOL"
# for i in a:
#     print(i)



# for i in range(1,21):
#     if i == 56:
#         print("break statement is executed")
#         break
#     print(i)
# else:
#     print("Break statement is not executed")



# n = int(input("please tell your number"))
# for i in range(n):
#     print("hello world ")
# n = int(input("please tell your number "))


# for i in range(1,n+1):
#     print(i)
# n = int(input("please tell your number "))

# for i in range(n,0,-1):
#     print(i)

# print table
# n = int(input("which table you want : - "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# sum of the numbers
# n = int(input("please tell your number:- "))
# sum = 0 
# for i in range(1,n+1):
#     sum = sum + i
# print(f"your sum is {sum}")

# factorial 
# n = int(input("please tell your number:- "))
# fact = 1 
# for i in range(1,n+1):
#     fact = fact * i
# print(f"your factorial is {fact}")


# sum of the odd even number 
# n = int(input("tell your number :- "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"your even and odd sum are {even} , {odd}")


# factors of number 
# n =int(input("which number factors you want :- "))
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# perfect number 
# n = int(input("check your number is perfect or not :-"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i
# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")



# prime number or not 
# n = int(input("check your number is prime or not  :-"))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")



# Reverse of string 
# a = "SHERYIANS"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# print(b)



# palindrome string or not 
# a = "NAMAN"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print("your string is pallindrome")
# else:
#     print("its not a pallindrome")



# a = "sdfsogn12413@#$%^&U"
# char = 0
# dig = 0
# spchr = 0
# for i in a:
#     if i.isdigit():
#         dig +=1 
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr +=1 



# print(f"your digits are {dig}\nyour alphabets are {char}\nyour special characters are {spchr}")
# print(dir(str))
# a = 1 
# while a <= 30:
#     print(a)
#     a = a + 1



# reverse of the number 
# a = int(input("tell your number"))
# rev = 0
# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10
# print(rev)



# a = int(input("tell your number"))
# copy = a
# rev = 0
# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10
# if copy == rev:
#     print("pallindromic number")
# else:
#     print("not a pallindromic number")



# import random
# num = random.randint(1,10)
# tries = 0
# while True:
#     guess = int(input("please guess your number between 1 and 10 :- "))
#     if num == guess:
#         tries +=1
#         print(f"you are right you guessed the number is {tries} tries")
#         break
#     elif num < guess:
#         print("go a little lower")
#         tries +=1
#     elif num > guess:
#         print("go a little higher")
#         tries +=1
#     else:
#         tries +=1 
#         print("sorry you are wrong")
# print(12)




# def hello():
#     print("this is a hello function so I am doing hello")
# hello()


# def hello(name,age):
#     print(f"your name is {name} and your age is {age}")
# hello(age = 22,name = "akarsh")


# def pallindrome(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]
#     if rev == st:
#         print(f"{st} is a pallindrome")
#     else:
#         print(f"{st} is not a not a pallindrome")



# pallindrome("NAMAN")
# pallindrome("CURSOR")
# def hello():
#     return "hello how are you"
# print(hello())



# a = [12,13,14,15,16,34.5]
# #1st way using index
# for i in range(len(a)):
#     print(a[i])
# #2nd way directly on values
# for i in a:
#     print(i)


# find the positive number 
# l = [-45,67,12,-68,-69,34]
# print("positive elements are ")
# for i in l:
#     if i >= 0:
#         print(i)
# print("negitive elements are")
# for i in l:
#     if i < 0:
#         print(i)



# l = [12,435,67,89,23,25,69]
# sum = 0
# for i in l:
#     sum = sum + i
# print(sum/len(l))


# find the largest num 
# l = [12,567,43,235,347,568,45,7]
# largest = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i
# print(f"your largest number is {largest} at index {index}")



# largest and second largest find 
# l = [12,16,13,19,17]
# largest = l[0]
# sec_largest = l[0]
# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
# print(sec_largest, largest)


# list is sorted or not 
# a = [12,13,18,15,16]
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")



# a = (1,2,3,4,5,5,5.5,print(),"hello")
# count = a.count(5)
# print(count)


# a = (1,)
# print(type(a))



# a = {1,8,9,"hello",2,3,4,5}
# for i in a:
#     print(i)
# a = {8,1,2,3,4}
# a.clear()
# print(a)



# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# b -= a
# print(b)

# d = {10:100,20:200,30:300,40:400}
# d[10] = 100 #updating
# d[50] = 500 # creating
# del d[30] # deleting 
# print(d)




# d = {10:100,20:200,30:300,40:400}
# print(d.items())
# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}


# for i in d2:
#     d1[i] = d2[i]
# print(d1)
# d1 = {10:100,20:200,40:300}
# sum = 0
# for i in d1:
#     sum = sum + d1[i]
# print(sum)


# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] +=1 
#     else:
#         d[i] = 1
# print(d)


# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}
# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]



# exception handling 
# a = int(input("tell your number :- "))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"sorry there is an err as {err}")
# else:
#     print("good there is no exception")
# finally:
#     print("i will run no matter what")
# print("ok i have done the division")



# example 2
# age = int(input("tell your age :- "))
# try:
#     if age < 10 or age > 18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")
# except Exception as err:
#     print(f"an error occured as {err}")
# print("the club will start soon")





#File handling
# r = open("superman.txt",'a')
# r.write("and now I am appending some content inside the file  ")
# r.close()
# class Factory:
#     a = 12 # attribute 
#     def hello(self): #method
#         print("how are you")
    


# obj = Factory()
# obj2 = Factory()
# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
#     def show(self):
#         print(f"your object details are {self.material}, {self.pockets},{self.zips} ")

# reebok = Factory("leather",3,2)
# campus = Factory("nylon",3,3)
# reebok.show()

   

# class Animal:
#     name = "lion" #class attribute  

#     def __init__(self,age):
#         self.age = age #instance attribute   

#     def show(self):  #instance method
#         print(f"how are you your agger is {self.age}")  

#     @classmethod
#     def hello(cls):
#         print(f"how are you brother {cls.age}")

#     @staticmethod
#     def static():
#         print("how are you")

   

# obj = Animal(12)
# class Factorymumbai: #parent class / superclass
#     a = "I am an attribute mentioned inside Factory"
#     def hello(self):
#         print("hello I am a method mentioned inside Factory")

# class Factorypune(Factorymumbai):   #child class /subclass
#     pass
# obj = Factorymumbai()
# obj2 = Factorypune()
# obj2.hello()


# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(f"hello your name is {self.name}")
# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
#     def show(self):
#         print(f"hello your name is {self.name},{self.age}")


# animal1 = Animal("lion")
# person1 = Human("akarsh",23)
# animal1.show()
# class Animal:
#     def __init__(self,name):
#         pass
# class Human:
#     def __init__(self,name,age):
#         pass
# class Robots(Human,Animal):
#     name3 = "charli123"
# obj = Robots()
# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips 
    

# class BhopalFactory(Factory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
#         self.color = color 
# class Punefactory(BhopalFactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets


# class Animal:
#     def show(self):
#         print("hello I am akarsh")
    


# class Human(Animal):
#     def show(self):
#         print("how are you")

# obj = Human()
# obj.show()


# class Animal:
#     def show(self):
#         print("I am showing ")

# class Human:
#     def show(self):
#         print("hello I am also showing ")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()


# class Factory:
#     __a = "pune"

#     def show(self):
#         print(Factory.__a)


# obj = Factory()

# obj.show()


# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass 
    
#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side

#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")



# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius
    
#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")

# obj = Circle(7)
# obj2 = Square(12)


# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"hello how are you and your name is {self.name}"

#     def __add__(self,other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age

#         return f"your sum of ages are {self.age + sum}"

# obj = Animal("lion",12)
# obj2 = Animal("dolphin",14)
# obj3 = Animal("tiger",34)

# print(obj + (obj2,obj3))


# class Animal:
#     @property
#     def show(self):
#         print("hello how are you")
    
# obj = Animal()

# obj.show



# def decorate(func):
#     def wrapper(*args,**kwargs):
#         print("the addition to your numbers are ")
#         func(*args,**kwargs)
#         print("thankyou I hope you liked it ")
#     return wrapper



# @decorate
# def addition(a,b):
#     print(f"your total is {a + b} ")

# addition(12,67)


# def information(**kwargs):
#     print("your information is\n\n ")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")
    



# information(name = "Akarsh", age = 23, designation = "AI/ML")

# l = {i : i**2 for i in range(1,10)}

# print(l)

# a = [1,2,3,4,5]

# def double(x):
#     return x *2

# result = map(double,a)

# print(list(result))

# from modelss.model import hello,maths

# a = int(input("how many rows you  want "))

# for i in range(1,a + 1):
#     for j in range(i):
#         print("* ",end = "")
#     print()

# n = int(input("tell how many rows you want"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print("  ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()



# n = int(input("tell how many rows you want"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()


# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()

# a = 1234
# copy = a
# sum = 0


# while a > 0:
#     z = a %10
#     fact = 1 
#     for i in range(1,z+1):
#         fact = fact * i
    
#     sum = sum + fact
#     a = a//10 

# if sum == copy:
#     print("this is a strong number ")
# else:
#     print("not a strong number")


# for j in range(2,21):
#     a = j

#     for i in range(2,(a//2)+1):
#         if a % i == 0:
#             break

#     else:
#         print(a)



# a = [1,1,1,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5]
# count = 0
# dict = {}
# for i in a:
#     if i in dict.keys():
#         dict[i] +=1 
#     else:
#         dict[i] = 1
# max = 0
# for i in dict.values():
#     if i > max:
#         max = i
# for i in dict:
#     if dict[i] == max:
#         print(f"{i} occured {max} times and that is largest occurence")
#         break


# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello FastAPI"}   


