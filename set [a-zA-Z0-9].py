import re

txt = "The Clock shows 10:00 AM"

#Check if the string has any a, r, or n characters:

x = re.findall("[a-zA-Z0-9]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
    
else:
    print("No match")

