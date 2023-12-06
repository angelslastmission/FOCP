#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Variable Assignment
#TASK1: Try inputting the following code and examine the results.
total = 100
print("The total is",total)


# In[33]:


#TASK2: Try inputting the following code and examine the results.
total=total+99
print("The total is now",total)


# In[34]:


#TASK3: Try inputting the following code, but replace each of the assignment expressions with
#the equivalent augmented assignment.
total=total-1
print("The total is",total)

total=total*4
print("The total is",total)

total=total/2
print("The total is",total)


# In[36]:


#TASK4: Try extending the code below so that it creates a new variable called ‘average’, that
#is set to equal the average calculated from the two other variables.
total=98.2
count=5
average=total/count
print("Average is",average)


# In[6]:


#DataTypes
#A Variable's data-type
#TASK: Use the type() function to determine the type of each of the following values.
list = [False, 1000, 100.111, "Hello", True, 100 / 5, 100 // 5]

for i in list:
    print(f"{i} is of type {type(i)}")


# In[7]:


#TASK: Input the following code and examine the result. What is the * operator doing to the
#given string operand?
value = "ABC"*10
print(value)


# In[10]:


#Calling Built-in functions
#TASK: Write some code that calls the print() function several times, displaying your
#name, address and contact details. Add additional calls to the print() function which
#includes an argument that calculates and prints the length of your name, by calling the
#len() function.
name="Eric Idle"
print("The average was",total/count)
name_length=len("Eric Idle")
print("The length of your name is",len(name))


# In[12]:


#TASK: Input the following code, when asked to type your age input a numeric value such as
#20. Does this program work? If not, why?
age = input("Enter your age")
print("in one year your age will be", age + 1)


# In[13]:


#the above program doesnot work an shows TypeError: can only concatenate str (not "int") to str


# In[14]:


#TASK: Write a program that prompts the user to input two numeric values. Once the values
#have been input display the product of these values, using the multiply (*) operator.
num1 = float(input("Enter the first numeric value: "))
num2 = float(input("Enter the second numeric value: "))
product = num1 * num2
print("The product of", num1, "and", num2, "is:", product)


# In[15]:


#Single,Double and Triple Quotes
#TASK: Try writing the above assignment statement but only use double quotes instead of
#single quotes as the string delimiter. What is the result?
comment = "I would have \"thought\" you knew better!"
print(comment)


# In[16]:


#Escape Sequences
#TASK: Write some code that calls a print() function, which takes a single string argument
#that results in the following text being displayed (exactly as shown).
print("This text includes characters such as '\','"' and "'", \n This is a new line that starts with a tab \n\t This is a new line that starts with two tabs" )


# In[17]:


#TASK: Write some code that calls a print() function, which takes a single string argument
#that results in the following text being displayed (exactly as shown).
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n Hello there! \n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")


# In[18]:


#Using triple quotes
#TASK: Write some code that calls a print() function, which takes a single string argument
#that results in the following text being displayed (exactly as shown). Do this without the use
#of any escape sequences.
print("""This text spans there lines, \n and include both single('), \n and double quotes (")""")


# In[19]:


#Indexing and Slicing
#TASK: Rewrite the above example, so that the third letter of the ‘surname’ is accessed
#rather than the first, then print this letter to the screen.
surname = "Palin"
third_letter = surname[2]

print("Third letter is",third_letter)


# In[20]:


#TASK: Rewrite the above example, so that the tenth letter of the ‘surname’ is accessed,
#and note the result.
surname = "Palin"
tenth_letter = surname[9]

print("Tenth letter is",tenth_letter)


# In[21]:


#the above program gives the result IndexError: string index out of range


# In[26]:


#TASK: Rewrite the above example, so that the second from last letter of the ‘surname’ is
#accessed rather than the last, then print this letter to the screen.
surname = "Palin"
sliced = surname[:-2]

print("Second from last letter of the surname", sliced)


# In[23]:


#Slicing
#TASK: Rewrite the above example, so that all of the characters of the ‘surname’ except the
#first character are sliced and then displayed on the screen.
surname = "Palin"
sliced = surname[:1]

print("Surname except the first character is",sliced)


# In[27]:


#TASK: Write code that accesses and prints all characters of the ‘surname’ except the last
#character.
surname = "Palin"
sliced = surname[:-1]
print("Surname except the last character is",sliced)


# In[29]:


#Introducinglists
#TASK: Write code that uses slicing to access then print the first four prime numbers defined
#within the ‘primes’ list given above. Note: you will have to input that list first for testing
#purposes.
primes = [2,3,5,7,11,13,17,19,23,29]
first_four = primes[:4]
print("The first four prime numbers are:", first_four)


# In[31]:


#TASK: Write code that uses slicing to insert two new names just before the final name within
#the ‘names’ list.
names = ["Harry", "Tom", "Tim", "Bill", "Graeme"]
new_names = ["Mark", "Jacob"]
names[-1:-1] = new_names
print("Updated names list:", names)


# In[ ]:




