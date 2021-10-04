def maiusculas(frase):
    a=frase
    b=len(a)
    c=[]

    for i in range(b):
        if a[i]==a[i].lower():
            i+=1
        else:
            c.append(a[i])
    i=0
    b=len(c)
    s=''

    for i in range(b):
        s+=c[i]
    return s
        
    
            

        
        
