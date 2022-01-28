f = open("demofile.json", "a")
f.write("hello world")
f.close()

#open and read the file after the appending:
f = open("demofile.json", "r")
print(f.read())