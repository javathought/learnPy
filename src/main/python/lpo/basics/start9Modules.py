# import the library
import urllib

# import foo.bar
# or
# from foo import bar
# 


# use it
    # help(urllib.urlopen)
# urllib.urlopen(...)

import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))