# Key=>value

# sehirler=['Kocaeli', 'İstanbul']
# plakalar=[41,34]
# print(plakalar[sehirler.index('Kocaeli')])

# plakalar={'key':'value'}

# plakalar={'Kocaeli':41, 'İstanbul':34}
# print(plakalar)
# print(plakalar['Kocaeli'])

# plakalar['Ankara']=6
# plakalar['Kocaeli']='new value'
# print(plakalar)

users={
    'AlmılaSultanTAŞ':{
        'age':22,
        'email':'almila@gamaiii',
        'address':'İstanbul',
        'phone':'12312131'
    },
    'FatımaAytöreTAŞ':{
        'age':2,
        'email':'aytore@gamaiii',
        'address':'İstanbul',
        'phone':'+9897465498'
    }
}

print(users['AlmılaSultanTAŞ'])
print(users['AlmılaSultanTAŞ']['age'])
