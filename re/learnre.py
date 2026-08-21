import re 

text_to_search = ("""
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \\ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
""")

setence = "In this Python Programming Tutorial, we will be learning how to read, write, and match regular expressions with the re module. Regular expressions are extremely useful for matching common patterns of text such as email addresses, phone numbers, URLs, etc. Learning how to do this within Python will allow us to quickly parse files and text for the information we need. Let's get started..."


pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)