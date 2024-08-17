# Ordenar

## Problema a resolver

Recorde das aulas que vimos alguns algoritmos para ordenar uma sequência de números: seleção por ordenação, ordenação por bolhas e ordenação por mesclagem.

- A seleção por ordenação itera sobre as partes não ordenadas de uma lista, selecionando o menor elemento de cada vez e movendo-o para sua localização correta.
- A ordenação por bolhas compara pares de valores adjacentes um de cada vez e os troca se estiverem na ordem incorreta. Isso continua até que a lista seja ordenada.
- A ordenação por mesclagem divide recursivamente a lista em duas repetidamente e, em seguida, mescla as listas menores de volta em uma maior na ordem correta.

Neste problema, você analisará três programas de ordenação (compilados!) para determinar quais algoritmos eles usam. Em um arquivo chamado `answers.txt` em uma pasta chamada `sort`, registre suas respostas, juntamente com uma explicação para cada programa, preenchendo os espaços em branco marcados como `TODO`.

## Código de distribuição

Para este problema, você precisará de algum "código de distribuição" - ou seja, código escrito pela equipe do CS50. São fornecidos três programas C já compilados, `sort1`, `sort2` e `sort3`, bem como vários arquivos `.txt` de entrada e outro arquivo, `answers.txt`, para você gravar suas respostas. Cada um de `sort1`, `sort2` e `sort3` implementa um algoritmo de ordenação diferente: seleção por ordenação, ordenação por bolhas ou ordenação por mesclagem (embora não necessariamente nessa ordem!). Sua tarefa é determinar qual algoritmo de ordenação é usado por cada arquivo. Comece baixando esses arquivos.

### Baixar arquivos de distribuição

Abra o [VS Code](https://cs50.dev/).

Comece clicando dentro da janela do terminal e execute `cd` sozinho. Você deve descobrir que seu "prompt" se assemelha ao abaixo.

    $

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2023/fall/psets/3/sort.zip

seguido por Enter para baixar um ZIP chamado `sort.zip` no seu codespace. Tome cuidado para não esquecer o espaço entre `wget` e a URL a seguir, ou qualquer outro caractere!

Agora execute

    unzip sort.zip

para criar uma pasta chamada `sort`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm sort.zip

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

## Dicas

### Explore os arquivos `.txt`

- Vários arquivos `.txt` são fornecidos para você. Esses arquivos contêm `n` linhas de valores, invertidos, embaralhados ou classificados.
  - Por exemplo, `reversed10000.txt` contém 10000 linhas de números que são invertidas de `10000`, enquanto `random50000.txt` contém 50000 linhas de números que estão em ordem aleatória.
- Os diferentes tipos de arquivos `.txt` podem ajudá-lo a determinar qual ordenação é qual. Considere como cada algoritmo é executado com uma lista já ordenada. Que tal uma lista invertida? Ou lista embaralhada? Pode ser útil trabalhar com uma lista menor de cada tipo e percorrer cada processo de ordenação.

### Cronometre cada ordenação com entradas diferentes

- Para executar as ordenações nos arquivos de texto, execute o seguinte no terminal: `./[nome_do_programa] [arquivo_de_texto.txt]`. Certifique-se de ter usado `cd` para mover para o diretório `sort`!
  - Por exemplo, para ordenar `reversed10000.txt` com `sort1`, execute `./sort1 reversed10000.txt`.
- Pode ser útil cronometrar suas ordenações. Para fazer isso, execute `time ./[arquivo_de_ordenacao] [arquivo_de_texto.txt]`.
  - Por exemplo, você pode executar `time ./sort1 reversed10000.txt` para executar `sort1` em 10.000 números invertidos. No final da saída do seu terminal, você pode olhar para o tempo `real` para ver quanto tempo realmente decorreu durante a execução do programa.

## Passo a passo

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/-Bhxxw6JKKY"></iframe>

<details><summary>Não sabe como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/uOYhrBs37j0"></iframe></details>

## Como testar

### Correção

    check50 cs50/problems/2024/x/sort

## Como enviar

    submit50 cs50/problems/2024/x/sort