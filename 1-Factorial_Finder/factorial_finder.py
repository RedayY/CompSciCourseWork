# Code by Reday Yahya
# 17/12/2019
# Task 1: Factorial Finder
# The Factorial of a positive integer, n, is defined as the product 
# of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0,
# is defined as being 1. Solve this using both loops
# and recursion. (Skipping recursions, native python)

import os
import math

userInput = int(input("Insert number to be factorialized: "))

#Function that finds Factorial of given Integer
def factorialFinder(factorialInt):
    arrayOfInts = []
    orderedInts = []
    
    if factorialInt > 0:
        #Setting up User Input for sorting
        for i in range(userInput):
            arrayOfInts.append(i)

        #Sorting Array
        arrayOfInts.remove(0)
        while len(arrayOfInts) > 0:
            orderedInts.append(arrayOfInts[-1])
            arrayOfInts.remove(arrayOfInts[-1])
            
        #Calc and Output Block    
        result = math.prod(orderedInts)
        factorial = result * factorialInt
        print("Factorial of: ", factorialInt, " is: ", factorial)
        
    else:
        #In Maths its agreed to view a factorial of 0 as 1
        factorialInt = factorialInt + 1
        print("Factorial of: ", factorialInt, " is: ", factorialInt)    
            
#Methodcall by Input
factorialFinder(userInput)