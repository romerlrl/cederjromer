from tkinter import *
from listas import L400 as base
from mc2p import *

canvas_width = 1300
canvas_height = 650

#base=[(376, 512), (133, 357), (417, 360), (586, 498), (371, 127), (582, 510), (365, 593), (508, 125), (154, 297), (474, 579), (220, 451), (160, 212), (469, 193), (137, 594), (304, 190), (528, 310), (557, 559), (339, 298), (429, 430), (348, 292)]
#base=[(100, 100), (101, 300), (300, 101), (140, 130)]

def criaPonto(x0, y0, r, color='black'):
    ri=3
    d = C.create_oval(x0+ri, y0+ri, x0-ri, y0-ri, fill=color)
    d2= C.create_oval(x0+r, y0+r, x0-r, y0-r)

#base=L90l
master = Tk()
master.title("Points")
C = Canvas(master,
           width=canvas_width,
           height=canvas_height)
C.pack(expand=YES, fill=BOTH)

message = Label(master, text="Os mais próximos estarão em vermelho.")
message.pack(side=BOTTOM)
calculando=operacao(base[::])
print("Calculando: ", calculando[1])
for x, y in base:
    criaPonto(x, y, calculando[1])
for item in calculando[0]:
    x, y = item
    criaPonto(x, y, 5, 'red')
mainloop()

