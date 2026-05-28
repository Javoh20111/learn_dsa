""" file_name = "friends.txt"

with open(file_name, "w", encoding="utf-8") as f:
    f.write("Javohir\n")
    f.write("Eshonov\n") """


source = input("Please provide source: ")
destination = input("Please provide destination: ")


with open(source, "r", encoding="utf-8") as f:
    data = f.read()

with open(destination, "w", encoding="utf-8") as d:
    d.write(data)