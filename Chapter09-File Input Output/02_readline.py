
f = open("sampal.txt",)
 
# Read first line
data = f.readline()
print(data)

# Read 2nd line
data = f.readline()
print(data)

# Read 3rd and so on......
data = f.readline()
print(data)
f.close()