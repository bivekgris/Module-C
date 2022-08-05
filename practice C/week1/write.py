with open('file0.txt','r+') as f:
    f.write('from write')
    f.write(' ')
    print(f.read())