# # sher =  "hsv color space"
# # print(sher)

# # """"s jjsje ev e
# #  vevekve vvnv"""

# # Sheriyan_school = "sheriyan school"

# # Pascal_case = "pascal programming language"
# # print(Sheriyan_school)
# # print(Pascal_case)
# a= 23
# print(a)


# ad = 23.4    
# print(ad)
# ad = "sheriyan school"
# print(ad)

# print(type(a))
# print(type(ad))

# a ="dfjhvejkjvjkvbevelehjlevje"
# print(a)
# print(type(a))

# a =68
# print(chr(a))

# a = "sheriyan school"
# print(a[0])
# print(a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14])

# print(a[0:3:1])
# print(a[0:15:1])
# print(a[0:15:3])

# a = "sfvjv"
# print(a[0:5:1])

# name = input 

# a = "good morning"
# print(a[2:5])

# a = 12
# a = str(a)
# print(a)
# print(type(a))

# c = "12"
# c = int(c)
# print(c)
# print(type(c))

# a = 12
# b = 23
# print(a + b) 

# cs = "12"
# cs = bool(cs)
# print(cs)
# print(type(cs))

# wfw = 2223.24
# wfw = bool(wfw)
# print(wfw)
# print(type(wfw))

# fefe =23.44
# print(type(fefe))

# name = input("what is your name? ")
# print("hello " + name)

# name = input("please eneter your namae")
# print("this is my name " + name + " and i am learning python")

# # format sting 
# name = input("what is your name? ")
# age = input("what is your age? ")   
# print("my name is {} and i am {} years old".format(name, age))


# name = input("what is your name? ")
# age = input("what is your age? ")
# print ("my name is {name} and age is {age}" .format (name=name,age =age))

# operators in python
# a = 12
# b = 23
# print(a + b)  # addition  
# print(a - b)  # subtraction
# print(a * b)  # multiplication      
# print(a / b)  # division
# print(a % b)  # modulus
# print(a ** b)  # exponentiation
# print(a // b)  # floor division


# for p in range(1, 11):
#     print(p)





# for p in range(100, 11, -2):
#     print(p)    

# a = "sheriyan fvevwffwfschool"
# print(len(a))

# for i in range (len(a)):
#     print(a[i])

a = "sheriyans is cool and i am learning python"
for i in a:
    # if i == "s":
        print(i)


# for i in range (1, 11):
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")

# n = int(input("enter a number: "))
# for i in range(1, n+1):
#    print(i)

# n = int(input("enter a number: "))
# for i in range (n, 0, -1):
#     print(i)

# for i in range(2, 20, 2): # so the first one is for initialization 2nd 1 for for last num till the loop run and last one is for the steps
#     print(i)

# number = int(input("enter the num : "))
# for i in range (1, number+1):
#     print(i)


# num = int(input("enter a number: "))
# for i in range (num , 0, -1):
#     print(i)

# for i in range (1, 11):
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")



# sum of n terms 
# sum = 0
# n = int(input("enter a number: "))
# for i in range (1, n+1):
#     sum = sum + i   
# print("the sum of n terms is: ", sum)

# factorial of number 
# factorial = 1
# num = int(input("enter a number: "))
# for i in range (1, num+1):
#     factorial = factorial * i   
# print("the factorial of the number is: ", factorial)



# n = int(input("enter a number: "))
# even = 0 
# odd = 0
# for i in range (1, n+1):
#     if i % 2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print("the sum of even numbers is: ", even)
# print("the sum of odd numbers is: ", odd)


# sum of factors of num 
# factor = 0
# num = int(input("enter a number: "))
# for i in range (1, num+1):
#     if num % i == 0:
#         factor = factor + i
# print("the sum of factors of", num, "is", factor)


# factor of the num 

# num = int (input("enter the num: "))
# for i in range (1, num+1):
#     if num % i == 0:
#         print(i)


# perfect number 

# num = int(input("enter a number: "))
# sum = 0
# for i in range (1, num):
#     if num % i == 0:
#         sum = sum + i

# if sum == num:
#     print(num, "is a perfect number")
# else:
#     print(num, "is not a perfect number")


# num = int (input("enter the num: "))
# sum =0
# for i in range (1, num):
#     if num % i ==0:
#         sum = sum + i
# print("the sum of factors of", num, "is", sum)

# n = int(input("enter the number to check perfect num or not: "))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum+=i 

# if sum == n:
#     print("number is perfect number")
# else: print("{n} not a perfect num ".format(n=n))



# prime number 
# count=0
# n = int(input("enter the number: "))
# for i in range(1,n+1):
#     if n%i ==0:
#         count+=1

# if count ==2:
#     print('your num is prime')
# else:
#     print("your num is not prime")



# reverse of the string 
# a = "sheriyanschool"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b+ a[i]

# print(b)



# check the string is palindrome or not 

# a = input("Enter a string: ")
# b = ""

# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]

# if b == a:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")



# reverse the num

# a = int (input("enter the num"))
# while a > 0:
#     print(a%10)
#     a =a//10



# a = int (input("enter the num"))
# rev =0
# while a > 0:
#     rev = rev*10+a%10
#     a =a//10

# print(rev)


# a = int (input("enter the num"))
# rev =0
# while a > 0:
#     rev = rev*10+a%10
#     a =a//10

# print(rev)

# function 
# functional code 

# def hello():
#     print("hello boiii this is the intro oof the functional call")

# hello()

# parametric function 
# def sum(a,b):
#     print(f"sum of the num {a+b}")

# sum(12,12)

# 1. positional argument
# def hello(name, age):
#     print(f"your name is {name} and age is {age}")

# hello(age =22, name ="ayush")

# 2. positional argument 
# def sum(a,b=33):   #here in the argument the default value of b= 33
#     print(f"sum of the num {a+b}")
# sum(12,44)   #here the valu updated in the argument 


# def pallindrome(st):
#     rev =""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         print("string is palindrome")
#     else: ("not the palindrome string")


# pallindrome("naman")
# pallindrome("cursonfeej")

# Data structure 

# a =12,23,4          how to store the nums
# list 
# duplicate allow 
# mutable
# hetrogeneous allow print function allow num alphabet stri sb allow hai 

# a = [12, 13,23,23,44,12,3,24, print("hello boii"), True]

# # print(a[8])
# # first way using index 

# for i in range (len(a)):
#     print(a[i])


# mean of the list element 

# l = [12,32,434,34,57]
# sum = 0
# for i in l:
#     sum = sum +i
# print(sum/len(l))



# l = [12,32,434,34,57]
# largest = l[0]
# index = 0 

# for i in range(len(l)):
#     if l[i]> largest:
#         largest = l[i]
#         index =i
# print(f"your largest num is {largest} at index {index}")

# l = [ 12,3,2,4,4,42, 16]
# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest 
#         largest = i
#     elif i> sec_largest:   #here the elif condition used when 432 is consider as largest when the sec largest num at the end of the list then the condittion if failed thats why we add this line 
#         sec_largest = i
# print(sec_largest, largest)


# lst = list(map(int, input("Enter numbers: ").split()))
# print(lst)  

# a = (12,3,3243,12313,1,2,2,2,23,334,)
# count =a.count(2)
# print(count)


# a,b,c,d = (1,2,3,4)

# print(type(a))
# immutable in nature 
# duplicate allow 
# set of ordered number can access through index 
# hetrogeneous in nature

# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])


# set 

# a = {1,2,3,4,5,6,2,2,2}
# print(a)
# {1, 2, 3, 4, 5, 6}


# d = {10:20, 22:3,32:22, 212:222,2332:2}
# for i in d.values():
#     print(i)
# print("hellooos,vbfvb")
# for i in d.values():
#     print(i)


# deep copy
# a = [1,2,3,4,5]
# b= a
# b[0]= 100
# print(a)

# shallow copy 
# help()


# d1 = {11:20, 22:30,13:30,14:50}
# d2 = {11:20, 20:22,111:222}

# for i in d2:
#     d1[i]=d2[i]
# print(d1)


# d1 = {11:20, 22:30,13:30,14:50}

# sum = 0
# for i in d1:
#     sum = sum + d1[i]
# print(sum)




# d1 = [1,2,3,3,44,5,6,7,8,3,4,4]
# d={}
# for i in d1 :
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# {1: 1, 2: 1, 3: 3, 44: 1, 5: 1, 6: 1, 7: 1, 8: 1, 4: 2}


# d1= {10:100,20:222,30:2222}
# d2 ={22:22,}

# exceptional handling

# a = int(input("enter the number you want to enter: "))
# try:
#     print(10/a)

# # except ZeroDivisionError:    # now from here u can use another code aswell
# except Exception as err:
#     print("sorry u cannot divide with zero")

# else:       # ye run karega jab no exception hoga 
#     print("good ******there is no exception****** here")

# finally:   #ye humesha chalega chahey error ho chey na ho 
#        print("me to *********humeshha chalunga***** no matter what")
# print("ok ye run ho jayega kyu ki exception handling use hori hai")

# # raise where to use raise 

# age = int(input("tell your age : "))
# try: 
#     if age< 10 or age> 18:
#        raise ValueError("your are must be betweeen 10 to 18")
#     else:
#         print("welcome to the club")

# except Exception as err:
#     print(f"an err occured is {err}")

# print("the club will start soon")

# output :      raise ValueError("your are must be betweeen 10 to 18")
# ValueError: your are must be betweeen 10 to 18


# File handling 
#  CRUD operation 



# p= open(r'main.py')

# print(p.read())

# w = open("superman.txt", 'w')
# w.write("hello bhai ye me direct terminal se likha ra hu")



