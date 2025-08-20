**Recuperar**

![Imagem recuperada](https://cs50.harvard.edu/x/2024/psets/4/recover/img recuperada.png)

## Problema a Resolver

Prevendo esse problema, passamos os últimos dias tirando fotos pelo campus. Todas elas foram salvas em uma câmera digital como JPEGs em um cartão de memória. Infelizmente, de alguma forma as excluímos todas! Felizmente, no mundo da computação, “excluído” tende a não significar “deletado” e sim “esquecido”. Apesar da câmera insistir que o cartão está em branco, temos certeza que isso não é verdade. Na verdade, esperamos (ou melhor, contamos!) que você escreva um programa que recupere as fotos para nós!

Em um arquivo denominado `recuperar.c` em uma pasta chamada `recuperar`, escreva um programa para recuperar JPEGs de um cartão de memória.

## Código de Distribuição

Para este problema, você estenderá a funcionalidade do código fornecido pela equipe do CS50.

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd` sozinho. Você deve descobrir que o prompt da janela do terminal se assemelha ao abaixo:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/4/recover.zip

para baixar um ZIP chamado `recover.zip` em seu espaço de códigos.

Em seguida, execute

    unzip recover.zip

para criar uma pasta chamada `recuperar`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm recover.zip

e responder com “y” seguido por Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd recuperar

seguido por Enter para se mover para (ou seja, abrir) esse diretório. Agora seu prompt deve se parecer com o abaixo.

    recuperar/ $

Execute `ls` sozinho e você deverá ver dois arquivos: `recuperar.c` e `cartão.raw`.

## Histórico

Embora os JPEGs sejam mais complicados do que os BMPs, os JPEGs têm “assinaturas”, padrões de bytes que podem diferenciá-los de outros formatos de arquivo. Especificamente, os três primeiros bytes dos JPEGs são

    0xff 0xd8 0xff

do primeiro ao terceiro byte, da esquerda para a direita. O quarto byte, por sua vez, é `0xe0`, `0xe1`, `0xe2`, `0xe3`, `0xe4`, `0xe5`, `0xe6`, `0xe7`, `0xe8`, `0xe9`, `0xea`, `0xeb`, `0xec`, `0xed`, `0xee`, ou `0xef`. Dito de outra forma, os primeiros quatro bits do quarto byte são `1110`.

Provavelmente, se você encontrar esse padrão de quatro bytes em uma mídia conhecida por armazenar fotos (por exemplo, meu cartão de memória), eles demarcarão o início de um JPEG. Para ser justo, você pode encontrar esses padrões em alguns discos por puro acaso, então a recuperação de dados não é uma ciência exata.

Felizmente, as câmeras digitais tendem a armazenar fotografias contíguas em cartões de memória, pelo que cada fotografia é armazenada imediatamente após a fotografia tirada anteriormente. Consequentemente, o início de um JPEG geralmente demarca o fim de outro. No entanto, às vezes as câmeras digitais inicializam os cartões com um sistema de arquivos FAT cujo “tamanho do bloco” é de 512 bytes (B). A implicação é que essas câmeras só gravam nesses cartões em unidades de 512 B. Uma foto de 1 MB (ou seja, 1.048.576 B) ocupa 1048576 ÷ 512 = 2048 “blocos” em um cartão de memória. Mas o mesmo acontece com uma foto que é, digamos, um byte menor (ou seja, 1.048.575 B)! O espaço desperdiçado no disco é chamado de “espaço morto”. Os investigadores forenses muitas vezes procuram no espaço morto por restos de dados suspeitos.

A implicação de todos esses detalhes é que você, o investigador, provavelmente pode escrever um programa que itera sobre uma cópia do meu cartão de memória, procurando pelas assinaturas de JPEGs. Cada vez que você encontrar uma assinatura, poderá abrir um novo arquivo para gravação e começar a preencher esse arquivo com bytes do meu cartão de memória, fechando o arquivo somente quando encontrar outra assinatura. Além disso, em vez de ler os bytes do meu cartão de memória um de cada vez, você pode ler 512 deles de cada vez em um buffer para fins de eficiência. Graças ao FAT, você pode confiar que as assinaturas de JPEGs serão “alinhadas em bloco”. Ou seja, você só precisa procurar por essas assinaturas nos primeiros quatro bytes de um bloco.

Perceba, é claro, que os JPEGs podem abranger blocos contíguos. Caso contrário, nenhum JPEG poderia ser maior que 512 B. Mas o último byte de um JPEG pode não estar no final de um bloco. Lembre-se da possibilidade de espaço morto. Mas não se preocupe. Como este cartão de memória era novo quando comecei a tirar fotos, é provável que tenha sido “zerado” (ou seja, preenchido com 0s) pelo fabricante, caso em que qualquer espaço morto será preenchido com 0s. Não há problema se esses 0s finais acabarem nos JPEGs que você recuperar; eles ainda devem ser visíveis.

Agora, eu só tenho um cartão de memória, mas há muitos de vocês! Então fui em frente e criei uma “imagem forense” do cartão, armazenando seu conteúdo, byte por byte, em um arquivo chamado `cartão.raw`. Para que você não perca tempo iterando sobre milhões de 0s desnecessariamente, eu só tirei os primeiros megabytes do cartão de memória. Mas você deve finalmente descobrir que a imagem contém 50 JPEGs.

## Especificação

Implemente um programa chamado `recuperar` que recupera JPEGs de uma imagem forense.

- Implemente seu programa em um arquivo denominado `recuperar.c` em um diretório denominado `recuperar`.
- Seu programa deve aceitar exatamente um argumento de linha de comando, o nome de uma imagem forense da qual recuperar JPEGs.
- Se o seu programa não for executado com exatamente um argumento de linha de comando, ele deve lembrar o usuário do uso correto e `main` deve retornar `1`.
- Se a imagem forense não puder ser aberta para leitura, o seu programa deve informar ao usuário sobre isso e `main` deve retornar `1`.
- Os arquivos gerados devem ser denominados `###.jpg`, onde `###` é um número decimal de três dígitos, começando com `000` para a primeira imagem e contando.
- Seu programa, se usar `malloc`, não deve vazar memória.

## Dicas

### Escreva um pseudocódigo antes de escrever mais código

Se não tiver certeza de como resolver o problema maior, divida-o em problemas menores que você provavelmente pode resolver primeiro. Por exemplo, este problema é realmente apenas um punhado de problemas:

1. Aceite um único argumento de linha de comando: o nome de um cartão de memória
2. Abra o cartão de memória
3. Enquanto houver dados para ler no cartão de memória
    1. Crie JPEGs a partir dos dados

Vamos escrever um pseudocódigo como comentários para lembrá-lo de fazer exatamente isso:

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Aceitar um único argumento de linha de comando

        // Abrir o cartão de memória

        // Enquanto houver dados para ler no cartão de memória

            // Criar JPEGs a partir dos dados
    }

