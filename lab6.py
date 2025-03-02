#Python builtin functions exercises
#1
import math   
with open("/Users/inzhuaitakhyn/all-labs-2/myfile.txt", "r") as file:  
    numbers = [int(num) for num in file.read().split()] 
result = math.prod(numbers)  

print("Product of all numbers:", result)

#2
with open("/Users/inzhuaitakhyn/all-labs-2/myfile.txt", "r") as file:
    text = file.read()
upper_count = sum(1 for char in text if char.isupper())
lower_count = sum(1 for char in text if char.islower())
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)

#3
with open("/Users/inzhuaitakhyn/all-labs-2/myfile.txt", "r") as file:
    text = file.read().strip()
if text == text[::-1]:
    print("The string is a palindrome!")
else:
    print("The string is NOT a palindrome.")

#4
import time
import math
with open("/Users/inzhuaitakhyn/all-labs-2/myfile.txt", "r") as file:
    lines = file.readlines()

if len(lines) >= 2:
    number = int(lines[0].strip())  
    delay_ms = int(lines[1].strip())  
    def delayed_sqrt(number, delay_ms):
        time.sleep(delay_ms / 1000)  
        result = math.sqrt(number)
        print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
    delayed_sqrt(number, delay_ms)
else:
    print("Error: The file must contain at least two lines (number and delay).")
#5
with open("/Users/inzhuaitakhyn/all-labs-2/myfile.txt", "r") as file:
    content = file.read().strip().split()  
tuple_values = tuple(map(lambda x: bool(eval(x)), content))  
result = all(tuple_values)

print(f"Tuple: {tuple_values}")
print(f"Are all elements True? {result}")
#Python Directories and Files exercises
#1
import os

path = "/Users/inzhuaitakhyn/all-labs-2"  
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
all_items = os.listdir(path)
print("Directories:", directories)
print("Files:", files)
print("All Items:", all_items)
#2
import os
path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"  
exists = os.path.exists(path)
readable = os.access(path, os.R_OK)
writable = os.access(path, os.W_OK)
executable = os.access(path, os.X_OK)
print(f"Path: {path}")
print(f"Exists: {exists}")
print(f"Readable: {readable}")
print(f"Writable: {writable}")
print(f"Executable: {executable}")
#3
import os
path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt" 
if os.path.exists(path):
    print(f"The path '{path}' exists.")
    directory = os.path.dirname(path)
    print(f"Directory: {directory}")
    filename = os.path.basename(path)
    print(f"Filename: {filename}")
else:
    print(f"The path '{path}' does not exist.")
#4
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"  # Update as needed

try:
    with open(file_path, "r") as file:
        line_count = sum(1 for line in file)  # Count lines
    print(f"Number of lines in the file: {line_count}")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#5
user_input = input("Enter items separated by commas: ")
data_list = [item.strip() for item in user_input.split(",")]
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"  
try:
    with open(file_path, "w") as file:
        for item in data_list:
            file.write(item + "\n")  
    print(f"List has been written to {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
#6
import os
import string
directory = "/Users/inzhuaitakhyn/all-labs-2/"  
os.makedirs(directory, exist_ok=True)
for letter in string.ascii_uppercase:  # 'A' to 'Z'
    file_path = os.path.join(directory, f"{letter}.txt")
    with open(file_path, "w") as file:
        file.write(f"This is {letter}.txt\n")  
print(f"26 text files (A.txt to Z.txt) have been created in {directory}")
#7
source_file = "/Users/inzhuaitakhyn/all-labs-2/source.txt"  
destination_file = "/Users/inzhuaitakhyn/all-labs-2/destination.txt" 
with open(source_file, "r") as src, open(destination_file, "w") as dest:
    dest.write(src.read())

print(f"Contents of {source_file} copied to {destination_file}")
#8
import os  
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt" 
if os.path.exists(file_path):
    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    else:
        print(f"Permission denied: Cannot delete '{file_path}'.")
else:
    print(f"File '{file_path}' does not exist.")
    
