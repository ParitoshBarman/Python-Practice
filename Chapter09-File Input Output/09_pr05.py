words = ['donky','kaddu', 'mote']




with open("sampal.txt") as f:
    content = f.read()



for word in words:
    content = content.replace(word, '$%^@#$^#')


with open("sampal.txt",'w') as f:
    f.write(content)
    