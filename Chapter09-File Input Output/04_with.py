with open("annother.txt",'r') as f:
    a = f.read()

with open("annother.txt",'w') as f:
    a = f.write('me')
print(a)