print("------------------------------------------------")
print( "    WELCOME TO YOUR PERSONAL CALCULATOR ")
print("-------------------------------------------------")


#Addition function.

def add(a,b):
 sum= a + b
 return sum


#Subtraction function.

def subtract(a,b):
 difference= a - b
 return difference
 

#Multipication function. 

def prod(a,b):
    product = 0
    counter = 0
    while counter<b:
        product = add(product,a)
        counter = add(counter,1)
    return product


#Division Function.

def Division(m,n):
 
 # Global "result" used here because i want to use "result" later in my equation 
 # function. I did this so i could get rid of the remainder.
 
 global result
 result = 1
 
 if (n==0) :
  return "The result of any integer divided by zero is undefined."

# This elif statement used when n and m are negative, it takes  the absolute
# value of both m and n, to allow the program to evaluate.

 elif (n<0) and (m<0):
   n = subtract(0,n)
   m = subtract(0,m)
  
   answer = subtract(m,n)
   while answer>0:
    result = add(result,1)
    answer = subtract(answer,n)
   return (str(subtract(0,m))+"/"+str(subtract(0,n))+" = "+str(result)+
           " remainder "+str(answer))

 # I take absolute value of n and m separatly in these the elif statements
 # this is done so to eliminate a problem i was having with negatives.

 elif (n<0):
   n = subtract(0,n)
   answer = subtract(m,n)
   while answer>0:
    result = add(result,1)
    answer = subtract(answer,n)
   return (str(m)+"/"+str(subtract(0,n))+" = "+str(subtract(0,result))+
            " remainder "+str(subtract(0,answer))) 
 elif (m<0):
   m = subtract(0,m)
   answer = subtract(m,n)
   while answer>0:
    result = add(result,1)
    answer = subtract(answer,n)
   return (str(subtract(0,m))+"/"+str(n)+" = "+str(subtract(0,result))+
            " remainder "+str(subtract(0,answer))) 
   
 else:
  answer = subtract(m,n)
  while answer>0:
   result = add(result,1)
   answer = subtract(answer,n)
  return str(m)+"/"+str(n)+" = "+str(result)+" remainder "+str(answer) 


 
# Factorial function.

def factorial(a):
 answer = 1
 if a<=1:
  answer = 1
  return answer
 else:
  while a>1:
   answer = prod(answer,a)
   a = subtract(prod(a,1),1)
  return answer
 

# Double factorial function.
def doubleFactorial(a):
 answer = 1
 if a<=1:
  answer = 1
  return answer
 else:
  while a>1:
   answer = prod(answer,a)
   a = subtract(prod(a,1),2)
  return answer

# Equation solver.

def equation():
 print()
 print(" Options: ")
 print("    + : Addition  ")
 print("    - : Subtraction ")
 print("    * : Multiplication ")
 print("    / : Division ")
 print("    ! : Factorial")
 print("    !!: Double Factorial")
 print("    = : Solve equation \n")
 
 answer = int(input("Select an initial integer:"))
 print()
 choice = input( "Choose one of the options listed above:")
 print()
 
 
 while True:
  if choice == "+":
   print()
   x = int(input("Choose a real number for addition:")) 
   print()
   answer = add(answer,x)
   choice = input("Choose another operator:")
  
  elif choice == "-":
    print()
    x = int(input("Choose an integer for subtraction:")) 
    print()
    answer = subtract(answer,x)
    choice = input("Choose another operator:")
  
  elif choice == "*":
   print()
   x = int(input("Choose a number for product:"))
   print()
   answer = prod(answer,x)
   choice = input("Choose another operator:")
   
  elif choice == "/":
   print()
   x = int(input("Choose a number to divide total:"))
   print()
   answer = Division(answer,x)
   answer = int(result)
   choice = input("Choose another operator:")
   
  elif choice == "!":
   print()
   answer = factorial(answer)
   choice = input("Choose another operator:")
   
  elif choice == "!!":
   print()
   answer = doubleFactorial(answer)
   choice = input("Choose another operator:")
   
  elif choice == "=":
   print()
   return str(answer)+" is the result of your equation."  
   break
  
  else:
   print("invalid operation")
   choice = input("Make a valid choice:")



print(" Options: ")
print("    1 - Addition  ")
print("    2 - Subtraction ")
print("    3 - Multiplication ")
print("    4 - Division      ")
print("    5 - Factorial     ")
print("    6 - Double Factorial")
print("    7 - Equation        ")
print("    Q - Quit\n           ")

option = input( "Choose one of the options listed above:")
print()
while True:
 
 if option == "1":
  print()
  x = int(input("Choose a real number for addition:"))
  print()
  y = int(input("Choose a second real number for addition:"))
  print()
  print("("+str(x)+")"+"+"+ "("+str(y)+")"+"="+ str(add(x,y))+"\n")


 elif option == "2":
   print()
   x = int(input("Choose any number for subtraction:"))
   print()
   y = int(input("Choose a second integer for subtraction:"))   
   print()
   print("("+str(x)+")"+"-"+ "("+str(y)+")"+"="+ str(subtract(x,y)))
 
 
 elif option == "3":
  print()
  x = int(input("Choose a number for product:"))
  print()
  y = int(input("Choose a second number for product:"))
  print()
  print("("+str(x)+")"+"*"+ "("+str(y)+")"+"="+ str(prod(x,y))+"\n")


 elif option == "4":
  print()
  x = int(input("Choose a numerator for division:"))
  print()
  y = int(input("Choose the denominator for division:"))
  print()
  print(Division(x,y))
 
 
 elif option == "5":
  print()
  z = int(input("Choose an integer to take the factorial of:") +"\n")
  print()
  print("("+str(z)+")"+"!"+"="+ str(factorial(z)))
 
 
 elif option == "6":
  print()
  z = int(input("Choose an integer to take  the double factorial of:") )
  print()
  print("("+str(z)+")"+"!!"+"="+ str(doubleFactorial(z))+"\n")
 
 
 elif option == "7":
  print()
  print(equation())
 
 
 elif option == "Q":
  break


 else:
  print( "Invalid choice, please select again."+"\n")
 print()
 option = input("Select another option.")
 

print("------------------------------------------------")
print( "   THANKS FOR USING MY PROGRAM, GOODBYE! ")
print("-------------------------------------------------")


