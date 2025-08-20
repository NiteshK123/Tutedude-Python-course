# Task 1
def factorial(n):
	if n<2:
		return 1
	else:
		return n*factorial(n-1)

n = int(input('Enter a number: '))
a = factorial(n)
print('Factorial of',n,'is:',a)

# Task 2
from math import *
num = int(input('Enter a number: '))
num1 = sqrt(num)
num2 = log(num)
num3 = sin(num)
print('Square root:',str(num1))
print('Logarithm:',str(num2))
print('Sine:',str(num3))