### Converter o pseudocódigo para o código

Primeiro, considere como aceitar um único argumento de linha de comando. Se o usuário utilizar mal o programa, você deverá informá-lo sobre o uso correto do programa.

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Aceitar um único argumento de linha de comando
        if (argc != 2)
        {
            printf("Uso: ./recover ARQUIVO\n");
            return 1;
        }

        // Abrir o cartão de memória

        // Enquanto ainda houver dados para ler no cartão de memória

            // Criar JPEGs a partir dos dados
    }

Agora que você verificou o uso correto, você pode abrir o cartão de memória. Tenha em mente que você pode abrir `card.raw` programaticamente com `fopen`, como no exemplo abaixo.

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Aceitar um único argumento de linha de comando
        if (argc != 2)
        {
            printf("Uso: ./recover ARQUIVO\n");
            return 1;
        }

        // Abrir o cartão de memória
        FILE *card = fopen(argv[1], "r");

        // Enquanto ainda houver dados para ler no cartão de memória

            // Criar JPEGs a partir dos dados
    }

Você deve, é claro, verificar se o arquivo foi aberto adequadamente! Se não foi, informe ao usuário e saia do programa: nós deixaremos essa parte para você.

Em seguida, seu programa deve ler os dados do cartão que você abriu, até que não haja mais dados para ler. Ao longo do caminho, seu programa deve recuperar cada um dos JPEGs de `card.raw`, armazenando cada um como um arquivo separado no seu diretório de trabalho atual.

Primeiro, considere como ler `card.raw` até o final. Lembre-se que, para ler dados de um arquivo, você precisa armazenar temporariamente esses dados em um "buffer". E lembre-se também que `card.raw` armazena dados em blocos de 512 bytes. Como tal, você provavelmente desejará criar um buffer de 512 bytes para armazenar blocos de dados à medida que os lê sequencialmente. Uma maneira de fazer isso é usar o tipo `uint8_t` de `stdint.h`, que armazena exatamente 8 bits (1 byte). O tipo é chamado de `uint8_t` porque ele armazena um número inteiro sem sinal/positivo/não negativo que requer 8 bits de espaço (ou seja, um byte).

    #include <stdint.h>
    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Aceitar um único argumento de linha de comando
        if (argc != 2)
        {
            printf("Uso: ./recover ARQUIVO\n");
            return 1;
        }

        // Abrir o cartão de memória
        FILE *card = fopen(argv[1], "r");

        // Criar um buffer para um bloco de dados
        uint8_t buffer[512];

        // Enquanto ainda houver dados para ler no cartão de memória

            // Criar JPEGs a partir dos dados
    }

No entanto, provavelmente _não_ é a melhor ideia usar 512 como um ["número mágico"](../../../shorts/magic_numbers/) aqui. É provável que você possa melhorar ainda mais esse design!

Agora, considere como ler dados do cartão de memória. Por sua [página de manual](https://man.cs50.io/3/fread), `fread` retorna o número de bytes que leu, caso em que deve retornar `512` ou `0`, dado que `card.raw` contém alguns blocos de 512 bytes. Para ler cada bloco de `card.raw`, após abri-lo com `fopen`, é suficiente usar um loop como este.

    #include <stdint.h>
    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Aceitar um único argumento de linha de comando
        if (argc != 2)
        {
            printf("Uso: ./recover ARQUIVO\n");
            return 1;
        }

        // Abrir o cartão de memória
        FILE *card = fopen(argv[1], "r");

        // Criar um buffer para um bloco de dados
        uint8_t buffer[512];

        // Enquanto ainda houver dados para ler no cartão de memória
        while (fread(buffer, 1, 512, card) == 512)
        {
            // Criar JPEGs a partir dos dados

        }
    }

Assim, assim que `fread` retornar `0` (que é efetivamente `false`), seu loop terminará.

Finalmente, cabe a você determinar como criar programaticamente JPEGs à medida que continua lendo a partir de `card.raw`. Para isso, você pode achar o [passo a passo](/#walkthrough) abaixo útil.

Tenha em mente que seu programa deve numerar os arquivos que ele gera, nomeando cada um `###.jpg`, onde `###` é um número decimal de três dígitos a partir de `000` em diante. Faça amizade com [`sprintf`](https://man.cs50.io/3/sprintf) e observe que `sprintf` armazena uma string formatada em um local na memória. Considerando o formato `###.jpg` prescrito para o nome do arquivo JPEG, para quantos bytes você deve alocar para essa string? (Não se esqueça do caractere NUL!)

Para verificar se os JPEGs que seu programa gerou estão corretos, basta clicar duas vezes e dar uma olhada! Se cada foto aparecer intacta, sua operação provavelmente foi um sucesso!

E, claro, lembre-se de `fclose` cada arquivo que você abriu com `fopen`!

### Mantenha seu diretório de trabalho limpo

É provável que os JPEGs que o primeiro rascunho do seu código gerar não estejam corretos. (Se você abri-los e não vir nada, eles provavelmente não estão corretos!) Execute o comando abaixo para excluir todos os JPEGs em seu diretório de trabalho atual.

    rm *.jpg

Se você preferir não ser solicitado a confirmar cada exclusão, execute o comando abaixo.

    rm -f *.jpg

Apenas tome cuidado com o parâmetro `-f`, pois ele "força" a exclusão sem perguntar.

## Passo a Passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ooL0r_8N9ms?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Como testar

### Executando o programa

    ./recover card.raw

### Correção

    check50 cs50/problems/2024/x/recover

### Estilo

    style50 recover.c

## Como enviar

    submit50 cs50/problems/2024/x/recover

