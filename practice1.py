#Write a Python program to search a literal string in a string and also find the location within the original string where the pattern occurs.

import re
pattern = 'more'
text = 'we have one more class after python class'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))
	