import time
import datetime


def hora():
    import time
    hora = time.localtime(time.time())
    hora=list(hora)
    data=[str(x) for x in hora[:3:-1]]
    data="/".join(data)
    hora2=[str(x) for x in hora[3:6]]
    hora2=":".join(hora2)
    data+="  " + hora2
    return data

def ComDicionario():
    universo=open('lista20k.csv', 'r', encoding='utf-8')
    selecao=open('lista3k.csv', 'r', encoding='utf-8')

    objetivo='saida-metodo-dicionarios.txt'
    saida=open(objetivo, 'w', encoding='utf-8')
    dicio=dict()
    for k in universo:
        dicio[k]=True
    for k in selecao:
        dicio[k]=False
    for k, v in dicio.items():
        if v: saida.write(k)
    saida.close()
    universo.close()
    selecao.close()


def ComConjunto():
    universo=open('lista20k.csv', 'r', encoding='utf-8')
    selecao=open('lista3k.csv', 'r', encoding='utf-8')

    objetivo="saida-metodo-conjuntos.txt"
    saida=open(objetivo, 'w', encoding='utf-8')
    set_universo=set(universo.readlines())
    set_selecao=set(selecao.readlines())
    set_invertido=set_universo-set_selecao
    lista=list(set_invertido)
    for item in lista:
        saida.write(item)
    saida.close()
    universo.close()
    selecao.close()


def ComListaOrdenada():
    universo=open('lista20k.csv', 'r', encoding='utf-8')
    selecao=open('lista3k.csv', 'r', encoding='utf-8')
    objetivo='saida-metodo-listaOrdenada.txt'
    saida=open(objetivo, 'w', encoding='utf-8')
    foo=str()
    itemUniverso=universo.readline()
    itemSelecao=selecao.readline()
    while itemSelecao!="29996,Treena":
        if itemSelecao==itemUniverso:
            itemSelecao=selecao.readline()
        else:
            saida.write(itemUniverso)
        itemUniverso=universo.readline()
    #print("OK")

    while itemUniverso!="29999,Trellis":
        itemUniverso=universo.readline()
        saida.write(itemUniverso)
    saida.close()
    universo.close()
    selecao.close()

def ComListaNaoOrdenada():
    def SeNao(foo):
        for j in selecao2:
            if j==foo: return False
        saida.write(foo)

    
    caminhoUniverso=(f"lista20k{'r'*ordenado[0]}.csv")
    caminhoSelecao=(f"lista3k{'r'*ordenado[0]}.csv")
    
    universo=open(caminhoUniverso, 'r', encoding='utf-8')
    selecao=open(caminhoSelecao, 'r', encoding='utf-8')

    objetivo='saida-metodo-lista-nao-ordenada.txt'
    saida=open(objetivo, 'w', encoding='utf-8')
    print("Ok")
    selecao2=selecao.readlines()
    for k in xrange(20000):
        u=universo.readline()
        uf=u[2:8]
        SeNao(u)
    saida.close()
    universo.close()
    selecao.close()


def main(operacao):
    soma=0
    if operacao==ComListaNaoOrdenada: ordenado[0]=not(ordenado[0])
    for k in range(10):
        inicio=time.time()
        operacao()
        fim=time.time()
        fim-=inicio
        soma+=fim
        print(fim)
    print("-"*15)
    print(fim)
    
    '''
    t= timeit.Timer("operacao", "from __main__ import operacao")
    resultado.write(hora())
    resultado.write(t.repeat())
    
    #diff=final-time
    mysetup=str(operacao)
    print (timeit.timeit(setup = mysetup, stmt = operacao, number = 100) )
    
    universo.close()
    selecao.close()
    resultado.close()
    '''
ordenado=[False]
