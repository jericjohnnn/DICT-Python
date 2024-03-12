import os

f = open("math")
print(f.read())

f = open("math", "a")
f.write("i like python")

f = open("math", "r")
for x in f:
    print(x)

os.remove("math")
