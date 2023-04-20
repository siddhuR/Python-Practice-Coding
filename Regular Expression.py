import re
txt = "The rain in Spain"
x = re.findall("Spain$" , txt)

if (x) :
    print("Yes, there is at least one match")
else:
    print("No match")



