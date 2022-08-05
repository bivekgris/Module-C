with open('q11.txt','a+') as f:
    f.write('\nGoofnight World')
    f.seek(0)
    print(f.read())
    