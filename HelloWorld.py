
# simple version
# print("Hello World!")

# with name hard-coded in
# name = 'Kristin'
# print('Hello {}!' .format(name))

# print('Hello', name)

# ask user for a name
# name = input("Please enter a name:")
# print('Hello', name)

import datetime
name = input("Please enter a name:")
c = datetime.datetime.now()
q = c.hour
s = ""

if 0 <= q < 12:
    s = "Good morning"

elif 12 <= q < 17:
    s = "Good afternoon"

else:
    s = "Good evening"

print(s, name, "it is", c)





