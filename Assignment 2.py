# Task1
a = int(input('Enter a number: '))
if a%2==0:
	print(str(a),'is an even number.')
else:
	print(str(a),'is an odd number.')

# Task2
n=50
total=0
for i in range(1,n+1):
	total+=i
print('The sum of numbers from 1 to 50 is:', str(total))