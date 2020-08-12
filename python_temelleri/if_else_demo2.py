# #1
# number=float(input('Sayı: '))
# result=0<number<100
# if result:
#     print(f'Sayımız: {number} ve 0 ile 100 arasındadır.')
# else:
#     print(f'Sayımız: {number} ve 0 ile 100 arasında değildir.')

# #2
# number=int(input('Sayı: '))
# result=(number>0) and (number%2==0)
# if result:
#     print(f'Sayımız: {number} ve pozitif çift sayıdır.')
# elif (number<0) and (number%2==0):
#     print(f'Sayımız: {number} ve negatif çift sayıdır.')
# elif (number>0) and (number%2!=0):
#     print(f'Sayımız: {number} ve pozitif tek sayıdır.')
# elif (number<0) and (number%2!=0):
#     print(f'Sayımız: {number} ve negatif tek sayıdır.')

# #3
# email='asd'
# password='123'
# iemail=input('Mailiniz: ')
# ipassword=input('Şifreniz: ')
# if email!=iemail:
#     print('Lütfen giriş bilgilerinizi kontrol ediniz.')
# else:
#     if password==ipassword:
#         print ('Girişiniz başarıyla gerçekleşti.')
#     else:
#         print('Lütfen şifrenizi kontrol ediniz.')

# #4
# a=int(input('A sayısı: '))
# b=int(input('B sayısı: '))
# c=int(input('C sayısı: '))
# if(a==b or b==c or a==c):
#     print('Sayılarda eşitlik var')
# if (a>b and a>c):
#     if b>c:
#         print('A>B>C')
#     else:
#         print('A>C>B')
# if (b>a and b>c):
#     if a>c:
#         print('B>A>C')
#     else:
#         print('B>C>A')
# if (c>a and c>b):
#     if a>b:
#         print('C>A>B')
#     else:
#         print('C>B>A')

# #5
# vize1=int(input('Vize 1 notunuz: '))
# vize2=int(input('Vize 2 notunuz: '))
# final=int(input('Final notunuz: '))

# ortalama=((((vize1+vize2)/2)*60)/100)+ ((final*40)/100)
# durum=((ortalama>=50) and (final>=50)) or (final>=70)
# if durum:
#     print(f'Ortalamanız: {ortalama} ve geçme durumunuz başarılı.')
# else:
#     print(f'Ortalamanız: {ortalama} ve geçme durumunuz başarısız.')

# #6
# ad=input('Lütfen adınızı giriniz: ')
# kilo=float(input('Lütfen kilonuzu giriniz:'))
# boy=float(input('Lütfen boyunuzu giriniz:'))
# form=kilo/(boy**2)
# print(form)
# if 0<form<=18.4:
#     print(f'Kilo indeksiniz: {form} ve şişko kategorisindesiniz.')
# elif 18.5<=form<=24.9:
#     print(f'Kilo indeksiniz: {form} ve şişko kategorisindesiniz.')
# elif 25<=form<=29.9:
#     print(f'Kilo indeksiniz: {form} ve şişko kategorisindesiniz.')
# elif 30<=form<=34.9:
#     print(f'Kilo indeksiniz: {form} ve şişko kategorisindesiniz.')