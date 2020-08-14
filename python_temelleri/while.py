# # 1'den 100'e kadar

# x=1
# while x<=100:
#     if x%2==0:
#         print(x)
#     x+=1

# name='' #false
# while not name.strip(): #true
#     name=input('isminizi giriniz: ')

# print (f'Merhaba {name} ')

#UYGULAMA#

sayilar=[1, 3, 5, 7, 9, 12, 19, 21]

# #1
# x=0
# while x<len(sayilar):
#     print(sayilar[x]) 
#     x+=1

# #2
# strt=int(input('Başlangıç değerini giriniz: '))
# fnsh=int(input('Bitiş değerini giriniz: '))
# while fnsh>len(sayilar):
#     fnsh=int(input(f'Lütfen bitiş değerini tekrar giriniz; \nEn yüksek değer {len(sayilar)} olmalıdır:'))

# while strt<=fnsh:
#     if (sayilar[strt-1]%2==1):
#         print(sayilar[strt-1])
#     strt+=1

# #3
# a=100
# while a>0:
#     print(a)
#     a-=1

# #4
# a=[]
# b=0
# while b<5:
#     a.append(int(input('Bir Sayı Giriniz: ')))
#     b+=1
# print(a)
# a.sort()
# print (a)

#5
urun=[]
adet=int(input('Kaç ürün ekleyeceksiniz?: '))
while (adet>0):
    name=input('Ürün ismi: ')
    price=input('Ürün fiyatı:')
    urun.append({
        'name: ': name,
        'price: ':price
    })
    adet-=1

for u in urun:
    print(f"Ürün adı: {u['name: ']} Ürün fiyatı: {u['price: ']}")


