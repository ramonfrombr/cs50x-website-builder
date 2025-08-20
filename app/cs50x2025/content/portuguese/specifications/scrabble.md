# Scrabble

![Tabuleiro de Scrabble](https://cs50.harvard.edu/x/2024/psets/2/scrabble/scrabble.png)

## Problema a Resolver

No jogo [Scrabble](https://scrabble.hasbro.com/en-us/rules), os jogadores criam palavras para ganhar pontos e o número de pontos é a soma dos valores das letras na palavra.

| A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   | O   | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 3   | 3   | 2   | 1   | 4   | 2   | 4   | 1   | 8   | 5   | 1   | 3   | 1   | 1   | 3   | 10  | 1   | 1   | 1   | 1   | 4   | 4   | 8   | 4   | 10  |

Por exemplo, se quisermos marcar a palavra "CODE", notaremos que 'C' vale 3 pontos, 'O' vale 1 ponto, 'D' vale 2 pontos e 'E' vale 1 ponto. Somando-os, obtemos que "CODE" vale 7 pontos.

Em um arquivo chamado `scrabble.c` em uma pasta chamada `scrabble`, implemente um programa em C que determine o vencedor de um curto jogo tipo Scrabble. O programa deve solicitar duas inserções: uma vez para "Jogador 1" inserir a palavra e uma vez para "Jogador 2" inserir a palavra. Então, dependendo de qual jogador marcou mais pontos, o programa deve imprimir "Jogador 1 venceu!", "Jogador 2 venceu!" ou "Empate!" (no caso de os dois jogadores marcarem a mesma quantidade de pontos).

## Demonstração

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-74B4kq3ftleKe6AdN0NxFV8CN" src="https://asciinema.org/a/74B4kq3ftleKe6AdN0NxFV8CN.js"></script>

## Dicas

### Escreva algum código que você saiba que irá compilar

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {

    }

Perceba que agora você incluiu alguns arquivos de cabeçalho que darão acesso a funções que podem ajudar a resolver este problema.

### Escreva um pseudocódigo antes de escrever mais código

Se você não tiver certeza de como resolver o problema em si, divida-o em problemas menores que você provavelmente possa resolver primeiro. Por exemplo, este problema é na verdade apenas um punhado de problemas:

1.  Solicitar ao usuário duas palavras
2.  Computar a pontuação de cada palavra
3.  Imprimir o vencedor

Vamos escrever alguns pseudocódigos como comentários para lembrá-lo de fazer exatamente isso:

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Solicitar ao usuário duas palavras

        // Computar a pontuação de cada palavra

        // Imprimir o vencedor
    }

<div class="alert alert-warning" data-alert="warning" role="alert"><p>Alguns problemas em conjuntos de problemas, como este, podem conter spoilers (como o próximo) que, em última análise, orientam você por toda a solução. Embora você tenha permissão para usar este código, nós realmente o encorajamos a tentar as coisas sozinho primeiro! Os outros problemas no conjunto de problemas não terão este tipo de orientação e, normalmente, o problema que contém o "spoiler completo" é uma versão de aquecimento do problema maior que você precisará resolver posteriormente.</p></div>

### Converter o pseudocódigo em código

Primeiro, considere como você pode solicitar ao usuário duas palavras. Lembre-se de que `get_string`, uma função na biblioteca CS50, pode solicitar ao usuário uma string.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Solicitar ao usuário duas palavras
        string palavra1 = get_string("Jogador 1: ");
        string palavra2 = get_string("Jogador 2: ");

        // Computar a pontuação de cada palavra

        // Imprimir o vencedor
    }

