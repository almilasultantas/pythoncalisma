# name='Almıla Sultan TAŞ'
# for letter in name:
#     if letter=='S':
#         break
#     print(letter)
    
# for letter in name:
#     if letter=='S':
#         continue
#     print(letter)
    
# x=0
# while x<5:
#     if x==2:
#         break
#     print (x)
#     x+=1
# x=0
# while x<5:
#     if x==2:
#         x+=1
#         continue
#     print (x)
#     x+=1
# t=0
# x=1
# while x<=100:
#     if x%2==0:
#         t+=x
#     x+=1
# print(t)

# # loop-operation#


# # range
# for i in range(50,100,10):
#     print(i)
# print(list(range(50,100,20)))

# # enumerate
# #indeks=0
# greeting='Hello'
# for index,l in enumerate(greeting):
#     print(f'letter:{greeting[index]}, indeksi: {index}')

# for i in enumerate(greeting):
#     print(i)

# # zip
# list1=[1, 2, 3, 4, 5]
# list2=['a', 'b', 'c', 'd', 'e']
# print(list(zip(list1,list2)))
# for i in list(zip(list1,list2)):
#     print (i)
# for i,a in list(zip(list1,list2)):
#     print (i)
#     print(i,a)


# list comprehensions
# for x in range (10):
#     print(x)

# numbers=[x for x in range(10)]
# print(numbers)

# for x in range(10):
#     print(x**2)
# numbers=[x**2 for x in range(10)]
# print(numbers)
# numbers=[x*x for x in range(10) if x%3==0]
# print(numbers)

# mystring='Helloo'
# mylist=[]
# for l in mystring:
#     mylist.append(l)
# print(mylist)

# mylist=[l for l in mystring]
# print(mylist)

# years=[1983, 1999, 2008, 1956, 1986]
# ages=[2020-year for year in years]
# print (ages)

# result=[x if x%2==0 else 'Tek' for x in range(1,10)]
# print (result)

# result=[]
# for x in range(3):
#     for y in range(3):
#         result.append((x,y))
# print (result)

# numbers=[(x,y) for x in range(3) for y in range(3)]
# print(numbers)

# random

# import random
# a=random.randint(1,6)
# print(a)
# d=int(input('Kaç tahmin hakkınız olsun?:'))
# c=int(input('Tahmininiz: '))
# puan=100
# while c!=a:
#     puan-=100/d
#     if puan==0:
#         print('Kaybettiniz.')
#         break
#     c=int(input('Tahmininiz: '))
    
# print(f"Puanınız: {puan}")

#Asal sayı kontrolü
sayi=int(input('Bir sayı giriniz: '))
if sayi==1:
    print('1 sayısı asal değildir')
for i in range(2, sayi):
    if sayi%i==0:
        print(f'Girmiş olduğunuz sayı: {sayi} ve asal değildir.')
        break
print(f'Girmiş olduğunuz sayı: {sayi} ve asal sayıdır.')