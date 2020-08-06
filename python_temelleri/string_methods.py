message='Hello There. My name is Almıla Sultan TAŞ'
#message=message.upper() #metindeki tüm harfleri büyük yazıyor.
#message=message.lower() #metindeki harfleri küçük yazıyor.
#message=message.title() #metindeki baş harfleri büyük yazıyor.
#message=message.capitalize() #metindeki sadece ilk harfi büyük yapıyor.
#message= message.strip() #metinin başında ve sonunda boşluk varsa onu almamak için kullanıyo0ruz.
#message=message.split() #bütün hepsini(boşluklardan ayırdı) tırnak içide ayrı ayrı almasını sağlıyor. dizi haline getiriyor.
#message=message.split('.') #noktalardan ayırdı
#print(message[1])
#message='***'.join(message)
#index=message.find('Almıla')
#index=message.rfind('Almıla') #sağdan saydırma
#isfound=message.startswith('H')
#isfound=message.endswith('Ş')
#message=message.replace('Almıla Sultan','Fatıma Aytöreee') içindeki kelimeyi değştirir
#message=message.replace('Almıla','Fatıma').replace('Sultan','Aytöree')
#print (isfound)
#adet=website.count('a') # içinde kaç adet olduğunu veriyor
#adet=website.count('a',0,10) # karakter aralığında arama
#print(index)
#message=message.center(50) #metinin belirlenen karakter sayısı arasında ortalar
message=message.center(50,'*')
message=message.ljust(50,'*')
message=message.rjust(50,'*')
print(message)

