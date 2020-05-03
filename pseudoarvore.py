from tkinter import *
#Troca os rótulos de dois nós ou adiciona uma string y ao nó x. 
#As variáveis r e c são de controle interno, não há necessidade de mexer nelas
def Troca(x, y='', r=1, c=1):
    if isinstance(y, Label):
        aux=x['text']
        x['text']=y['text']
        y['text']=aux
    else:
        x['text']=str(y)
    cont['o']+=c
    if (r): log.append(('t', y, x))
    print(cont)

#imprime o log de ações feitas.
def l():
    for k in log: print(k)

#Remove a raiz da árvore para uma fila.
def add():
    sort.append(A1['text'])
    #Troca(A1, lista1[-len(sort)])
    Troca(A1, r=0)
    Troca(lista1[cont['pointer']], A1, r=0)
    #Troca(A1, lista1[-len(sort)])
    topo['text']=sort
    log.append(('r', ))
    cont['pointer']-=1
    cont['o']+=1
    print(cont)

#Basicamente, Ctrl+Z
def z():
    LastOp=log.pop()
    print('desfazendo ',end=' ')
    if LastOp[0]=='t':
        print('troca')
        Troca(LastOp[1], LastOp[2], 0, -1)
    else:
        print('add')
        x=sort.pop()
        cont['pointer']+=1
        Troca(A1, lista1[cont['pointer']], 0, -1)
        Troca(A1, x, 0, -1)
        topo['text']=sort

#Seria utilizado para deixar nós invisíveis, mas não foi necessário.
def show(no):
    #pega as posições de x e y
    x, y = float(no.place_info()['relx']), float(no.place_info()['rely'])
    addy=-1
    if x<1: addy=1 #está invisível
    x+=addy
    y+=addy
    no.place(relx=x, rely=y)
    #no.place('rely')+=2

#Reseta o programa
def reset():
    log=[]
    for k in range(len(lista1)): Troca(lista1[k], lista2[k], c=0)
    cont={'o':0, 'pointer':8}
    sort=[]
    topo['text']=sort

cont={'o':0, 'pointer':8}
h=0.05
janela=Tk()
A1=Label(janela, text='A1')
A1.place(relx=0.5, rely=0.1)

#Altura 2
h+=0.2
A2=Label(janela, text='A2')
A2.place(relx=0.25, rely=0.3)
A3=Label(janela, text='A3')
A3.place(relx=0.75, rely=0.3)

#Altura 3
h+=0.3
A4=Label(janela, text='A4')
A4.place(relx=1/8, rely=h)
A5=Label(janela, text='A5')
A5.place(relx=3/8, rely=h)
A6=Label(janela, text='A6')
A6.place(relx=5/8, rely=h)
A7=Label(janela, text='A7')
A7.place(relx=7/8, rely=h)

#Altura 4
h+=0.15
A8=Label(janela, text='A8')
A8.place(relx=1/16, rely=h)
A9=Label(janela, text='A9')
A9.place(relx=3/16, rely=h)

sort=[]
topo=Label(janela, bg='yellow')
topo.pack(fill=X)
janela.geometry('300x300+800+200')

lista1=[A1, A2, A3, A4, A5, A6, A7, A8, A9]
lista2=[45, 34, 78, 90, 12, 57, 80, 56, 15]
log=[]
reset()
