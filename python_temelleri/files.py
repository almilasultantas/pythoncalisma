#Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#Kullanımı: open(dosya_adi,dosya_erisme_modu)
#dosya_erismme_modu=> dosyayı hangi amaçla açtığımızı belirtir.
    # #"w"=> (Write) yazma modu. Dosyayı konumda oluşturur. Dosya içeriğini siler ve yeniden oluşturur.
    # #"a"=> (Append) ekleme modu. Dosyayı konumda yoksa oluşturur.
    # #"x"=> (Create) oluşturma modu. Dosya zaten varsa hata verir.
    # #"r"=> (Read) okuma modu. Varsayılan dosya konumda yoksa hata verir.

#"W"
#py dosyasının bulunduğu klasöre oluşturuyor
# file=open("newfile.txt","w")
# file.close()
#istediğimiz bir adrese klasör oluşturmak için 
# file = open("C:/users/Casper/desktop/newfile.txt", "w")
# file.close()
# file=open("newfile.txt","w", encoding="utf-8")
# file.write("Almıla Sultan TAŞ\n")
# file.close()

# #"A"

# file=open("newfile.txt","a",encoding="utf-8")
# file.write("MehmetAlp Yasin TAŞ\n")
# file.close()

# #"X"

# file=open("newfile2.txt","x",encoding="utf-8")
# file.close()

# #"R"
# try:
#     file =open("newfile3.txt","r") #or file =open("newfile.txt")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı")
#     file.close()

# file=open("newfile.txt", "r", encoding="utf-8")
# # #for föngüsü ile okuma
# # for i in file:
# #     print(i, end="")
# # file.close()

# #read() fonksiyonu ile okuma

# content1=file.read()
# print("İçerik 1")
# print(content1)
# content2=file.read()
# print("İçerik 2")
# print(content2) # bunun tekrar ookunması için klasörün kapatılıp açılması gerek çünkü imleç sonda klıyor bu şekilde
# file.close()

# file=open("newfile.txt", "r", encoding="utf-8")
# content=file.read(5)
# content=file.read(3)
# print(content)
# file.close()

# #readline() komutu

# file=open("newfile.txt", "r", encoding="utf-8")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")

# file.close()


# #readlines() komutu

# file=open("newfile.txt", "r", encoding="utf-8")
# liste=file.readlines()
# print(liste[0])
# print(liste[1])
# print(liste[2])
# print(liste)
# file.close()

# #dosya okumafonksiyonları
# with open("newfile.txt", "r", encoding="utf-8") as file:
#     #file=open("newfile.txt", "r", encoding="utf-8")
#     content=file.read(10)
#     print(content)
#     file.seek(0) #imlecin konumunu değiştiriyoruz
#     #böylece file.close() 'a gerek kalmıyor
#     print(file.tell()) # konum verecek
#     content2=file.read()
#     print(content2)
    
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     #"r+" hem okuma hem de yazma modu demek    
#     file.seek(20)
#     file.write("Denemeğğ")
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     #"r+" hem okuma hem de yazma modu demek    
#     print(file.read())
#Sayfa Sonu Güncelleme
# with open ("newfile.txt", "a", encoding="utf-8") as file:
#     file.write("Ferize TAŞ\n")
# with open("newfile.txt","r",encoding="utf-8") as file:
#     #"r+" hem okuma hem de yazma modu demek    
#     print(file.read())
#Sayfa Başında güncelleme
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content=file.read()
#     content="Emirhan TAŞ\n"+content
#     # print(content)
#     file.seek(0)
#     file.write(content)

#Sayfa Ortasında Güncelleme

# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     list=file.readlines()
#     list.insert(1,"Ferizee TAŞ\n")
#     print(list)
#     file.seek(0)
#     file.writelines(list)
#     # for i in list:
#     #     file.write(i)
# with open("newfile.txt","r",encoding="utf-8") as file:
#     #"r+" hem okuma hem de yazma modu demek    
#     print(file.read())
def nothesapla(satir):
    satir=satir[:-1]
    liste=satir.split(":")
    ogrenciadi=liste[0]
    notlar=liste[1].split(",")
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ortalama=(not1+not2+not3)/3
    if ortalama>=90 and ortalama<=100:
        harf="AA"
    elif ortalama>=85 and ortalama<=89:
        harf="BB"
    elif ortalama>=65:
        harf="CC"
    else:
        harf="FF"
    return ogrenciadi+": "+harf+"\n"

def ortalamarioku():
    with open("sinavnotlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(nothesapla(satir))
        

        

def notgit():
    ad=input("Öğrenci Adını Giriniz: ")
    soyad=input("Öğrenci Soyadını Giriniz: ")
    not1=input("Not 1: ")
    not2=input("Not 2: ")
    not3=input("Not 3: ")

    with open("sinavnotlari.txt", "a", encoding="utf-8") as file:
        file.write(ad+" "+ soyad+" :"+not1+", "+not2+", "+not3+"\n")

def notlarikayitet():
    with open("sinavnotlari.txt", "r", encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(nothesapla(i))
    with open("sonuclar.txt", "w", encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)

#UYGULAMA#
while True:
    islem=input("1-Notları Oku\n2-Not Gir\n3-Notları Kaydet\n4-Çıkış")
    if islem=="1":
        ortalamarioku()
    elif islem=="2":
        notgit()
    elif islem=="3":
        notlarikayitet()
    else:
        break