# Character   Meaning
# 'r'         open for reading (default)
# 'w'         open for writing, truncating the file first
# 'x'         create a new file and open it for writing
# 'a'         open for writing, appending to the end of the file if it exists
# 'b'         binary mode
# 't'         text mode (default)
# '+'         open a disk file for updating (reading and writing)
# 'r+'        Will over write the sstart of data (no trucket)
# 'w+'        open for read and writing but all data will be deleted 
# 'a+'        Read and add/append pointer at end (no trucket)




#---------For opening and reading a file-----------

# f = open("text.txt","r")
# data = f.read()
# print(data)
# f.close


#------------For reading just one line---------

# f = open("text.txt","r")

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close


# ----------------------> Writing to a file<--------------

#to change all text of file or overwrite it
# f = open("text.txt","w")

# f.write("I want to quit the job")
# f.close()



#To add text to the end of file or append text
#--->if there is no file exist and run the code python will create a file with that name
# f = open("text.txt","a")
# f.write("\n I am really good at programming")




# -----------------------------> With Syntax "clean way "<------------------ by using with file will automaticly be closed


# with open("text.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("text.txt","w") as f:
#     f.write("Writin in proper syntax")



# ----------------------> Deleting a file<--------------
#using the or module : Module(like a code library)is a written by another programmer that generally has function we can use

# import os

# os.remove("simple.txt")





# ---------------------> Practice Q:Create a new file "practice.txt" using python.Add the following data in it.

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are leaarning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")
    
    
    
#--------->Q: WAF that replace all occurancse of "Java" with "Python in the above file"
# with open("practice.txt", "r") as f:
#     data = f.read()
    
#     new_data = data.replace("Java","Python")
#     print(new_data)
    
# with open("practice.txt","w") as f:
#     f.write(new_data)
    
    
    
#------------->Q: Search if th word "Learning" exists in the file or not.


# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find("leaarning") != -1 ): or if(word in data)
#         print("found")
#     else:
#         print("Not found")



#--------------->Q:WAF to find in which line of the file does the word "learning " occure frist print -1 if word not found

# def check_for_line():
#     word = "Python"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1      

# check_for_line()




# ------>Q: From a file containing numbers seprated by comma,print the count of even numbers.
#take out indivdual and cast that string in intiger
 
# def check_for_evennum():
#     with open("number.txt","r") as f:
#         data = f.read()
#         print(data)
            

# check_for_evennum()



# ---------------> Q:Count Words .Read the file and count how many times the word "hello" appears (case insensitive).Print the count.

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



#--------------->Q: Longest Word:Read all words from the file and print the longest word and its length.

# with open("practice.txt","r") as f:
#     data = f.read()
#     words = data.split()
#     longest_word = ""
#     for w in words:
#         if(len(w) > len(longest_word)):
#             longest_word = w
#     print(longest_word,len(longest_word))


# Q: find the shortest word

# with open("practice.txt","r") as f:
#     data = f.read()
#     words = data.split()
#     shortest_word = words[0]
#     for w in words:
#         if(len(w) < len(shortest_word)):
#             shortest_word = w
#     print(shortest_word)



#-----------> Q:Count Vowels in File:Count how many vowels (a, e, i, o, u) appear in the whole file
# i = 1
# with open("practice.txt","r") as f:
#     data = f.read()
#     for w in data:
#         if(w  in "aeiou"):
#             print(w,i)
#             i += 1
        
        

#--------------> Q: Reverse Each Word: Read words from the file and print each word reversed, but in the same order:Example: "Hello World" → "olleH dlroW".

# with open("practice.txt","r") as f:
#     data = f.read()
#     words = data.split()
#     print(words)
#     for w in words:
#         print(w[::-1])
    
with open("practice.txt","r") as f:
    data = f.read()
    new_data = data.replace("in","im")
    print(new_data)
    
with open("practice.txt","w") as f:
    f.write(new_data) 
        
        
