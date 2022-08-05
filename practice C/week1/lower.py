with open('file1.txt', 'r') as f:
    a=f.read()

print(a)

a=a.lower()
print(a)

with open('file1.txt','w') as f:
    f.write(a)
    