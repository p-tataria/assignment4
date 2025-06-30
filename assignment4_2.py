a = str(input("Enter text to write to the file: "))

file1 = open("output.txt",'r+')
line1 = file1.write(a)

file1.close()

print("Data successfully written to output.txt.")
b=str(input("Enter additional text to append: "))


file1 =  open("output.txt",'a')
line2 = file1.write("Learning the file handling in python.")

file1.close()

print("Data successfully appended.")

print("Final content of output.txt: ")

file1 = open("output.txt",'r')
variable = file1.readline()
variable2 = file1.readline()
print(variable)
print(variable2)
file1.close()