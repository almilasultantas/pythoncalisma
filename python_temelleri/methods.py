# #method
# list =[1, 2, 3]
# list.append(4)
# list.pop()
# print(type(list))
# print (list)

# mystring='Hello'
# print(mystring.upper())
# print(type(mystring))

# #fonksiyon
# name=input('Lütfen isminizi giriniz: ')
# def sayHello(name='User'):
#     print (f'Hellloğğğğğğ {name}')

# sayHello(name)
# sayHello()
# def yasHesapla(dogumyili):
#     return 2020-dogumyili

# def emekliligeKacYilKaldi(dogumyili, isim):
#     '''
#     DOCSTRING: Dogum yiliniza göre emekliliginize kac yil kaldi
#     INPUT:dogum yili
#     OUT:hesaplanan yil bilgisi
#     '''
#     yas=yasHesapla(dogumyili)
#     emeklilik=65-yas
#     if emeklilik>0:
#         print(f'Emekliliğinize {emeklilik} yıl kaldı.')
#     else:
#         print('Zaten emeklisiniz.')

# emekliligeKacYilKaldi(1998,'Al')
# print(help(emekliligeKacYilKaldi))
# list=[1, 2, 3]
# print(help(list.append))
# def changeName(n):
#     n='Aytöre'
# name='Almıla'
# print(name)
# changeName(name)
# print(name)

# def change(n):
#     n[0]='İstanbul'
# sehirler=['Ankara', 'İzmir']
# change(sehirler)
# change(sehirler[:])
# print(sehirler)
# sehirler=['Ankara', 'İzmir']
# n=sehirler[:] #Listeyi kopyalama adresi değil (Slicing işlemi)
# n[0]='İstanbul'
# print(sehirler,'\n',n)

# def add(a,b,c=0):
#     return sum((a,b,c))
# print(add(10,20))
# print(add(10,20,30))

# def add(*asdf):
#     return sum((asdf))
# print(add(10,20))
# print(add(10,20,30))

# def add(*params):
#     print (params)
#     print (params[0])
#     return sum((params))
# print(add(10,20))
# print(add(10,20,30, 40, 50))
# def displayuser(**args): #iki * dictionary olduğunu belirtiyor
#     for key,value in args.items():
#         print('{} is {} '.format(key,value))

# displayuser(name='Almıla',age=22,city='İstanbul')
# displayuser(name='Aytöre',age=12,city='İstanbul', phone='123654789')
# displayuser(name='Alp',age=5,city='İstanbul', phone='123654789', email='asad@asd')

# def myfunc(a,b,*args,**kwargs):
#     print(a)
#     print(b)    
#     print(args)
#     print(kwargs)
# myfunc(1, 2, 30, 40, 50, key1='value1',key2='value2')

##Uygulama##
# #1
# string=input('Lütfen yazılmasını istediğiniz kelimeyi giriniz: ')
# sayi=int(input('Kaç defa yazdırılmasını istiyorsunuz: '))
# def yazdirma(str,int):
#     while int>0:
#         print(str)
#         int-=1

# yazdirma(string,sayi)

# #2
# def change(*param):
#     return param



# print(change(1, 2, 3, 4, 5, 6, 7))

# print(type(change(1, 2, 3, 4, 5, 6, 7)))

# #or
# def listeyecevir(*param):
#     liste=[]
#     for p in param:
#         liste.append(p)
#     return liste  
    


# print(listeyecevir(10, 20, 33))
 
#3
'''
na1=int(input('Birinci sayıyı giriniz: '))
na2=int(input('İkinci sayıyı giriniz: '))
asalsayilar=[]
def asalmi(n1,n2):
    
    while n1<=n2:
      asalsayilar.append(n1)
      if n1==1: 
            n1+=1
      for i in range(2,n2):
            if n1%i==0:
                asalsayilar.remove(n1)
                break
      
      n1+=1
    print(f'Asal sayılarımız: {asalsayilar}')
asalmi(na1,na2)'''

# sayi1=int(input('1.Sayı: '))
# sayi2=int(input('2.Sayı: '))

# def asalmi(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if (sayi%i==0):
#                     break
#             else:
#                 print(sayi)
# asalmi(sayi1,sayi2)

# #4
# sayi=int(input('Sayı girini: '))
# 20
# def tambolenler(sayi):
#     tambolenler=[]
#     a=1
#     while a<=sayi:
#         if sayi%a==0:
#             tambolenler.append(a)
#         a+=1
#     print (tambolenler)
# tambolenler(sayi)

#Lambda

def square(num): return num **2
numbers=[1, 3, 5, 9]
result=list(map(square, numbers))
print(result)
for i in map(square,numbers):
    print(i)

numbers=[1, 3, 5, 9]
result=list(map(lambda num: num**2, numbers))
print(result)
