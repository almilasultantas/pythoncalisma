# error=>Hata
# print(a)=>name error
# int('1a2')=>Value error
# print(10/0)=>zero division error
# print('denem'e=>)SyntaxError

# while True:

#     # error handling=> hata yönetimi
#     try:
#         x=int(input('x: '))
#         y=int(input('y: '))
#         print(x/y)
# #   except ZeroDivisionError:
# #       print('Y için 0 girilemez.')
# #   except ValueError:
# #       print('X ve Y için sayısal değer girmelisiniz.')
# #   except (ZeroDivisionError, ValueError) as e:
# #       print('Yanlış değer girdiniz')
# #       print(e) 
# #       #   #hatanın türünü görebiliyoruz
#     except:
#         print('Yanlış değer girdiniz.')
#         #hatanın türüne ulaşamıyoruz burada
#     else:
#         # print('Her şey yolunda')
#         break

# #Raising an Exception
# x=10
# if x>5:
#     raise Exception("x 5'ten büyük değer alamaz")

# def check_pasword(psw):
#     import re
#     if len(psw)<8:
#         raise Exception("Parola en az 8 karakter olmalıdır.")
#     elif not re.search ("[a-z]", psw):
#         raise Exception("Parolanız küçük harf içermelidir.")
#     elif not re.search ("[A-Z]", psw):
#         raise Exception("Parolanız büyük harf içermelidir.")
#     elif not re.search ("[0-9]", psw):
#         raise Exception("Parolanız rakam içermelidir.")
#     elif re.search("\s",psw):
#         raise Exception("Parola boşluk içermemelidir.")
#     else: 
#         print("Parola geçerli")
# password="aX12345678"
# try:
#     check_pasword(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Geçerli parola: ", password)
# finally:
#     print("Validation tamamlandı")

# class Person:
#     def __init__(self, name, year):
#         if len(name)>10:
#             raise Exception("Name alanı fazla karakter içeriyor.")
#         else:
#             self.name=name

# p= Person("Almıla Sultan",1998)

###Uygulama###
liste=["1", "2", "5a", "10b", "abc", "10","50"]

#1
for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue

# #2

# while True:
#     try:
#         result=input("Çıkmak istiyorsanız'q' tuşuna basınız.\nLütfen bi sayı giriniz: ")
#         print(int(result))
#     except ValueError:
#         if result=="q":
#             break
#         else:
#             print("Yanlış değer girdiniz.")
#             continue

# #3
# karakter=["ç", "ğ", "ı", "ö", "ş", "ü", "İ"]
# password=input("Parolanızı giriniz: ")
# for i in password:
#     for z in karakter:
#         if i==z:
#             # print("Parolanız Türkçe karakter barındıramaz.")
#              raise TypeError("Parola Türkçe karakter içermez.")

# #or# bu direkt hata olarak yazdırıyor
# karakter="şçğüöıİ"
# password=input("Parolanızı giriniz: ")
# for i in password:
#     if i in karakter:
#         raise TypeError("Parola Türkçe karakter içermez.")
#     else:
#         pass


#4

def faktoriel(x):
    x =int(x)
    if x<0:
        raise ValueError('Negatif değer.')

    result=1
    for i in range(1,x+1):
        result=result*i
    return result

# print(faktoriel(-3))

for x in [5, 10, 20, -3, "10a"]:
    try :
        y=faktoriel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)