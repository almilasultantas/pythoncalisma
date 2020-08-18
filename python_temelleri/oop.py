# # #opject oriented programming(oop)
# # #class
# # #instance(object) lst burada instance/object
# # lst=[1, 2, 3]
# # result=type(lst)
# # print(result)


# #class tanımlama
# class Person:
#     # pass#hata vermemesini sağlıyor içi boşken
#     #class attributes
#     adress='no information'
#     #constructor(yapıcı metod)
#     def __init__(self,name, year):#self classtan üretilen herhangi bir objeyi temsil eder 
#         #self kelimesi yerine başka bir şey ayzılabilir?????
#         #oluşturulan her bir obje için çalışır
#         #object attributes
#         self.name=name
#         self.year=year
#         # print('İnit methodu çalıştı')
#     #instance methods
#     def intro(self):
#         print(f'Hello there I am {self.name}')
#     #instance methods
#     def calculeteAge(self):
#         return 2020-self.year
# #object(instance)
# p1=Person('Almıla', 1998)
# p2=Person('Aytöre',2007)
# #updating
# p1.name='Alp'
# p1.adress='İstanbul'
# #accessing object properties/attributes
# print(f'P1 için name: {p1.name} year:{p1.year} adress:{p1.adress}')
# print(f'P2 için name: {p2.name} year:{p2.year} adress:{p2.adress}')
# # print(p1)
# # print(p2)
# # print(type(p1))
# # print(type(p2))
# p1.intro()
# print(p1.calculeteAge())
# p2.intro()
# print(p2.calculeteAge())

# class Circle:
#     #Class object attribute
#     pi=3.14
#     def __init__(self, yaricap=1):
#         self.yaricap=yaricap
#     #methods
#     def cevre_hesapla(self):
#         return 2* self.pi*self.yaricap
#     def alan_hesapla(self):
#         return self.pi*(self.yaricap**2)
# c1=Circle()#yariçap=1
# c2=Circle(5)
# print(f'c1: alan= {c1.alan_hesapla()} ve çevre= {c1.cevre_hesapla()}')
# print(f'c2: alan= {c2.alan_hesapla()} ve çevre= {c2.cevre_hesapla()}')

#Inheritance(Kalıtım): Miras alma

# class Person():
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#         print('Person Created')
#     def who_am_i(self):
#         print('I am a person')
#     def eat(self):
#         print('I am eating')
# class Student(Person):#Persondan kalıtım aldık
#     def __init__(self,fname,lname, number):
#         self.studentnumber=number
#         Person.__init__(self,fname,lname)
#         print('Student Created')
#     #override
#     def who_am_i(self):
#         print('I am a student')
# class Teacher(Person):
#     def __init__(self,fname,lname,branch):
#         super().__init__(fname, lname)#burada selfi göndermemize gerek kalmıyor
#         self.branch=branch
#     def who_am_i(self):
#         print(f'I am a {self.branch} teacher')

# t1=Teacher('Alp','TAŞ','Math')
# print(t1.firstname+' '+t1.lastname+' '+t1.branch)  
# t1.who_am_i()
# p1=Person('Almıla','TAŞ')
# s1=Student('Aytöre', 'TAŞ', 123456)
# print(p1.firstname+' '+p1.lastname)
# print(s1.firstname+' '+s1.lastname +' '+ str(s1.studentnumber))
# p1.who_am_i()
# s1.who_am_i()
# p1.eat()
# s1.eat()

#ÖZEL METOTLAR#
# mylist=[1, 2, 3] 
# mystring='My string'
# print(len(mylist))
# print(len(mystring))

# class Movie():
#     def __init__(self, title, direction, duration):
#         self.title=title #set ediyoruz
#         self.direction=direction
#         self.duration=duration
#         print('Movie objesi oluşturuldu!')
#     def __str__(self):
#         return f"{self.title} by {self.direction}"
#     def __len__(self):
#         return self.duration
#     def __del__ (self):
#         print('Film objesi silindi.')
# m=Movie('Film adı', 'Yönetmen adı', 120)

# print(m)
# print(str(m))
# # print(len(str(m)))
# print(len(m))

# del m
# print(m)
#Uygulamaaa###
#Question
class Question:
    def __init__(self, text,choices, answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer

#Quiz 

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayquestion(self):
        question=self.getQuestion()
        print(f'Soru{self.questionIndex+1}:{question.text}')
        for q in question.choices:
            print('-'+q)
        answer=input('Cevap: ')
        self.guess(answer)
        self.loadQuestion()
    def guess(self, answer):
        question=self.getQuestion()
        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1
        
        
    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayquestion()
    def showScore(self):
        print(self.score)

q1=Question('En iyi programlama dili hangisidir?',['C#', 'Python','JavaScript', 'Java'], 'Python')
q2=Question('En popüler programlama dili hangisidir?',['JavaScript', 'C#', 'Python', 'Java'], 'Python')
q3=Question('En çok kazandıran programlama dili hangisidir?',['C#',  'Java', 'Python','JavaScript'], 'Python')
# print(q1.checkAnswer('Python'))
# print(q2.checkAnswer('C#'))
# print(q3.checkAnswer('Python'))
questions=[q1, q2, q3]
quiz=Quiz(questions)
# # question=quiz.questions[quiz.questionIndex]
# question=quiz.getQuestion()
# print(question)
# print(question.text)
quiz.displayquestion()