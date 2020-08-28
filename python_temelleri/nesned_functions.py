# def greeting(name):
#     print("Hello ", name)
# print(greeting("Almıla"))
# print(greeting)

# sayHello=greeting
# print(sayHello)
# print(greeting)

# del sayHello
# #encapsulation
# def outer(num1):
#     print("Outer")
#     def inner_increment(num1):
#         print("Inner")
#         return num1+1
#     num2=inner_increment(num1)
#     print(num1,"=>",num2)
# outer(10)
# #inner_increment(10)=>Hata verir çünkü outer'ın içinde tanımlı


# def fatorial(number):
#     if not isinstance(number,int):
#         raise TypeError("Number must be an integer.")
#     if not number>=0:
#         raise ValueError("Number must be zero or positive.")
#     def inner_factorial(number):
#         if number<=1:
#             return 1
#         return number * inner_factorial(number-1)
#     return inner_factorial(number)
# try:
#     print(fatorial(-2))
# except Exception as ex:
#     print(ex)

#Fonksiyondan fonksiyon döndürme
# def usalma(number):
    

#     def inner(power):
#         return number**power
#     return inner

# two=usalma(2)
# print(two(3))
# three=usalma(3)
# print(three(4))

# def yetki_sorgula(page):
#     def inner(role):
#         if role=="Admin":
#             return "{0} rolünün {1} sayfasına ulaşabilir.".format(role, page)
#         else:
#             return "{0} rolünün {1} sayfasına ulaşamaz.".format(role, page)
#     return inner
# user1=yetki_sorgula("Product Page")
# print(user1("Admin"))
# print(user1("Admi"))


# def islem(islem_adi):
#     def toplam(*args):
#         toplam=0
#         for i in args:
#             toplam+=i
#         return toplam
    
#     def carpma(*args):
#         carpim=1
#         for i in args:
#             carpim*=i
#         return carpim
#     if islem_adi=="toplama":
#         return toplam
#     else:
#         return carpma
# toplam=islem("toplama")
# print(toplam(2, 3, 4))
# carpma=islem("carpma")
# print(carpma(2, 3, 4))

# #functions as parameters

# def toplama(a, b):
#     return a+b
# def cikarma(a,b):
#     return a-b
# def carpma(a,b):
#     return  a*b
# def bolme(a,b):
#     return a/b
# def islem(f1, f2, f3, f4, islem_adi):
#     if islem_adi=="toplama":
#         print(f1(2,3))
#     elif islem_adi=="cikarma":
#         print(f2(5,3))
#     elif islem_adi=="carpma":
#         print(f3(4,3))
#     elif islem_adi=="bölme":
#         print(f4(10,2))
#     else:
#         print("Geçersiz işlem.")
    
# islem(toplama, cikarma, carpma,bolme,"bölmeaa")

# #decorators
# #bir fonksiyona bir özellik eklemek istiyorsak decorator fonksiyon oluşturuyoruz.
# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önce işlemler")
#         func(name)
#         print("Fonksiyondan sonra işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("Hello", name)
# @my_decorator
# def sayGreeting():
#     print("Greeting")

# # sayHello=my_decorator(sayHello)
# sayHello("Almıla")
# # sayGreeting=my_decorator(sayGreeting)
# # sayGreeting()

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)

        func(*args,**kwargs)

        finish=time.time()
        print("Fonksiyon "+func.__name__+" "+ str(finish-start)+" saniye sürdü.")
    return inner
@calculate_time
def usalma(a, b):
    print(math.pow(a, b))
@calculate_time   
def faktoriel(num):
    print(math.factorial(num))
    

usalma(2,3)
faktoriel(4)