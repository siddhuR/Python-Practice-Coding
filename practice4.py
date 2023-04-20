#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re
text = ' we have one more class after python class. '
print(re.sub("[ ,.]", ":", text))
