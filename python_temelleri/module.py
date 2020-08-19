# # #Math modülü
# #Yöntem 1
# # # import math
# # import math as islem #yeniden isimlendirdik gibi
# # # value=dir(math)
# # # value=help(math)
# # # value=(help(math.pow))
# # # value=math.sqrt(25)
# # # value=math.factorial(5)
# # value=islem.factorial(5)
# # print(value)

# #Yöntem 2

# # from math import *
# from math import factorial,sqrt
# value=sqrt(9)
# print(value)
# value=factorial(5)
# print(value)

#Random module
import random
# result=dir(random)
# print(result)
# result=help(random)
# print(result)
# result=random.random() #0.0 ile 1.0 arasında bir sayı üretecek
# print(result)
# result=random.uniform(1,10)
# print(result)
# result=int(random.uniform(1,10))
# result=random.randint(1,100)
# print(result)

# names=['Almıla', 'Aytöre', 'Alp', 'Sultan', 'Fatıma', 'Mehmet']
# # result=random.randint(0,(len(names)-1))
# result=random.choice(names)
# greeting='Hello there'
# result=random.choice(greeting)
# liste=list(range(10))
# random.shuffle(liste)
# print(liste)
# print(result)
# # print(names[result])

# liste=range(100)
# result=random.sample(liste,3)
# print(result)

#Kendi Modülümüzü oluşturma

'''
    modüle hakkında bilgilendirme
'''
print('Modül eklendi!')
number=10
numbers=[1, 2, 3]
person ={
    "name":"Almıla",
    "age":"22",
    "city":"İstanbul"
}
def func(x):
    '''
    fuction hakkında bilgilendirme
    '''
    print(f'x: {x}')

class Person:
    def speak(self):
        print('I am speking')

        #main oluştur ve sonrasında import et bunu ve çalıştırdığında modülün yüklendiğini göreceksin
        #help komutunu yazdırarakta modülün ne işe yaradığını öğrenebilirsin 
        #
