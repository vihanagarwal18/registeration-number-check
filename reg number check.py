import re
register= input("enter your 9 character long registeration number:")
if re.match("^[1-9][0-9][a-zA-Z][a-zA-Z][a-zA-Z][0-9][0-9][0-9][0-9]$",register):
    print("yes")
else:
    print("No")
