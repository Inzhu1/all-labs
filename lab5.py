#1
import re
pattern = r'\bab*\b'
text = input("Enter a string: ")
matches = re.findall(pattern, text)
print("Matched words:", matches)
#2
import re
text= input("Enter a string: ")
pattern = r"ab{2,3}"
words = text.split()
matched_words = [word for word in words if re.fullmatch(pattern, word)]
print("Matched words:", matched_words)
#3
import re
pattern = r'\b[a-z]+(?:_[a-z]+)+\b' 
text = input("Enter a string: ")
matches = re.findall(pattern, text)
print("Matched words:", matches)
#4
import re
pattern = r'\b[A-Z][a-z]+\b'
text = input("Enter a string: ")
matches = re.findall(pattern, text)
print("Matched words:", matches)
#5
import re
pattern = r'\ba[^ ]*b\b'  
text = input("Enter a string: ")
matches = re.findall(pattern, text)
print("Matched words:", matches)
#6
import re
text = input("Enter a string: ")
modified_text = re.sub(r'[ ,.]', ':', text)
print("Modified string:", modified_text)
#7
import re
def snake_to_camel(snake_str):
    words = snake_str.split('_')  
    return words[0] + ''.join(word.capitalize() for word in words[1:])  
text = input("Enter a snake_case string: ")
matches = re.findall(r'\b[a-z]+(?:_[a-z]+)*\b', text) 
converted = [snake_to_camel(match) for match in matches]
print("Converted words:", converted)
#8
import re
def split_at_uppercase(s):
    return re.findall(r'[A-Z][a-z]*', s)  
text = input("Enter a string: ")
words = split_at_uppercase(text)
print("Splitted words:", words)
#9
import re
def insert_spaces(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)  
text = input("Enter a string: ")
modified_text = insert_spaces(text)
print("Modified string:", modified_text)
#10
import re
def camel_to_snake(s):
    snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s)
    return snake_case.lower() 
text = input("Enter a CamelCase string: ")
converted_text = camel_to_snake(text)
print("Converted string:", converted_text)
