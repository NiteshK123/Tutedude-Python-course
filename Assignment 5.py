# task 1

data = {'Alice':5, 'Bob':7}
a = input("Enter the student's name: ")
try:
	print("{}'s marks: {}".format(a, data[a]))
except:
	print('Student not found.')


# Task 2
l = [i+1 for i in range(10)]
print('Orignal list: {}'.format(l))
l1 = l[0:5]
l2= l1[::-1]
# l2.reverse()
print('Extracted first five elements: {}'.format(l1))
print('Reversed extracted list: {}'.format(l2))