# liste=[1, 2, 3, 4, 5]
# iterator= iter(liste)
# print (iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))


# for i in liste:
#     print(i)

# iterator=iter(liste)
# while True:
#     try:
#         element=next(iterator)
#         print(element)
#     except StopIteration:
#         break

# # class Numberr:
# #     def __init__(self,start,stop):
# #         self.start=start
# #         self.stop=stop
# #     def __iter__(self):
# #         return self
# #     def ___next__(self):
# #         if self.start<=self.stop:
# #             x=self.start
# #             self.start+=1
# #             return x
# #         else:
# #             raise StopIteration
# # liste=Numberr(10,20)
# # print(list(liste))

# # for x in liste:
# #     print(x)
# #     def __init__(self, start, stop):
# #         self.start=start
# #         self.stop=stop

# #     def __iter__(self):
# #         return self
        
# #     def ___next__(self):
# #         if self.start<=self.stop:
# #             x=self.start
# #             self.start+=1
# #             return x
# #         else:
# #             raise StopIteration


# # liste=MyNumbers(10, 20)

# # myiter=iter(liste)
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # # for x in liste:
# # #     print(x)


# class MYNUMBERS:
#     def __init__(self,start,stop):
#         self.start=start
#         self.stop=stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start<=self.stop:
#             x=self.start
#             self.start+=1
#             return x
#         else:
#             raise StopIteration
# alist=MYNUMBERS(10,15)
# # for x in alist:
# #     print(x)
# myiter=iter(alist)
# while True:
#     try:
#         element=next(myiter)
#         print(element)
#     except StopIteration:
#         break

#generators

# def cube():
    
#     for i in range(5):
#         yield i**3

# # generator=cube()
# # iterator=iter(generator)
# iterator=cube()
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))

# for i in iterator:
#     print(i)

liste=[i**3 for i in range(5)]
print(liste)
#yukarıdakini generator yapmak istiyorsak:
liste=(i**3 for i in range(5))#generator oldu
print(liste)

for i in liste:
    print(i)