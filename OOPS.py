#CLASS AND OBJECT IN PYTHON
#class is a blue print of creating object
#Frist create class and then create object

#class created
# class Student:
#     name = "Desho"
    
#Object created
# s1 = Student()
# print(s1.name)



#    __init__Function(constructor)
#All classes have a function called__init_(),Which is always executed when the object is beiong initiated.
#The (Self) parameter is a reference to the current 
#creating object and class using constructor



#creating class    <                         
# class Student:                              
#     def __init__(self,name,marks):            
#         self.name = name
#         self.marks = marks
#         print("adding new student to Database")
        
        
#creating object<
# s1 = Student("Desho",99)
# print(s1.name,s1.marks)

# s2 = Student("baba",49)
# print(s2.name,s2.marks)


#(default constructor)
# def __init__(self):
#     pass



# ---------------> MADE class and object <---------------

# class Student:
#     def __init__(self,name,marks,fee_status):
#         self.name = name
#         self.marks = marks     #self is mean that every object will have there own value
#         self.fee_status = fee_status
        
        
# s1 = Student("jan",91,"Paid")
# s2 = Student("Kani",53,"Unpaid")
# s3 = Student("Pullo",99,"Paid")

# print(s1.name,"marks are",s1.marks,"fee are",s1.fee_status)  
# print(s2.name,s2.marks,s2.fee_status)
# print(s1.name,s3.marks,s3.fee_status)


               #class and instance Attributes
#____--->if i have to have the college name which is same for every student i will not save it in the constructor i will do it before the constructor

# class Student:
#     collage_name = "Atta shad degree college"
#     def __init__(self,name,marks,fee_status):
#         self.name = name  #obj attr > class attr
#         self.marks = marks
#         self.fee_status = fee_status

# s1 = Student("bahi",101,"Paid")
# s2 = Student("jani",111,"Unpaid")
# s3 = Student("kashi",999,"Unpaid")

# print(s1.collage_name,s1.name,s1.marks,s1.fee_status)
# print(s3.collage_name)



# #                    Mehtods: Method are functions that belong to Object

# #creationg class and mehtod

# class Student:   
#     college_name = "Degree college"        #<-------Class Attributes
#     def __init__(self,name):
#         self.name = name
#     def hello(self):    #<------method  non static
#         print("hello",self.name)          #<------methon
        
# s1 = Student("Kali")       #<-------object
# s1.hello()                 #<------Object



# #------------>Q: Create student class that takes name & marks of 3subjects as arguments in constructor.    Then create a mehtod to print the average.

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def average(self):     #<----Mehtod "non static"
#         sum = 0                 #Mehtod
#         for numbers in self.marks:          #Mehtod
#             sum += numbers              #Mehtod
#             average = sum/len(self.marks)           #Mehtod
#         print("The average marks of ", self.name, "are",average )      #Mehtod

# s1 = Student("ali",[100,50,80])
# s1.name = "pullo"            #we can also change the name of attributes 


# s2 = Student("shahoo",[100,99,123,321,200])
# s1.average()

# s2.average()




# --------------------> "static Mehtod: Mehtods that don't use the self pararmeter(work at class level)" <-------------------------

# class Student:
#     def __init__(self,name):
#         self.name = name
#     @staticmethod   #<---(Static Mehtod) >>decorator<<  ("Decorators allow us to wrap another function in order to ectend the behaviour of the wrapped function ,without permanently modifying it")
#     def college():
#         print("ABC College",s1.name)
    
# s1 = Student("babu")

# s1.college()

        

# ---------------> Important:"Abstraction"  , "Encapsulation" , "Inheritance" , "Polymorphism"<-------
#                             These are the four pillar of oops that oops is standing on

# Abstraction:Hidden the implementation details of a class and only showing the essential features to the user.  OR hiding the unnessicery details and showing the usefull details
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.acc = True
#         self.clutch = True
#         print("Start ")
        
# s1 = Car()
# s1.start()  #its hidding unnecessary details


# Encapsulation: Wrapping data and functions into a single unit(abject).


# ------->Q: Create Account class with 2 attributes - balance & account no.
# ------->Create methods for dabit,credit & printing the balance

class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
    
    def debit(self,amount):
        self.balance -= amount
        print("Rs." ,amount,"was debited from your acc")
        print("The total balance is Rs." ,self.show_balance())
        
    def credit(self,amount):
        self.balance += amount
        print("Rs." , amount,"was cradit to your acc")
        print("The total amount is Rs." , self.show_balance())
        
    def show_balance(self):
        return self.balance
    

a1 = Account(10000, 12345)    

a1.debit(1000)
a1.credit(200)