Em seguida, considere como calcular a pontuação de cada palavra. Como o mesmo algoritmo de pontuação se aplica a ambas as palavras, você tem uma boa oportunidade de _abstração_. Aqui, definiremos uma função chamada `compute_score` que pega uma string, chamada `word`, como entrada e, em seguida, retorna a pontuação da `word` como um `int`.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    int compute_score(string palavra);

    int main(void)
    {
        // Solicitar ao usuário duas palavras
        string palavra1 = get_string("Jogador 1: ");
        string palavra2 = get_string("Jogador 2: ");

        // Computar a pontuação de cada palavra
        int pontuacao1 = compute_score(palavra1);
        int pontuacao2 = compute_score(palavra2);

        // Imprimir o vencedor
    }

    int compute_score(string palavra)
    {
        // Computar e retornar pontuação para palavra
    }

Agora mude para implementar `compute_score`. Para calcular a pontuação de uma palavra, você precisa saber o valor do ponto de cada letra na palavra. Você pode associar letras e seus valores de pontos a um _array_. Imagine um array de 26 `int`, chamado `POINTS`, no qual o primeiro número é o valor do ponto para 'A', o segundo número é o valor do ponto para 'B' e assim por diante. Ao declarar e inicializar esse array fora de qualquer função individual, você pode garantir que esse array esteja acessível a qualquer função, incluindo `compute_score`.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    // Pontos atribuídos a cada letra do alfabeto
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int compute_score(string word);

    int main(void)
    {
        // Solicita ao usuário por duas palavras
        string word1 = get_string("Jogador 1: ");
        string word2 = get_string("Jogador 2: ");

        // Calcula a pontuação de cada palavra
        int score1 = compute_score(word1);
        int score2 = compute_score(word2);

        // Imprime o vencedor
    }

    int compute_score(string word)
    {
        // Calcula e retorna a pontuação da palavra
    }

Para implementar `compute_score`, primeiro tente encontrar o valor do ponto de uma única letra em `word`.

- Lembre-se de que para encontrar o caractere no índice enésimo de uma string, `s`, você pode escrever `s[n]`. Portanto, `word[0]`, por exemplo, fornecerá o primeiro caractere de `word`.
- Agora, lembre-se de que os computadores representam caracteres usando [ASCII](http://asciitable.com/), um padrão que representa cada caractere como um número.
- Lembre-se também que o índice 0 de `POINTS`, `POINTS[0]`, fornece o valor do ponto de 'A'. Pense em como você pode transformar a representação numérica de 'A' no índice do seu valor de ponto. Agora, e quanto a 'a'? Você precisará aplicar transformações diferentes para letras maiúsculas e minúsculas, portanto, pode achar as funções [`isupper`](https://manual.cs50.io/3/isupper) e [`islower`](https://manual.cs50.io /3/islower) para ser útil para você.
- Tenha em mente que caracteres que _não são_ letras devem receber zero pontos. Por exemplo, `!` vale 0 pontos.

Se você conseguir calcular adequadamente o valor de _um_ caractere em `words`, é provável que possa usar um loop para somar os pontos dos demais caracteres. Depois de tentar o acima por conta própria, considere esta dica (bastante reveladora!) abaixo.

    #include <ctype.h>
    #include <cs50.h>
    #include <stdio.h>
    #include <string.h>

    // Pontos atribuídos a cada letra do alfabeto
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int compute_score(string word);

    int main(void)
    {
        // Solicita ao usuário por duas palavras
        string word1 = get_string("Jogador 1: ");
        string word2 = get_string("Jogador 2: ");

        // Calcula a pontuação de cada palavra
        int score1 = compute_score(word1);
        int score2 = compute_score(word2);

        // Imprime o vencedor
    }

    int compute_score(string word)
    {
        // Mantém o controle da pontuação
        int score = 0;

        // Calcula a pontuação para cada caractere
        for (int i = 0, len = strlen(word); i < len; i++)
        {
            if (isupper(word[i]))
            {
                score += POINTS[word[i] - 'A'];
            }
            else if (islower(word[i]))
            {
                score += POINTS[word[i] - 'a'];
            }
        }

        return score;
    }

