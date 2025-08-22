#----> Recursive function <-------

# def show(n):
#     if(n == 0): #Base case for stopping condetion
#         return 
#     print(n)
#     show(n-1)

# n = int(input("Enter a number"))
# show(n)



# write a recursive function to calculate the sum of frist n natural number;

# def run(n):
#     if(n == 0):
#         return 0
#     return run(n-1) + n

# print(run(5))



#------> write a recursive function to print a;; elements in a list.

def count(a,i):
    if(i == len(a)):
        return 
    print(a[i])
    print(a , i + 1)
    
number = [1,2,3,4,5,6,7,8,9]

count(number , 0)
    
        
        
    

    
        
    