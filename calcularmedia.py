##calcularmedia.py
##24/08/2023

alunos = int (input("quantos alunos tem a turma "))
i = 0
while i < alunos :
    n1 = float(input("diga a primeria nota "))
    n2 = float(input("diga a segunda nota "))
    n3 = float(input("diga a segunda nota "))

    if n2>n1:

        if n3>n1:
            n1 = n3

    if n1>n2:

        if n3>n2:
            n2 = n3
        
    if n1==n2:

        if n3>n2:
            n2 = n3
        
    x = (n1+n2) /2
    
    print("sua media é", x)
    
    y= x-6
    
    if x==6:
        print("PASSOU")
    if x>6:
        print("PASSOU COM", y, "DE FOLGA")
    if x<6:
        print("FALHOU")

    i+=1
    
