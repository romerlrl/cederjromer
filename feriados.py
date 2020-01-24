#exercício treinando o uso da biblioteca datetime
def printmoda(string, n, DIAS):
    if n > 4:
        print(string, "cai tudo no final de semana")
    else:
        print(string, "cai tudo na ", DIAS[n])
    return None

from datetime import date
from statistics import mode
DIAS = [
    'Segunda-feira', #0
    'Terça-feira',   #1
    'Quarta-feira',  #2
    'Quinta-Feira',  #3
    'Sexta-feira',   #4
    'Sábado',        #5
    'Domingo'        #6
]
listaoriginal=[]
ano=int(input())
indice_da_semana = []
dia256 = 13 - bool(ano % 4)
feriados = [["Ano novo", 1, 1],
            ["Tiradentes", 21, 4],
            ["São Jorge", 23, 4], 
            ["Dia do Trabalhador", 1, 5],
            ["Ariversário", 6, 9], 
            ["Independência", 7, 9],
            ["Dia do Programador", int(dia256), 9],
            ["Dia de Nossa Senhora Aparcida", 12, 10], 
            ["Finados", 2, 11],
            ["Zumbi", 20, 11]]
#if not (ano % 4): feriados += ["Natal", 25, 12]
for i in feriados:
    data = date(year=ano, month=i[2], day=i[1])
    indice_da_semana.append(data.weekday())
    print("{} ({}/{})".format(i[0], i[1], i[2]),
          DIAS[indice_da_semana[-1]])
moda = mode(indice_da_semana)
if moda == 0 or moda == 4:
    printmoda("Feriadão!", moda, DIAS)
elif moda == 1 or moda == 3:
    printmoda("Vai enforcar?", moda, DIAS)
elif moda == 2:
    printmoda("Pelo menos um descanso no meio da semana", moda, DIAS)
else:
    printmoda("GRR", moda, DIAS)
