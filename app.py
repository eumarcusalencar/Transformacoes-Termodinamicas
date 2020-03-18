def Isobarica():
    Ti=0
    Tf=0
    Vi=0
    Vf=0
    variaveis=[Ti,Tf,Vi,Vf]
    name=['Ti','Tf','Vi','Vf']
    print("Digite qual variável você deseja descobrir:\n1-Temperatura inicial\n2-Temperatura final\n3-Volume inicial\n4-Volume final")
    tipo=int(input())
    while tipo<1 or tipo>4:
        tipo=int(input("O valor inserido é inválido, digite novamente:"))
    cont=0
    for i in variaveis:
        if cont != tipo-1:
            print("digite o valor de",name[cont])
            valor=float(input())
            variaveis[cont]=valor
        cont+=1
    Ti=variaveis[0]
    Tf=variaveis[1]
    Vi=variaveis[2]
    Vf=variaveis[3]
    if Vi==0:
        print("O volume inicial é:",Ti*Vf/Tf)
    elif Ti==0:
        print("A temperatura inicial é:",Vi*Tf/Vf)
    elif Vf==0:
        print("O volume final é:",Vi*Tf/Ti)
    else:
        print("A temperatura final é:",Vf*Ti/Vi)

def Isotermica():
    Pi=0
    Pf=0
    Vi=0
    Vf=0
    print("Digite qual variável você deseja descobrir:\n1-Pressão inicial\n2-Pressão final\n3-Volume inicial\n4-Volume final")
    tipo=int(input())
    while tipo<1 or tipo>4:
        tipo=int(input("O valor inserido é inválido, digite novamente:"))
    variaveis=[Pi,Pf,Vi,Vf]
    name=['Pi','Pf','Vi','Vf']
    cont=0
    for i in variaveis:
        if cont != tipo-1:
            print("digite o valor de",name[cont])
            valor=float(input())
            variaveis[cont]=valor
        cont+=1
    Pi=variaveis[0]
    Pf=variaveis[1]
    Vi=variaveis[2]
    Vf=variaveis[3]
    if Vi==0:
        Vi=1
        print("O volume inicial é:",Pf*Vf/Pi)
    elif Pi==0:
        Pi=1
        print("A pressão inicial é:",Pf*Vf/Vi)
    elif Vf==0:
        Vf=1
        print("O volume final é:",Pi*Vi/Pf)
    else:
        Pf=1
        print("A pressão final é:",Pi*Vi/Vf)

def Isometrica():
    Pi=0
    Pf=0
    Ti=0
    Tf=0
    print("Digite qual variável você deseja descobrir:\n1-Pressão inicial\n2-Pressão final\n3-Temperatura inicial\n4-Temperatura final")
    tipo=int(input())
    while tipo<1 or tipo>4:
        tipo=int(input("O valor inserido é inválido, digite novamente:"))
    variaveis=[Pi,Pf,Ti,Tf]
    name=['Pi','Pf','Ti','Tf']
    cont=0
    for i in variaveis:
        if cont != tipo-1:
            print("digite o valor de",name[cont])
            valor=float(input())
            variaveis[cont]=valor
        cont+=1
    Pi=variaveis[0]
    Pf=variaveis[1]
    Ti=variaveis[2]
    Tf=variaveis[3]
    if Ti==0:
        Ti=1
        print("A temperatura inicial é:",Pi*Tf/Pf)
    elif Pi==0:
        Pi=1
        print("A pressão inicial é:",Ti*Pf/Tf)
    elif Pf==0:
        Pf=1
        print("A pressão final é:",Pi*Tf/Ti)
    else:
        Tf=1
        print("A temperatura final é:",Pf*Ti/Pi)
        
print("Tipos de transformações:\n1-Isobárica\n2-IsoTérmica\n3-Isométrica")
opcao=int(input("Digite qual tipo de transformação você deseja calcular: "))
if opcao==1:
    Isobarica()
if opcao==2:
    Isotermica()
if opcao==3:
    Isometrica()
