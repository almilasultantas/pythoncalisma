# def square(num): return num**2=lambda num: num**2
# numbers=[1, 3, 5, 9, 10, 4] 
# result=list (map(lambda num: num**2, numbers))
# print(result)

# for item in map(lambda num: num**2,numbers):
#     print(item)

# square=lambda num: num**2
# print(square(3))

# def check_even(num): return num%2==0
# result=list (filter(check_even,numbers))
# result=list (filter(lambda num: num%2==0,numbers))
# check_even=lambda num: num%2==0
# result=list (filter(check_even,numbers))
# result=check_even(numbers[2])
# print(result)

# #global scope
# x='global x'
# def function():
#     #local scope
#     x='local x'
#     print(x)
# function()
# print(x)

# #global
# name='Çınar'
# def changeName(new_name):
#     #Local
#     name=new_name
#     print(name)
# changeName('Ada')
# print(name)

# name='global string'
# def greeting():
#     # name='Almıla'
#     def hello():
#         # name='Aytöre'
#         print('Hello '+name)

#     hello()
# greeting()

# x=50
# def test(x):
#     print(f'x: {x}')
#     x=100
#     print(f'changed x to {x}')
# test(x)
# print(x)

# x=50
# def test():
#     global x
#     print(f'x: {x}')
#     x=100
#     print(f'changed x to {x}')
# test()
# print(x)

#Bankamatik Uygulaması#
hesapA={
    'Ad':'Almıla Sultan TAŞ',
    'HesapNo':'123456789',
    'Bakiye':4500,
    'EkHesap':5000
}
hesapB={
    'Ad':'Fatıma Aytöre TAŞ',
    'HesapNo':'987654321',
    'Bakiye':3500,
    'EkHesap':6000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['Ad']}")
    if hesap['Bakiye']>=miktar:
        hesap['Bakiye']-=miktar
        print('Paranızı alabilirsiniz.')
    else:
        toplam=hesap['Bakiye']+hesap['EkHesap']
        if toplam>=miktar:
            onay=input('Ek hesap kullanılsın mı? (Y/N)')
            if onay=='Y':
                ekhesapkullanilacakmiktar=miktar-hesap['Bakiye']
                hesap['Bakiye']=0
                hesap['EkHesap']-=ekhesapkullanilacakmiktar
                print('Paranızı alabilirsiniz.')
            else:
                print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} bulunmaktadır.")
        else:
            print('Bakiye yetersiz.')



paraCek(hesapA,6000)
paraCek(hesapA,6000)
print(hesapA['Bakiye'],hesapA['EkHesap'])
#Gönderdiğimiz bilgiler bi obje olduğu için Referans olarak alınıyor bilginin adresi gönderiliyor ve değişim gerçekleşiyor
#değişkenleri fonksiyona göndersek değişimler değişkenler üzerinde etki etmez sadece kopyalama işlemi yapılır.