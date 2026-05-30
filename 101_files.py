""" file_name = "friends.txt"
 """
""" with open(file_name, "r", encoding="utf-8") as f:
    pos0 = f.tell()
    head = f.read(5)
    pos1 = f.tell()
    print(pos1) """


""" source = input("Please provide source: ")
destination = input("Please provide destination: ")

try:
    with open(source, "r", encoding="utf-8") as f:
        data = f.read()
        with open(destination, "w", encoding="utf-8") as d:
            d.write(data)
except:
    print("File not found! Please check out sourse location!") """

""" file_name = "contacts.txt"
try:
    with open(file_name, "r", encoding="utf-8") as f:
        line = f.readline()
        while line != "":
            print(line, end="")
            line = f.readline()
except FileNotFoundError:
    print("Error: file not found.") """

from datetime import datetime
import pandas as pd 

""" with open("person.csv", "a+", encoding="utf-8") as l:
    name = input("Enter your name")
    time = datetime.now().strftime("%Y-%m-%d %H-%M")
    l.write(f"\n{name},{time}") """


""" df = pd.read_csv("person.csv", header=None, names = ["name", "date"])
print(df) """

""" with open("contacts.txt", "r", encoding="utf-8") as c:
    rows = []
    for line in c:
        line = line.strip("\n")
        if line =="":
            continue
        rows.append(line)
count = 0 
total = 0
for elem in rows:
    count+=1
    elem = elem.split(",")
    name = elem[0].strip()
    age = int(elem[1].strip())
    total+=age
 """

import csv

""" people = [
 ["name", "age"],
 ["Mara Pinto", 25],
 ["Rúben Pinto", 18]
]

with open("people.csv", "w",  newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(people) """

""" with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  """



""" with open("people.csv", "a+", encoding="utf-8") as f:
    num = int(input("The number students: "))
    for i in range(num):
        name = input("What is your name: ")
        age = int(input("Enter your age: "))
        writer = csv.writer(f)
        writer.writerow([name,age])

with open("people.csv", "r", encoding="utf-8") as f:
    print(f"\n{'NAME':<8}{'AGE':>7}\n--------------------")

    reader = csv.reader(f)
    for line in reader:
        if len(line) != 2:
            print(f"Warning: Skipping malformed line: {line}")
            continue

        name,age = line
        print(f"{name:<10}{age:>5}")"""

import os 

path = "contacts.txt"
if os.path.isfile(path):
    print("File exists")
else:
    print("Missing file")
