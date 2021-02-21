file1 = 'copy.txt'
file2 = 'this.txt'

with open(file1) as f1:
    f1 = f1.read()
with open(file2) as f2:
    f2 = f2.read()


if f1 == f2:
    print('Files are identical')
else:
    print('Files are not identical')