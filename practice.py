# n = 5
# r = 1

# for i in range(1,n+1):
#     r *= i
# print(r)


# n = 5
# r = 1
# sum = 0

# while(r<=n):
   
#     r += 1
#     sum += r
#     print(sum)


# n = 5
# r =0
# i = 1
# while(i<= n):
#     i += 1
#     r += i
# print(r)


# try:
#     b=10
#     c= 10
#     a = b/c
#     print(a)
# except:
#     print("error")
   
   
# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1 
#     return factorial(n-1) * n
    
# print(factorial(5))


# def sum(n):
#     if(n == 0):
#         return
#     print(n)
    
#     sum(n - 1)
    
# sum(6)


# def even(n):
#     if(n == 0):
#         return
#     print(n)
#     even(n-2)
    
# even(10)


# i = 0

# while(i <= 5):
#     print("Hello",i)
#     i += 1


# i = 5
# while(i >= 1):
#     print(i)
#     i = i - 1
    
# list = ["amir", "khan", "shahruk", "dubai ", "mumbai", "euripe"]

# i = 0

# while(i < len(list)):
#     print(list[i],i)
#     i += 1
 
 
# tuple1 = (1,4,9,16,25,36,49,64,81,100)

# x = 81

# i = 0

# while( i < len(tuple1)):
#     if(tuple1[i] == x):
#         print("the number is been found AT index ",i)
#     i +=1

    


# i = 1




# n = 3

# while(i <= 10):
#     print(n * i)
#     i +=1


# list = [1,4,9,16,25,36,49,64,81,100]
# x = 49
# i = 0
# for el in list:
#     if(el == x):
#         print("Found", el , "At index",i )
#         break
#     i += 1



# for i in range (2,100,2):
#     print(i)


# for i in range(1,101):
#     print(i)
    
# n = 9

# for i in range(1,11):
#     print(i * n)


# i = 1
# n = 0
# while(i <= 5):
#     n = n + i
#     i = i + 1
    
# print(n)

# n = 1

# for i in range(1,6):
#     n = n * i 
# print(n)


# n = 1
# i = 1

# while( i <= 5):
#     n = n * i
#     i += 1
# print(n)

# for i in range( 1,11):
#     print("*"*i)

#-------------Q1 Factorial with Loop: Write a program that takes a number n and calculates its factorial using a for loop.<-----------
# i = 1
# n = 5

# for i in range(1,n):
#     n *= i
# print(n)

#------------------>Q2 Count Even and Odd Numbers: Write a program that takes a list of numbers and counts how many are even and how many are odd using a loop.<------------
# list = [1,3,5,7,9,2,4,6,8,10]
# idx = 0
# for i in list:
#     a = (i%2 == 0)
#     if(a == True):
#         print("There are even number", i)
#     if( a== False):
#         print("These are odd number", i )
#     idx += 1
    
#------------>Q3 Count Even and Odd Numbers: Write a program that takes a list of numbers and counts how many are even and how many are odd using a loop.<-----------



# st = "khanbaba"

# i = 7

# while(i >= 0):
#     print(st[i])
#     i -=1
    


# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O")
#     f.write("\nusing Java.\nI like programming in Java.")
    

# with open("practice.txt","r") as f:
#     data = f.read()
#     new_data = data.replace("Java","Python")
#     print(new_data)
    
# with open("practice.txt","w") as f:
#     f.write(new_data)

# def finding_data():
#     i = 0
#     with open("practice.txt","r") as f:
#         data = f.read()
       
#         if(data.find("learning") != -1):
#             print("Found",i) 
#         i += 1  
                
# finding_data()     


# def finding_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#             else:
#                 print(-1)
#             line_no +=1
            
# finding_line()
                
                
# def number():
#     with open("practice.txt","r") as f:
#         data = f.read()
#         new_data = data.split(",")
#         for i in new_data:
#             if(int(i) % 2 == 0):
#                 print("Even")
#             else:
#                 print("Odd")
            
# number()


# def numbers():
#     with open("practice.txt","r") as f:
#         data = f.read()
#         num = ""
#         for i in range(len(data)):
#             if(data[i] == ","):
#                 print(int(num))
#                 num = ""
#             else:
#                 num += data[i]
# numbers()        
                
# def number():
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         num = data.split(",")
#         for i in num:
#             if(int(i)%2 == 0):
#                 print("Even")
#             else:
#                 print("Odd")

# number()


# def finding_hello():
#     word = "Hello"
#     idx = 1
#     with open("practice.txt","r") as f:
#         data = f.read()
#         words = data.split()
#         for w in words:
#             if(w == word):
#                 print(w)
#                 idx +=1
#     print("the word hello is printed", idx,"times")
            
            
# finding_hello()
        
        
        
        
        
# def finding():
#     i = 1
#     find_the_word = "Hello"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         words = data.split()
        
#         for w in words:
#             if w == find_the_word:
#                 print(w)
#                 i += 1
#         print("The word ",w,"Is find ",i,"times")    
# finding()




# with open("practice.txt","r") as f:
#     data = f.read()
#     new_data = data.replace("in","im")
#     print(new_data)
    
# with open("practice.txt","w") as f:
#     f.write(new_data) 

class Student:
    def __init__(self,name,marks,fee_status):
        self.name = name
        self.marks = marks
        self.fee_status = fee_status
        
        
s1 = Student("jan",91,"Paid")
s2 = Student("Kani",53,"Unpaid")
s3 = Student("Pullo",99,"Paid")

print(s1.name,"marks are",s1.marks,"fee are",s1.fee_status)  
print(s2.name,s2.marks,s2.fee_status)
print(s1.name,s3.marks,s3.fee_status)
  
marks = [101,111,222]
sum = 0

for numbers in marks:
    sum = sum + numbers
print(sum)




class Student:
    def __init__(self,name):
        self.name = name
    @staticmethod  #decorator   ("Decorators allow us to wrap another function in order to ectend the behaviour of the wrapped function ,without permanently modifying it")
    def college():
        print("ABC College")
    
s1 = Student("babu")

print(s1.name)

        
