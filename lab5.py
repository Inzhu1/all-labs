#1
import re
pattern = r"^ab*$"
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"
try:
    with open(file_path, "r") as file:
        content = file.read().strip() 
    if re.fullmatch(pattern, content):
        print("The string matches the pattern!")
    else:
        print("The string does NOT match the pattern.")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#2
import re
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"
pattern = r"^ab{2,3}$" 
try:
    with open(file_path, "r") as file:
        content = file.read().strip()  
    words = content.split()  
    for word in words:
        if re.fullmatch(pattern, word):
            print(f"'{word}' matches the pattern!")
        else:
            print(f"'{word}' does NOT match the pattern.")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#3
import re
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"  
pattern = r"\b[a-z]+_[a-z]+\b"  
try:
    with open(file_path, "r") as file:
        content = file.read()  
    matches = re.findall(pattern, content)  
    if matches:
        print("Matches found:", matches)
    else:
        print("No matches found.")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#4
import re
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"  
pattern = r"\b[A-Z][a-z]+\b"  
try:
    with open(file_path, "r") as file:
        content = file.read()  
    matches = re.findall(pattern, content)  
    if matches:
        print("Matches found:", matches)
    else:
        print("No matches found.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#5
import re
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"  
pattern = r"^a.*b$"  
try:
    with open(file_path, "r") as file:
        lines = file.readlines() 
    matches = [line.strip() for line in lines if re.fullmatch(pattern, line.strip())]
    if matches:
        print("Matches found:", matches)
    else:
        print("No matches found.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#6
import re
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()  
    modified_content = re.sub(r"[ ,.]", ":", content)
    print("Modified content:")
    print(modified_content)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#7
import re
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"
try:
    with open(file_path, "r") as file:
        content = file.read().strip()  
    def snake_to_camel(snake_str):
        return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_str)
    camel_case_content = snake_to_camel(content)
    print("Converted to CamelCase:")
    print(camel_case_content)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#8
import re
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"
try:
    with open(file_path, "r") as file:
        content = file.read().strip() 
    split_result = re.split(r'(?=[A-Z])', content)
    print("Split string at uppercase letters:")
    print(split_result)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#9
import re
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"
try:
    with open(file_path, "r") as file:
        content = file.read().strip() 
    modified_content = re.sub(r'(?<!^)(?=[A-Z])', ' ', content)
    print("Modified string with spaces:")
    print(modified_content)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#10
import re
file_path = "/Users/inzhuaitakhyn/all-labs-2/myfile.txt"
try:
    with open(file_path, "r") as file:
        content = file.read().strip() 
    snake_case_content = re.sub(r'(?<!^)(?=[A-Z])', '_', content).lower()
    print("Converted string (snake_case):")
    print(snake_case_content)

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")