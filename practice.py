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

#-------------Q1<-----------
# i = 1
# n = 5

# for i in range(1,n):
#     n *= i
# print(n)

#------------------>Q2<------------
list = [1,3,5,7,9,2,4,6,8,10]
idx = 0
for i in list:
    a = (i%2 == 0)
    if(a == True):
        print("There are even number", i)
    if( a== False):
        print("These are odd number", i )
    idx += 1
    
#------------>Q3<-----------



st = "khanbaba"

i = 7

while(i >= 0):
    print(st[i])
    i -=1
    

    