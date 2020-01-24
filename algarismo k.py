'''
outro algoritmo que surgiu numa discussão entre colegas
dando um numero n e uma posição k, o algoritmo retorna 
o algorismo na posição k contada de trás para frente:
...4321
'''

import random

def pos(n, k):
  return (n%(10**k) //(10**(k-1)))

n=random.randint(10**19, 10**20)
print(n)
for p in range(1, 21):
  print(pos(n, p))
