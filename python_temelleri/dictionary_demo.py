students={}
number=input('Öğrenci no: ')
name=input('Öğrenci adı: ')
surname=input('Öğrenci soyad: ')
phone=input('Öğrenci telefon: ')

# students[number]={
#     'Ad:':name,
#     'Soyad: ':surname,
#     'Telefon: ':phone
# }

students.update({
    number:{
        'Ad:':name,
        'Soyad: ':surname,
        'Telefon: ':phone
    }
})

print(students)