
## O desafio
Essa pasta surgiu quando um colega de turma falou de um problema que ele tinha: Sem muitos detalhes,
> É um problema bobo até, tenho 2 listas com CPF e nome, ai quero comparar os cpfs, e devolver uma terceira com os nomes dos cpfs que estão em uma e não na outra

O plano inicial dele era usar [pandas](https://media3.giphy.com/media/ZebTmyvw85gnm/source.gif), já até havia começado mas acreditava que era um exagero. 
Estava usado o `in` e `listas` mesmo. 

Sugeri primeiro set(), bastaria transformar as duas listas em conjunto e pedir a negação da segunda. Seria um bom exercício, afinal
>Set é uma ferramenta nativa do Python, ideia muito interessante, mas até agora só me serviu para 1. Exemplificar exercícios de Matemática Discreta 2. Remover itens repetidos de uma lista. 

Depois pensei em uma outra ideia: Dicionários. Eu amo dicionários.
> Você também pode fazer um dicionário que recebe o CPF como chave e um dicionário como valor. O novo dicionário vai ter três chaves: o nome, se está na primeira lista e se está na segunda lista. E depois filtrar as chaves específicas. 

> Ainda que seja mais linhas de código, vai diminuir a complexidade do seu algoritmo de n×m  para n+m

> Ou melhor ainda: ao rodar a lista1 já ir botando Falso no valor booleano

Faltava detalhes importantes: A lista está ordenada? Todos os valores da primeira lista estão na segunda? A lista é muito grande? Mas topei o desafio e tentei implementar as minhas duas soluções propostas + duas que envolviam listas.

## Gerando o dataset
Primeiro de tudo eu precisava de uma lista para trabalhar, criei a minha então: Mesclei algumas listas de nomes disponíveis na internet e obtive uma lista universo de 20 mil nomes sem repetição. Apesar de conhecer a lógica por trás da criação dos CPFs, optei por algo mais simples, atribuindo a todos os nomes um pseudo-cpf de 10000+<o número da linha>. Como pode ser visto no exemplo.
```
26487,Romar
26488,Rome
26489,Romeka
26490,Romel
26491,Romelia
26492,Romell
26493,Romeo
26494,Romero
```
Como lista selecionada, meu algoritmo sorteou 3450 itens da lista Universo, o que representa 17,25% do Universo.  Sem saber se os dados estariam ordenados, criei dois novos arquivos embaralhando os dois conjuntos.

## Resultados obtidos
Consegui fazer os algoritmos com relativa facilidade. Curiosamente, não vi necessidade de separar os itens do csv em nenhum momento, todas as comparações foram feitas tratando cpf,nome como uma única string. 

Tal como eu havia previsto, o algoritmo que procurava os itens do Universo na Seleção teve um desempenho bastante inferior, mas todos os demais foram bem rápidos. Precisava saber qual dos demais então tinha um desempenho melhor. O ComDicionário tinha O(s+u), o ListaOrdenada tinha O(u), o ComConjunto, se entendi [esse artigo](https://pt.stackoverflow.com/questions/306024/como-pode-a-busca-de-um-elemento-em-um-conjunto-ser-o1) também tem O(u).

Tentei obter o tempo de execução deles com o `timeit`, mas não obtive sucesso. Optei por uma solução mais bruta e conhecidamente problemática o time.time(), tal como comentado a exaustão na internet, o resultado foi bem díspare.

Após terminar o código e reler a conversa para redigir esse README, notei que em nenhum momento foi citado que um csv é incluso no outro. Talvez esse git receba novos commits em breve.



