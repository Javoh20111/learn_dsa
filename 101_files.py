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

