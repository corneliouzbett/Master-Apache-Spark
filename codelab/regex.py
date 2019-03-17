import re

text = "The example code is for dummies like you"

x = re.search("^The .*you$", text)

if (x):
    print("YES we have a match")
else:
    print("NOT don't have a match")