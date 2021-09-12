# ITP Week 1 Day 4 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
def subt(num1, num2):
    return(num1 - num2)
print(subt(5,3))

#     - A function that multiplies three integers
def mult(num1, num2, num3):
    return(num1 * num2 * num3)
print(mult(5,4,3))

#     - A function that adds four integers
def addt(num1, num2, num3, num4):
    return(num1 + num2 + num3 + num4)
print(addt(5,4,3,2))


# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.
 #use for, if, else statements
 #if string == +
 #  return num1 + num2
 #elif string == 1
 #return num1 - num2
 #elif string == *

# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.

#Remember to first write in comments an outline of what you want to code (using regular words, no computer-speak) BEFORE you begin to code.  Break each part down to the smallest problem you can, and then address them individually.  CONSULT THE RESOURCES if you get stuck, and don't be afraid to Google.