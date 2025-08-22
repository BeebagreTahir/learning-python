#-------------------------- While loop --------------------------

# i = 1
# n = int(input("enter a number for multiplication:"))
# while(i <= 10):
#     print(n *i)
#     i += 1


#print the elements of the following list using a loop:

# list = [1,4,9,16,36,49,64,81,100]
# i = 0 
# while(i < len(list)):
#     print(list[i])
#     i += 1



# heros = ["iron man" , "spider man", "Thor"]
# idx = 0
# while (idx < len(heros)):
#     print(heros[idx] , idx)
#     idx += 1



#Search for a single number in this tupple using loop:

# tuple = (1,4,9,16,25,36,49,81,100)
# x = 100
# i = 0
# while(i < len(tuple)):
#     if(tuple[i] == x):
#         print("Found at index " ,i,"and the number is ",tuple[i])
#     i += 1


#> Contnue in loop mean skip the next step <

# i = 1
# while (i <= 10):                #to print odd numbers
#     if(i%2 == 0):
#         i += 1
#         continue # skip
#     print(i)
#     i +=1


# i = 1
# while (i <= 10 ):
#     if(i%2 != 0):         # to print even numbers
#         i += 1
#         continue
#     print(i)
#     i +=1



#continue means skip
  
  
#----------------for loop.../-------------------


# list = [1,4,9,16,25,36,49,81,100]
# i = 0
# for numbers in list: 
#     print(numbers)
    

# tuple = (1,4,9,16,25,36,49,81,100)
# i = 0
# x = 81
# for numbers in tuple:
#     if(numbers == x):
#         print("number found", numbers, "at index ",i)
#     i += 1

#-----------------------understanding range --------------------

# for i in range(1,10,2 ):
#     print(i)
    
        #"for printing 101 to 1"
# for i in range(100, 0 , -1):
#     print(i)


#-------------------------multiplaction loop----------------------
# n =int(input("please select a numer:"))
# for i in range(1,11,):
#     print(i * n)




#->pass statement:pass is a null statement that dose nothing. it is used as a placeholder for future code . 

# for i in range(5):
#     pass


# wrtie a program to find the sum of frist n number (using while loop)

# n = 9 
# idx = 0
# for i in range(1,n+1):
#     idx += i
# print("total sum =" ,idx)

# n = 5
# sum = 0
# i = 1
# while(i <= n):
#     sum += i
#     i += 1
# print("total sum =" , sum )
    






#write program to find the factorial of frist n number using for lopp
# n = 5
# f = 1

# for i in range(1,n+1):
#     f = f * i
# print(f)





#-------------Q1 Factorial with Loop: Write a program that takes a number n and calculates its factorial using a for loop.<-----------
i = 1
fact = 5
n = 1

for i in range(1,fact+1):
    n *= i
print(n)

#------------------>Q2 Count Even and Odd Numbers: Write a program that takes a list of numbers and counts how many are even and how many are odd using a loop.<------------
list = [1,3,5,7,9,2,4,6,8,10]
idx = 0
for i in list:
    a = (i%2 == 0)
    if(a == True):
        print("There are even number", i)
    if( a== False):
        print("These are odd number", i )
    idx += 1
    
#------------>Q3 Count Even and Odd Numbers: Write a program that takes a list of numbers and counts how many are even and how many are odd using a loop.<-----------



st = "khanbaba"

i = 7

while(i >= 0):
    print(st[i])
    i -=1
    
    
# Q4: Make a loop that prints a triangle of stars

i = 1

while (i <= 5):
    print("*"*i)
    i += 1

# Q5 Write a program that prints numbers from 1 to 20, but only the multiples of 3.

for i in range(1,20):
    if(i%3 == 0):
        print(i)
        
        
# Q6 Take a string from the user and count how many vowels (a, e, i, o, u) are in it using a loop

st = "beebagretahir"

i = 0

for char in st:
    if(char in "a e i o u"):
        print(char)
        i += 1
print("total vowels ", i)

#Q7 Decreasing stars

for i in range(6,0,-1):
    print("*"*i)