with open('q11.txt','a+') as f:
    f.seek(0)
    output1=f.read()
    print(output1)
    f.write('789')