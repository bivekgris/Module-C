with open ('file1.txt','r') as f:
    a=f.read()
    
print(a)
a=a.replace(a[9:13],'GOOD')
print(a)