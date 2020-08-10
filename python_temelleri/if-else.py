# if 3>2:
#     print('Hoş Geldiniz')
# else:
#     print('Güle güle')

# x=20
# y=20
# if x>y:
#     print('x y den büyük')
# elif x==y:
#     print('x y eşit')
# else:
#     print('y x den büyük')

# num =int(input('Sayı:'))
# if num>0:
#     print('Sayı pozitiftir.')
# elif num<0:
#     print('Sayı negatiftir.')
# else:
#     print('Sayı sıfırdır.')

# #1 
# name=input('Lütfen ad-soyad giriniz: ')
# age=int(input('Lütfen yaşınızı giriniz: '))
# education=int(input("Eğitim durumunuz nedir? \nİlkokul mezunu iseniz 1'e \nOrtaokul mezunu iseniz 2'ye\nLise mezunu iseniz 3'e\nÜniversite mezunu ya da öğrencisi iseniz 4'e basınız."))
# if (age>=18) and (education>=3):
#     print(f'Sayın {name } ehliyet alabilirsiniz.')
# else:
#     print(f'Sayın {name} ehliyet alamazsınız.')

# #2
# exam1=float(input('İlk yazılınızın sonucu: '))
# exam2=float(input('İkinci yazılınızın sonucu: '))
# quiz=float(input('Sözlü sonucu: '))
# ortalama=(exam1+exam2+quiz)/3
# print('Ortalamanız:',ortalama)
# if (0<=ortalama<=24 ):
#     print(f'Not bilginiz: 0')
# elif (25<=ortalama<=44 ):
#     print(f'Not bilginiz: 1')
# elif (45<=ortalama<=54 ):
#     print(f'Not bilginiz: 2')
# elif (55<=ortalama<=69 ):
#     print(f'Not bilginiz: 3')
# elif (70<=ortalama<=84 ):
#     print(f'Not bilginiz: 4')
# else:
#     print(f'Not bilginiz: 5')

# #3
# days=int(input('aracınız kaç gündür trafikte: '))
# if days<=365:
#     print('1.servis aralığı.')
# elif 365<=days<=365*2:
#     print('2.servis aralığı.')
# elif 365*2<=days<=365*3:
#     print('3.servis aralığı.')
# else:
#     print('Hatalı süre.')

###Datetime kullanımlı

import datetime

tarih=input('Bakım tarihinizi yıl/ay/gün şeklinde giriniz:')
tarih=tarih.split('/')
ttarih=datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi=datetime.datetime.now()
farks=simdi-ttarih
fark=farks.days
print(fark)
if fark<=365:
    print('1.servis aralığı.')
elif 365<=fark<=365*2:
    print('2.servis aralığı.')
elif 365*2<=fark<=365*3:
    print('3.servis aralığı.')
else:
    print('Hatalı süre.')