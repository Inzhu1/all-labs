#json
with open("sample-data.json", "r") as file:
    data = json.load(file)
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)
for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    description = item["l1PhysIf"]["attributes"].get("description", "")
    speed = item["l1PhysIf"]["attributes"].get("speed", "inherit")
    mtu = item["l1PhysIf"]["attributes"].get("mtu", "")
    print("{:<50} {:<20} {:<10} {:<10}".format(dn, description, speed, mtu))
#python date
#1
from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Current Date:", current_date)
print("Date 5 days ago:", new_date)
#2
from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())
#3
from datetime import datetime
current_datetime = datetime.now()
new_datetime = current_datetime.replace(microsecond=0)
print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", new_datetime)
#4
from datetime import datetime
date1_input = input("Enter the first date (in format YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.strptime(date1_input, "%Y-%m-%d %H:%M:%S")
date2_input = input("Enter the second date (in format YYYY-MM-DD HH:MM:SS): ")
date2 = datetime.strptime(date2_input, "%Y-%m-%d %H:%M:%S")
difference = (date2 - date1).total_seconds()
print( difference)
#generators
#1
def generate_squares(n):
    for i in range(1, n + 1):
        yield i ** 2
n = int(input("Enter N: "))
print(f"Squares up to {n}:")
for square in generate_squares(n):
    print(square)
#2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
n = int(input("Enter n: "))
print("Even numbers:", ",".join(str(num) for num in even_numbers(n)))
#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter n: "))
print(f"Numbers divisible by 3 and 4 between 0 and {n}:")
for number in divisible_by_3_and_4(n):
    print(number)
#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
print(f"Squares from {a} to {b}:")
for square in squares(a, b):
    print(square)
#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i
n = int(input("Enter n: "))
print(f"Countdown from {n} to 0:")
for num in countdown(n):
    print(num)
#math library
#1
import math
degree = float(input("Input degree: "))
radian = math.radians(degree)
print(f"radian: {radian:.6f}")
#2
import math
height = float(input("Height: "))
base1 = float(input("first value: "))
base2 = float(input("second value: "))
area = (base1 + base2) * height / 2
print(f"Expected Output: {area}")
#3
import math
num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))
area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
print(f"The area of the polygon is: {area:.2f}")
#4
import math
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print(f"Expected Output: {area}")
