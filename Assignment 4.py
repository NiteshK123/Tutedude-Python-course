
# Task 1
try:
	file = open('sample.txt','r+')
	reading_file = file.readlines()
	print('Reading file content:')
	for i in range(len(reading_file)):
		if i==len(reading_file)-1:
			print('Line'+str(i+1)+':',reading_file[i])
			continue
		print('Line'+str(i+1)+':',reading_file[i][:-1])
	file.close()
except FileNotFoundError:
	print("Error: The file 'sample.txt' was not found.")


print()

# Task 2
with open('output.txt','w') as file1:
	input1 = input('Enter text to write to the file: ')
	file1.write(input1)
	print('Data successfully writen to output.txt.')

with open('output.txt','r') as file1:
	print('Final content of output.txt:')
	reading_file = file1.read()
	print(reading_file)

with open('output.txt','a') as file1:
	input2 = input('Enter additional text to append: ')
	file1.write("\n"+input2)
	print('Data successfully appended.')

with open('output.txt','r') as file1:
	print('Final content of output.txt:')
	reading_file = file1.read()
	print(reading_file)