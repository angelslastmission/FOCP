#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Boolean Expressions
#TASK: Start the Python Interpreter and input the following expressions, noting each result.
print(10<100)
print(100 != 100)
print(50>= 50)


# In[3]:


#TASK: Input a program that defines a variable called ‘age’ that is initialised to your own age.
#Then type several boolean expressions that compare the variable to see whether it is less
#than ‘18’, ‘21’ then ‘31’.
# Define the variable 'age' initialized to your own age
age = 20
is_less_18 = age < 18
is_less_21 = age < 21
is_less_31 = age < 31
print(f"Is the age less 18? {is_less_18}")
print(f"Is the age less 21? {is_less_21}")
print(f"Is the age less 31? {is_less_31}")


# In[6]:


#TASK: Try inputting the following code and note the results.
"a"<"b"


# In[7]:



"b"<"a"


# In[8]:



"John"<"Terry"


# In[9]:


#TASK: Try inputting the following code and note the result. Try to work out why the answer is
#different from the previous expression (look carefully, it is different).
"john"<"Terry"


# In[10]:


#lowercase letters have higher unicode values than uppercase letters


# In[2]:


#TASK: Try inputting the following code and note the results.
5<10.2


# In[3]:


5<"Monty"


# In[4]:


5<"5"


# In[5]:


#Logical expressions with Expressions
#TASK: Try inputting the following code and examine the results.
age = 30
print (age >=18 and age <=65)
print(age <18 or age >65)
print(not age > 18)


# In[6]:


#TASK: Try inputting the following code and examine the result.
age = 30
print((age >=18 and age <=65) and (not age==30))


# In[7]:


#Chaining relational operators
#TASK: Try inputting two expressions that use operator chaining and are equivalent to the
#two expressions shown below. (note: you may first want to first assign values to the
#‘weight’ and ‘height’ variables for testing purposes)
weight = 121
print(100 < weight < 200) 

height = 149
print(131 < height < 160) 


# In[9]:


#Membership testing
#TASK: Input the examples above but with alternative operand values, that result in both
#True and False results.
names = ["Terry", "John", "Michael","Eric","Graham"] 

print("Eric" in names)
print("Terry" in names)
print("Sisham" in names)


# In[10]:


message = "Hello there, my name is Sisham"
print("name" in message) 
print("message" in message)



# In[11]:


#The'if' statement
#TASK: Try writing an if statement that checks if someone is between the ages of 18 and 30
#inclusive. If they are, then #print a message saying &quot;you are still young!&quot;
age = 20
if age >= 18 and age <= 30:
    print("You are still young!")


# In[12]:


#using the "elif" clause
#TASK: Try writing an if statement similar to the last example that includes an extra elif
#clause to check ages between 30-40. Print a suitable message in the associated code block.
age = 35
if age > 100:
    print("You are very old,")
    print("Well done!")
elif age > 80:
    print("You are fairly old")
    print("Pretty good!")
elif age > 40:
    print("You are middle-aged")
    print("Never mind")
elif 30 <= age <= 40:
    print("You are in your 30s or early 40s")
    print("Age is just a number!")
else:
    print("You are not very old - yet")


# In[13]:


#Non-boolean conditions
#TASK: Rewrite the above code that inputs a name then prints a message, but change the
#condition so it explicitly uses a Boolean expression. Use the example below to help.
name = input("Enter your name: ")
if name != "":
    print("Your name is", name)
else:
    print("Name not entered")


# In[14]:


#the ternary operator
#TASK: Rewrite the code shown below as a single line Ternary expression.
age = 20
if age>=18:
    print("you are an adult")
else:
    print("you are not ab adult,yet!")


# In[15]:


#Using "while" and "for" loops
#TASK: Input and execute a for loop that iterates over a list of four names, printing each of
#them to the screen.
names = ["Eric", "Terry", "John", "Sisham"]
for name in names:
    print(name)


# In[16]:


#The range() function
#TASK: Input and execute a for loop that uses a range() function to generate the following
#output:
for n in range(2, 11, 2):
    result = n ** n
    print(f"{n} to the power of {n} = {result}")


# In[17]:


#Using 'continue' with loop
#TASK: Input code containing a for loop that iterates over a list of numbers, printing a
#running total during each iteration. #You may wish to first define the numbers list as follows:
numbers = [10, 20, 30, 90, 200, 30, 22, 11]
running_total = 0
for number in numbers:
    running_total += number
    print(running_total)


# In[18]:


#TASK: Amend your previous solution so that if any value within the list is found to be over
#100 then the loop should break immediately.
numbers = [10, 20, 30, 90, 200, 30, 22, 11]
running_total = 0
for number in numbers:
    if number > 100:
        break
    running_total += number
    print(running_total)


# In[34]:


#TASK: Amend your previous solution once again, so that the message “all numbers
#processed” is printed when the loop completes, but only if all values were less or equal to
#100 (i.e. the loop did not break early)
numbers = [10, 20, 30, 90, 200, 30, 22, 11]  

running_total = 0
for number in numbers:
    if number > 100:
        break    
    running_total += number
    print(running_total)
else:
    print("All numbers processed")


# In[ ]:





# In[ ]:




