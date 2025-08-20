## Legibilidade

![Capa de A Teia de Carlota](https://cs50.harvard.edu/x/2024/psets/2/readability/charlottes_web.jpg)

## Problema a resolver

De acordo com a [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), _A Teia de Carlota_, de E.B. White, tem uma leitura entre o segundo e o quarto anos e _O Doador_, de Lois Lowry, tem uma leitura entre o oitavo e o décimo segundo anos. O que, no entanto, significa que um livro tem um certo nível de leitura?

Bem, em muitos casos um especialista pode ler um livro e decidir a série (isto é, ano escolar) para a qual considera o livro mais indicado. No entanto, um algoritmo também poderá, provavelmente, descobrir isso!

Num ficheiro chamado `readability.c` numa pasta chamada `readability`, implementarás um programa que calcula aproximadamente o nível de escolaridade necessário para compreender o texto. O teu programa deve imprimir como saída “Nível X”, onde “X” é o nível de escolaridade calculado, arredondado para o inteiro mais próximo. Se o nível de escolaridade for 16 ou superior (equivalente ou superior ao nível de leitura de um caloiro), o teu programa deverá imprimir “Nível 16+” em vez de dar o número de índice exato. Se o nível de escolaridade for inferior a 1, o teu programa deverá imprimir “Antes do Nível 1”.

## Demonstração

<script async data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-2YTPtsNbRP2p4bD4drEjHaoRj" src="https://asciinema.org/a/2YTPtsNbRP2p4bD4drEjHaoRj.js"></script>

## Contexto

Então, que tipo de traços são característicos de níveis de leitura mais elevados? Bem, palavras mais longas provavelmente se correlacionam com níveis de leitura mais elevados. Da mesma forma, frases mais longas, provavelmente, também se correlacionam com níveis de leitura mais elevados.

Diversos “testes de legibilidade” foram desenvolvidos ao longo dos anos, que definem fórmulas para calcular o nível de leitura de um texto. Um desses testes de legibilidade é o _índice Coleman-Liau_. O índice Coleman-Liau de um texto foi concebido para imprimir o nível escolar que (nos EUA) é necessário para compreender determinado texto. A fórmula é

    índice = 0,0588 * L - 0,296 * S - 15,8

onde `L` é a média por número de caracteres por cada 100 palavras no texto e `S` é a média por número de frases por cada 100 palavras no texto.

## Conselhos

### Escreve algum código que saibas que vai compilar

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {

    }

Repara que incluíste agora alguns ficheiros de cabeçalho que te darão acesso a funções que te poderão ajudar a resolver este problema.

### Escreve algum pseudo código antes de escreveres mais código

Se não tiveres certeza de como resolver o problema, divide-o em problemas menores que provavelmente conseguirás resolver primeiro. por exemplo, este problema é, na verdade, apenas um punhado de problemas:

1.  Solicita algum texto ao utilizador
2.  Conta o número de caracteres, palavras e frases no texto
3.  Calcula o índice Coleman-Liau
4.  Imprime o nível de escolaridade

Vamos escrever algum pseudo código como comentários para te lembrar de fazer exatamente isso:

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Solicita algum texto ao utilizador

        // Conta o número de caracteres, palavras e frases no texto

        // Calcula o índice Coleman-Liau

        // Imprime o nível de escolaridade
    }

### Converta o pseudocódigo em código

Primeiro, pense como você poderia solicitar texto do usuário. Lembre-se de que `get_string`, uma função na biblioteca CS50, pode solicitar uma string ao usuário.

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
        // Solicite texto ao usuário
        string texto = get_string("Texto: ");

        // Conte o número de letras, palavras e sentenças no texto

        // Calcule o índice de Coleman-Liau

        // Imprima o nível da série
    }

Agora que você coletou dados do usuário, você pode começar a analisar esses dados. Primeiro, tente contar o número de letras no texto. Considere que as letras são caracteres alfabéticos em maiúsculas ou minúsculas, não pontuação, dígitos ou outros símbolos.

Uma maneira de abordar esse problema é criar uma função chamada `count_letters` que recebe uma string, `texto`, como entrada e, em seguida, retorna o número de letras nesse texto como um `int`.

    int count_letters(string texto)
    {
        // Retorne o número de letras no texto
    }

Você precisará escrever seu próprio código para contar o número de letras no texto. Mas alguém mais experiente do que você pode já ter escrito uma função para determinar se um caractere é alfabético. Esta é uma boa oportunidade para usar o [manual do CS50](https://manual.cs50.io/), uma coleção de explicações de funções comuns na Biblioteca Padrão C.

Você pode integrar `count_letters` ao código que você já escreveu, como a seguir.

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int count_letters(string texto);

    int main(void)
    {
        // Solicite texto ao usuário
        string texto = get_string("Texto: ");

        // Conte o número de letras, palavras e sentenças no texto
        int letras = count_letters(texto);

        // Calcule o índice de Coleman-Liau

        // Imprima o nível da série
    }

    int count_letters(string texto)
    {
        // Retorne o número de letras no texto
    }

Em seguida, escreva uma função para contar palavras.

    int count_words(string texto)
    {
        // Retorne o número de palavras no texto
    }

Para o propósito deste problema, consideraremos que qualquer sequência de caracteres separados por um espaço é uma palavra (portanto, uma palavra hifenizada como “cunhada” deve ser considerada uma palavra, não três). Você pode presumir que uma frase:

- conterá pelo menos uma palavra;
- não começará ou terminará com um espaço; e
- não terá vários espaços em uma fileira.

Sob essas suposições, você pode ser capaz de encontrar uma relação entre o número de palavras e o número de espaços. É claro que você é bem-vindo para tentar uma solução que tolerará vários espaços entre palavras ou, de fato, nenhuma palavra!

Agora você pode integrar `count_words` ao seu programa como a seguir:

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int count_letters(string texto);
    int count_words(string texto);

    int main(void)
    {
        // Solicite texto ao usuário
        string texto = get_string("Texto: ");

        // Conte o número de letras, palavras e sentenças no texto
        int letras = count_letters(texto);
        int palavras = count_words(texto);

        // Calcule o índice de Coleman-Liau

        // Imprima o nível da série
    }

    int count_letters(string texto)
    {
        // Retorne o número de letras no texto
    }

    int count_words(string texto)
    {
        // Retorne o número de palavras no texto
    }

Por fim, escreva uma função para contar sentenças. Você pode considerar qualquer sequência de caracteres que termine com um `.` ou um `!` ou um `?` como uma sentença.

    int count_sentences(string texto)
    {
        // Retorne o número de sentenças no texto
    }

Você pode integrar `count_sentences` em seu programa como a seguir:

    #include <ctype.h>
    #include <cs50.h>
    #include <math.h>
    #include <stdio.h>
    #include <string.h>

    int count_letters(string text);
    int count_words(string text);
    int count_sentences(string text);

    int main(void)
    {
        // Pede ao usuário por algum texto
        string text = get_string("Texto: ");

        // Conta o número de letras, palavras e frases no texto
        int letters = count_letters(text);
        int words = count_words(text);
        int sentences = count_sentences(text);

        // Calcula o índice de Coleman-Liau

        // Imprime o nível de ensino
    }

    int count_letters(string text)
    {
        // Retorna o número de letras no texto
    }

    int count_words(string text)
    {
        // Retorna o número de palavras no texto
    }

    int count_sentences(string text)
    {
        // Retorna o número de frases no texto
    }

Por fim, calcule o índice de Coleman-Liau e imprima o nível de ensino resultante.

- Recorde que o índice de Coleman-Liau é calculado usando `índice = 0,0588 * L - 0,296 * S - 15,8`
- `L` é a média de letras por 100 palavras no texto: ou seja, o número de letras dividido pelo número de palavras, tudo isso multiplicado por 100.
- `S` é a média de frases por 100 palavras no texto: ou seja, o número de frases dividido pelo número de palavras, tudo isso multiplicado por 100.
- Você vai querer arredondar o resultado para o número inteiro mais próximo, então recorde que `round` é declarado em `math.h`, por [manual.cs50.io](https://manual.cs50.io/).
- Recorde que, ao dividir valores do tipo `int` em C, o resultado também será um `int`, com qualquer resto (por exemplo, dígitos após a vírgula) descartado. Falando de outra forma, o resultado será "truncado". Talvez você queira converter um ou mais de seus valores para `float` antes de fazer a divisão ao calcular `L` e `S`!

Se o número do índice resultante for 16 ou mais (equivalente ou maior que o nível de leitura de um estudante universitário sênior), seu programa deve gerar "Nível 16+" ao invés de gerar um número de índice exato. Se o número do índice for menor que 1, seu programa deve gerar "Antes do Nível 1".

## Passo a Passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/AOVyZEh9zgE?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Como testar

Tente rodar seu programa com os textos a seguir, para garantir que você veja o nível de ensino especificado. Certifique-se de copiar apenas o texto, sem espaços extras.

- `Um peixe. Dois peixes. Peixe vermelho. Peixe azul.` (Antes do Nível 1)
- `Você gostaria deles aqui ou lá? Eu não gostaria deles aqui ou lá. Eu não gostaria deles em lugar algum.` (Nível 2)
- `Parabéns! Hoje é o seu dia. Você está partindo para Grandes Lugares! Você está de partida!` (Nível 3)
- `Harry Potter era um garoto muito incomum em muitas formas. Por um lado, ele odiava as férias de verão mais do que qualquer outra época do ano. Por outro, ele realmente queria fazer seu dever de casa, mas era forçado a fazê-lo em segredo, no meio da noite. E ele também era um bruxo.` (Nível 5)
- `Em meus anos mais jovens e vulneráveis, meu pai me deu um conselho que tenho refletido em minha mente desde então.` (Nível 7)
- `Alice estava começando a ficar muito cansada de sentar ao lado de sua irmã na margem, e de não ter nada para fazer: uma ou duas vezes ela tinha espiado o livro que sua irmã estava lendo, mas não tinha nem figuras nem diálogos, "e para que serve um livro", pensou Alice, "sem figuras ou diálogos?"` (Nível 8)
- `Quando ele tinha quase treze anos, meu irmão Jem quebrou o braço feio no cotovelo. Quando sarou, e os medos de Jem de nunca poder jogar futebol foram acalmados, ele raramente sentia vergonha por sua lesão. Seu braço esquerdo estava um pouco mais curto que o direito; quando ele ficava de pé ou andava, as costas de sua mão ficava em ângulo reto com seu corpo, seu polegar paralelo à sua coxa.` (Nível 8)
- `Há mais coisas no Céu e na Terra, Horácio, do que sonham em sua filosofia.` (Nível 9)
- `Era um dia frio de abril, e os relógios batiam treze horas. Winston Smith, seu queixo afundado em seu peito em um esforço para escapar do vento terrível, deslizou rapidamente pelas portas de vidro da Casa da Vitória, embora não rápido o suficiente para impedir que uma espiral de poeira entrasse junto com ele.` (Nível 10)
- `Uma grande classe de problemas computacionais envolve a determinação de propriedades de gráficos, dígrafos, inteiros, conjuntos de inteiros, famílias finitas de conjuntos finitos, fórmulas booleanas e elementos de outros domínios contáveis.` (Nível 16+)

### Correção

Em seu terminal, execute o comando abaixo para verificar a correção de seu trabalho.

    check50 cs50/problems/2024/x/readability

### Estilo

Execute o comando abaixo para avaliar o estilo de seu código usando `style50`.

    style50 readability.c

## Como enviar

Em seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2024/x/readability

