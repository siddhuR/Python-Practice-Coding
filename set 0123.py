import re

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[0123]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
    
else:
    print("No match")
