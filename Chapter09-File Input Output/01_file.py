# f = open("sampal.txt","r")
f = open("sampal.txt",) # By default the mode is r
# data = f.read()
data = f.read(5)# first 5 character from the file
print(data)
f.close()