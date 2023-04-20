#Write a Python program to find the substring within a string.

import re
text = 'we have one more class after python class'
pattern = 'class'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)
	