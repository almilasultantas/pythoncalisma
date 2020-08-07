fruits={'orange', 'apple', 'banana'}
# print(fruits[0]) İndexlenemez
for x in fruits:
    print(x)
fruits.add('cherry')
fruits.update(['mango', 'grape'])

fruits.remove('apple')

fruits.discard('cherry')
print(fruits)

# # Listede tekrarlayan elemanları düzenlemek için 
# mylist=[1,2,5,4,4,2,1]
# print(mylist)
# mylist=set(mylist)
# print(mylist)
