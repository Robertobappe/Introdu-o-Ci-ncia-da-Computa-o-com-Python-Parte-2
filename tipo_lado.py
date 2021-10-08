class Triangulo:
    def __init__(t,a,b,c):
        t.a=a
        t.b=b
        t.c=c
        t.tipo_lado()
    def tipo_lado(t):
        if t.a==t.b==t.c:
            return 'equilátero'
        elif t.a==t.b or t.a==t.c or t.b==t.c:
            return 'isósceles'
        else:
            return 'escaleno'
    
        
