# #username, password=> database

# a, b, c, d=5, 5, 10, 4

# result= a==b
# result= a==c
# result= a!=b
# result= a>b
# print(result)


####### Deneme kısmııı #####
# #1
# a=int(input('İlk sayıyı giriniz: '))
# b=int(input('İkinci sayıyı giriniz: '))
# sonuc= (a>b)
# print(f'ils sayı:{a} ikinci sayı: {b} den büyüktür: {sonuc}')
# #2 
# vize1=int(input('Vize 1 notunuz: '))
# vize2=int(input('Vize 2 notunuz: '))
# final=int(input('Final notunuz: '))

# ortalama=((((vize1+vize2)/2)*60)/100)+ ((final*40)/100)
# durum=(ortalama>=50)
# tf=['Kaldınız', 'Geçtiniz']
# print(f'Ortalamanız: {ortalama} Dersten {tf[durum]}')

# #3
# sayi=int(input('Sayı giriniz: '))
# durumu=sayi%2
# sorgu=(durumu==0)
# sayid=['tek sayıdır.', 'çift sayıdır.']
# print(f'Sayımız {sayid[sorgu]}')

# #4
# sayi=int(input('Sayı giriniz: '))
# sorgu=((sayi>=0))
# durumu=['negatiftir.', 'pozitiftir.']
# print(f'Sayımız {durumu[sorgu]}')

#5
email='asdfg'
password='12'
gemail=str(input('Lütfen mail aderesiniz giriniz: '))
gpassword=str(input('Lütfen şifrenizi giriniz: '))

kemail=email==gemail
kpassword=password==gpassword

demail=['Girdiğiniz e-mail bulunmamaktadır.','']

dpassword=['Girdiğiniz şifre yanlıştır.', 'Girişiniz gerçekleştiriliyor.']

print(demail[kemail],dpassword[kpassword])