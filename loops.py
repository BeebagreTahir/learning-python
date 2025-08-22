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




# ------------> Contnue in loop mean skip the next step <--------------

# i = 1
# while (i <= 10):                #to print odd numbers
#     if(i%2 == 0):
#         i += 1
#         continue # skip
#     print(i)
#     i +=1


i = 1
while (i <= 10 ):
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i +=1


