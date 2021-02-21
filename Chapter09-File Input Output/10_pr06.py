with open('log.txt') as f:
    content = f.read()

if 'python' in content.lower():
    print('Yes Python is present')
else:
    print('NO Python is not present')