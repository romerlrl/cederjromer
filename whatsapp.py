from statistics import multimode
#Funções para criar o dicionário
def encontranumero(x):
    #essa função define o remetente, se o remetente for um numero, blz, se não procura o nome dele
    z=34
    if not(x[18]=='5'):
        z=x.find(": ")
    return (x[17:z], x[z+2:])

def RemoveDuploEspaco(string):
  x=string.count("  ")
  for i in range(x, 2, -1):
    string=string.replace(" "*i, " ")
  return string    

def ContaPalavra(string):
    string=RemoveDuploEspaco(string)
    palavras=string.count(" ")+1
    caractere=len(string)
    return (palavras, caractere)

def VerificaMidia(string):
    return string=="<Arquivo de mídia oculto>"

def Menciona(string):
    lista=[]
    if "@" in string:
        string=string.split("@")
        for i in string:
            num=i[:13]
        if num.isdigit(): lista.append(num)
    if not(lista):lista=False
    return lista

def NovaMsg(string):
    x=(string[0:1] + string[3:4]+string[6:7]).isdigit()
    return x

def EntrouOuSaiu(string):
    entrou=(string[-43:]==("entrou usando o link de convite deste grupo") or ("adicionou" in string))
    saiu = string[-4:]==("saiu" in string or "removeu" in string) and not(":" in string)
    VorF=entrou+saiu
    return VorF

def conta():
    caminho = "C:/Users/lucas/Box Sync/CEDERJ/fp python/Whatsapp/input/jacarelog abriljan.txt"
    #Ari = 0
    Convidade = 0
    convidadenome=input()
    convidadenum=input()
    arinumb="APAGADO"
    tot=0
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for i in arquivo.readlines():
            #if i[16:34]==arinumb: Ari+=True
            if i[16:34]==convidadenum: Convidade+=True
            tot+=True
    print(convidadenome, Convidade)
    #print("Ari", Ari)

def DevolveDicio(linha):
    #if not(EntrouOuSaiu):
        #if NovaMsg(linha):
    data=linha[:8]
    hora=linha[9:14]
    remetente, string = encontranumero(linha)
    destinatario=Menciona(linha)
    if VerificaMidia(string):
        midia=True
        caracter=False
        palavra=False
        destinatario=False
    else:
        midia=False
        palavra, caracter = ContaPalavra(string)
    dicio_msg={
        'data':data,
        'hora':hora,
        'remetente':remetente,
        'destinatario':destinatario,
        'Caracteres':caracter,
        'Palavras':palavra,
        'midia':midia
                }
    print(dicio_msg)
    return dicio_msg

#Funções para ler o dicionário
def DiaMaisMovimentado(listamoda):
    valmoda=multimode(moda)
    totmoda=moda.count(valmoda[0])
    print(valmoda, totmoda)    
    
