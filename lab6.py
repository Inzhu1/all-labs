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