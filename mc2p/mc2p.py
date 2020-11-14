from math import inf, hypot, sqrt

def pitagoras(no1, no2):
    #a soma dos quadrados dos catetos é igual a raiz quadrada da hipotenusa
    eixoX=abs(no1[0]-no2[0])
    eixoY=abs(no1[1]-no2[1])
    return int(hypot(eixoX, eixoY))

def operacao(L):
    LX=sorted(L)
    LX.append(None)
    distanciaInicial=pitagoras(L[0], L[1])
    candidatosH=set()
    candidatosV=set()
    ponteiroTartaruga=0
    todos=[]
    ponteiroLebre=1
    #while LX[ponteiroLebre]!=None:
    for ponteiroTartaruga in range(len(LX)-1):
        ponteiroLebre=ponteiroTartaruga+1
        while LX[ponteiroLebre]!=None:
            corrida=LX[ponteiroLebre][0]-LX[ponteiroTartaruga][0]
            if (corrida)>distanciaInicial:
                ponteiroTartaruga+=1
                ponteiroLebre=-2
            else:
                #candidatosH.add((LX[ponteiroTartaruga], LX[ponteiroLebre]))
                corrida=pitagoras(LX[ponteiroTartaruga], LX[ponteiroLebre])
                if corrida<=distanciaInicial:
                    if corrida<distanciaInicial:
                        todos=[]
                        distanciaInicial=corrida
                    print(f"Empate {corrida}")
                    todos.append(LX[ponteiroTartaruga])
                    todos.append(LX[ponteiroLebre])                
                    print(f"Novo recorde \o/")
                    #dupla=(LX[ponteiroTartaruga], LX[ponteiroLebre])
                    
                    
            ponteiroLebre+=1
        
    return todos, distanciaInicial  
