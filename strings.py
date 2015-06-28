
from __future__ import print_function

# == REPLACEMENT ==
# NOTE: case insensitive replacement requires 're' module
text = "Hello World World"
print(text)                                # "Hello World World"
print(text.replace("World", "Nick"))       # "Hello Nick Nick"
print(text.replace("World", "Nick", 1))    # "Hello Nick World"
print(text)                                # "Hello World World"

# == SLICING ==
# SYNTAX: text[start:end:step]
# 'end' and 'step' are optional
# text[start]     = char at position 'start'
# text[start:]    = substring from 'start' to end of 'text'
# text[start:end] = substring from 'start' to before 'end'

text = "Nick rocks"
#  0 is before 'N'
#  1 is before 'i' and after 'N'
#  2 is before 'c' and after 'i'
# -1 is before 's'   
print(text[0:4])                           # "Nick"
print(text[-5:])                           # "rocks"
print(text[-5:-3])                         # "ro"
