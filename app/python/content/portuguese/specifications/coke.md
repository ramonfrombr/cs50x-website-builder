## Máquina de Coca-Cola

![Garrafa de Coca-Cola CS50](coke.png)

Suponha que uma máquina venda garrafas de Coca-Cola (Coke) por 50 centavos e aceite apenas moedas nessas denominações: 25 centavos, 10 centavos e 5 centavos.

Em um arquivo chamado `coke.py`, implemente um programa que solicite ao usuário que insira uma moeda, uma de cada vez, informando ao usuário o valor devido a cada vez. Quando o usuário tiver inserido pelo menos 50 centavos, exiba quanto de troco é oferecido ao usuário. Assuma que o usuário só irá inserir números inteiros e ignore qualquer número inteiro que não seja uma denominação aceita.

## Demonstração

## Antes de começar

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute o comando `cd`. Você verá que o prompt da janela do seu terminal é algo parecido com o seguinte:

    $

Em seguida, execute

    mkdir coke

para criar uma pasta chamada `coke` em seu espaço de codificação.

Depois, execute

    cd coke

para entrar nessa pasta. Agora você verá que seu prompt do terminal será `coke/ $`. Agora você pode executar

    code coke.py

para criar um arquivo chamado `coke.py`, onde você escreverá seu programa.

## Como Testar

Aqui está como testar o seu código manualmente:

- Execute o programa com `python coke.py`. No prompt `Insert Coin:`, digite `25` e pressione Enter. O seu programa deverá exibir:

      Amount Due: 25

  e continuar solicitando ao usuário por moedas.

- Execute o programa com `python coke.py`. No prompt `Insert Coin:`, digite `10` e pressione Enter. O seu programa deverá exibir:

      Amount Due: 40

  e continuar solicitando ao usuário por moedas.

- Execute o programa com `python coke.py`. No prompt `Insert Coin:`, digite `5` e pressione Enter. O seu programa deverá exibir:

      Amount Due: 45

  e continuar solicitando ao usuário por moedas.

- Execute o programa com `python coke.py`. No prompt `Insert Coin:`, digite `30` e pressione Enter. Seu programa deve exibir:

      Amount Due: 50

  porque a máquina não aceita moedas de 30 centavos! Seu programa deve então continuar solicitando ao usuário por moedas.

- Execute o programa com `python coke.py`. No prompt `Insert Coin:`, digite `25` e pressione Enter, depois digite `25` novamente e pressione Enter. Seu programa deve interromper e exibir:

      Change Owed: 0

- Execute o programa com `python coke.py`. No prompt `Insert Coin:`, digite `25` e pressione Enter, depois digite `10` e pressione Enter. Digite `25` novamente e pressione Enter, após o qual o seu programa deve interromper e exibir:

      Change Owed: 10

Você pode executar o abaixo para verificar o seu código usando o `check50`, um programa que a CS50 usará para testar o seu código quando você enviar. Mas certifique-se de testá-lo também por conta própria!

    check50 cs50/problems/2022/python/coke

Os smileys verdes significam que o seu programa passou em um teste! Os smileys vermelhos indicarão que o seu programa exibiu algo inesperado. Visite a URL que o `check50` exibe para ver a entrada que o `check50` entregou ao seu programa, qual saída esperada, e qual saída o seu programa realmente deu.

Dica:

Tenha cuidado para imprimir as mensagens e respostas exatamente como mostrado acima. Se o seu programa imprimir qualquer texto extra, ele pode falhar no `check50`.

## Como fazer a Submissão

No seu terminal, execute o comando abaixo para enviar o seu trabalho.

    submit50 cs50/problems/2022/python/coke
