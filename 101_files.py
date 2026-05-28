""" file_name = "friends.txt"

with open(file_name, "w", encoding="utf-8") as f:
    f.write("Javohir\n")
    f.write("Eshonov\n") """

file_name = "contacts.txt"

with open(file_name, "w", encoding="utf-8") as f:
    f.write("Alice, 23")
    f.write("\nBruno, 19")
    f.write("\nCarla, 31")