from math import factorial
def combs(x, y):
  c=factorial(x)//(factorial(x-y)*factorial(y))
  return c

def coluna():
  entrada=int(input("Qual a linha que começa?"))
  saida=int(input("Qual a linha que termina?"))
  soma=False
  for a in range(entrada, saida):
    x=combs(a, entrada)
    soma+=x
    print(x, end=" ")
  print()
  print(soma)
  print(combs(a+1, entrada+1))
 
