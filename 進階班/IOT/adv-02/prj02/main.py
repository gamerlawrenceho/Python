import os

print(os.listdir())
with open("test.txt", "w") as f:
    f.write("Hello, MicroPython")
print(os.listdir())
os.romve("test.txt")
print(os.listdir())