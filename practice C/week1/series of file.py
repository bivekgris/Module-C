n=10

for i in range(1,n,1):
    a=f'q23_{i}.txt'
    try:
        with open(a,'r') as f:
            f.read()
    except:
        output2=False
    else:
        a=f'q23_{i}.txt'
        print(a)
    
    with open (a,'w') as f:
        f.write(str(i))
    
    with open (a,'r') as f:
        print(f.read())