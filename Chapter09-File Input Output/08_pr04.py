with open("sampal.txt") as f:
    content = f.read()

content = content.replace('donky', '$%^@#$^#')
print(content)

with open("sampal.txt",'w') as f:
    f.write(content)
    print(content)