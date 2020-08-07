# # value types=>string, number
# x=5
# y=25
# x=y
# y=10
# print (x,y)

# # reference type=>list,class
a=['apple', 'banana']
b=["apple", "banana"]
a=b #ikiside aynı adrese sahip oluyor

b[0]='grape'

print(a,b)
