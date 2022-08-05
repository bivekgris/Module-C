try:
    with open('q10.txt','x') as f:
        f.write('Hello!')
        output10=False
        
except:
    output10=True
    
print(output10)