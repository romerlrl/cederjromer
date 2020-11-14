Esse é um desafio clássico da computação: 

<pre>Dados n pontos no plano, determinar dois deles que estão à distância mínima</pre>
A solução por força bruta tem complexidade de O(n²) e envolve testar a distância de todos os nós.
A solução ótima é uma abordagem por divisão e conquista que envolve dividir o plano em diversas metades recursivamente sempre procurando a menor distância entre elas.
<pre>
procedimento menorcaminho(pontos)
  pontos.ordenarPontosPorEixoX()
  vencedores←[]
  lebre←1
  tartaruga←0
  distanciaMinima←∞
  enquanto lebre≠nulo
    corrida=pontos[lebre][0]-pontos[tartaruga][0]
    se corrida>distanciaMinima
      tartaruga++
      lebre←tartaruga+1
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
Além disso o algoritmo conta com uma função para tirar a distância entre os dois pontos que usa o teorema de pitágoras
