print("Reading file content:")

try:
    file1 = open("sample.txt",'r')
    reading_file = file1.readline()
    print("Line 1: ",reading_file)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
finally:
    try:
        file1 = open("sample.txt",'r')
        reading_file = file1.readline()
        line2 = file1.readline()
        print("Line 2: ",line2)
        file1.close()
    except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.") 
print("continue to task 2.")
