# x=5
# y=10
# z=20
# x,y,z=5,10,20
# x,y=y,x
# x=x+5 # x+=5

# print(x,y,z)

values=1, 2, 3, 4, 5
print(values)
print(type(values))
# x, y, z=values # eleman sayısına eşit olmalı ne fazla ne de eksik olmalı
x, y, *z=values
print(x,y,z)