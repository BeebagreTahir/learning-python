# try:
#     b =int(input("Please enter the frist number: "))
#     c=int(input("Please enter the secornd number: "))
#     a = b/c
#     print("The answer is ",a)
# except(ZeroDivisionError):
#     print("Error divided by zero")
# except(ValueError):
#     print("You didnt provide a number")
# except:
#     print("Some erroe have occured")
# finally:
#     print("processing complete")



# try:
#     a = int(input("Enter the frsit number:"))
#     b = int(input("Enter the second number:"))
#     c = a/b
#     print("The answer by dividing both number is ",c)
# except(ZeroDivisionError):
#     print("Error: cannot divide by Zero")



#------------>"Imagine you have a number and want to calculate its square root. To do this, you need to create a Python function. You give this function one number, 'number1'.The function should generate the square root value if you provide a positive integer or float value as input. However, the function should be clever enough to detect the mistake if you enter a negative value. It should kindly inform you with a message saying, 'Invalid input! Please enter a positive integer or a float value."<-----------------


#To find the square root of a number use --->math.sqrt(n)



# def finding_square_root(number1):
    
    
#     try:
#         num1 = number1**0.5
#         if(number1 < 1):
#             raise ValueError("Error: please enter a postive or fload value")
#         print(num1)
           
#     except ValueError as e:
#         print(e)
        
# finding_square_root(0)



#                       ------("Both ways are correct")--------


                    
# import math

# def calculating_squareRoot(number1):
#     try:
#         result = math.sqrt(number1)
#     except(ValueError):
#         print("Error: Please enter a postive value or a intiger")
        
# number1 = float(int(input("Please enter a number")))
# calculating_squareRoot(number1)


# ---------->Imagine you have a number and want to perform a complex mathematical task. The calculation requires dividing the value of the input argument "num" by the difference between "num" and 5, and the result has to be stored in a variable called "result".______________________________________________________________________________________________You have to define a function so that it can perform that complex mathematical task. The function should handle any potential errors that occur during the calculation. To do this, you can use a try-except block. If any exception arises during the calculation, it should catch the error using the generic exception class "Exception" as "e". When an exception occurs, the function should display "An error occurred during calculation.

# def inp(number1):
#     try:
#         result = number1 /(number1 - 5)
#         print(result)
#     except Exception as e:
#         print("Error: ")
        
# number1 = float(input("Enter a number : "))

# inp(number1)
    



    