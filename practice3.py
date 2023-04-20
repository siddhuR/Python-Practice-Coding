#Write a Python program to match if two words from a list of words starting with letter "P".

import re
words = ["start send", "want went", "python java"]
for p in words:
        m = re.match("(P\w+)\W(P\w+)", p)
        if m:
            print(m.groups())
			