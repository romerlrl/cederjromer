Esse é um desafio clássico da computação: 

<pre>Dados n pontos no plano, determinar dois deles que estão à distância mínima</pre>
A solução por força bruta tem complexidade de O(n²) e envolve testar a distância de todos os nós.
A solução ótima é uma abordagem por divisão e conquista que envolve dividir o plano em diversas metades recursivamente sempre procurando a menor distância entre elas, ao contrário da opção mais comum, este exercício devolve todos os pontos que tem um vizinho com a distância mínima.
<pre>
procedimento menorcaminho(pontos)
  pontos.ordenarPontosPorEixoX()
  vencedores←[]
  lebre←1
  tartaruga←0
  distancia←∞
  para tartaruga←0 até tamanho(pontos)
    lebre←tartaruga
    enquanto lebre<0
      corrida←pontos[lebre][0]-pontos[tartaruga][0]
      se corrida>distancia
        lebre←0
      senao
        corrida←hipotenusa(pontos[lebre][0],pontos[tartaruga][0])
        se corrida = distancia
          adiciona(todos, pontos[lebre][0], pontos[tartaruga][0])
        se corrida< distancia
          esvazia(todos)
          adiciona(todos, pontos[lebre][0], pontos[tartaruga][0])
        lebre++
  devolve todos  
</pre>
Além disso o algoritmo conta com uma função para tirar a distância entre os dois pontos que usa o teorema de pitágoras.

Para a melhor visualização, foi elaborado com o tkinter um grid que destaca tais pontos em vermelho e com um pequeno círculo em sua volta. Todos os pontos porém possuem uma circunferência de raio igual a distância mínima que ajuda a destacar um erro de algoritmo, se houver alguém ponto dentro da esfera de um círculo preto, significa que tem algo de errado.
