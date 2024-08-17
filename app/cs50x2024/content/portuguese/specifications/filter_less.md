## Filtro

![Harvard Yard em escala de cinza](https://cs50.harvard.edu/x/2024/psets/4/filter/less/yard-grayscale.bmp)

## Problema a resolver

Talvez a maneira mais simples de representar uma imagem seja com uma grade de pixels (ou seja, pontos), cada um dos quais pode ser de uma cor diferente. Para imagens em preto e branco, precisamos, portanto, de 1 bit por pixel, pois 0 poderia representar preto e 1 poderia representar branco, como abaixo.

![um bitmap simples](https://cs50.harvard.edu/x/2024/psets/4/filter/less/bitmap.png)

Nesse sentido, então, uma imagem é apenas um bitmap (ou seja, um mapa de bits). Para imagens mais coloridas, você simplesmente precisa de mais bits por pixel. Um formato de arquivo (como [BMP](https://en.wikipedia.org/wiki/BMP_file_format), [JPEG](https://en.wikipedia.org/wiki/JPEG) ou [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)) que suporte "cores de 24 bits" usa 24 bits por pixel. (O BMP na verdade suporta cores de 1, 4, 8, 16, 24 e 32 bits.)

Um BMP de 24 bits usa 8 bits para significar a quantidade de vermelho na cor de um pixel, 8 bits para significar a quantidade de verde na cor de um pixel e 8 bits para significar a quantidade de azul na cor de um pixel. Se você já ouviu falar da cor RGB, bem, aí está: vermelho, verde, azul.

Se os valores R, G e B de algum pixel em um BMP são, digamos, `0xff`, `0x00` e `0x00` em hexadecimal, aquele pixel é puramente vermelho, pois `0xff` (também conhecido como `255` em decimal) implica "muito vermelho", enquanto `0x00` e `0x00` implicam "sem verde" e "sem azul", respectivamente. Neste problema, você manipulará esses valores R, G e B de pixels individuais, criando, em última análise, seus próprios filtros de imagem.

Em um arquivo chamado `helpers.c` em uma pasta chamada `filter-less`, escreva um programa para aplicar filtros em BMPs.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-QnLel70SPmbW9nswXTb9Yu9ZD" src="https://asciinema.org/a/QnLel70SPmbW9nswXTb9Yu9ZD.js"></script>

## Código de distribuição

Para este problema, você estenderá a funcionalidade do código fornecido a você pela equipe do CS50.

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd` sozinho. Você deve descobrir que o prompt da janela do seu terminal se assemelha ao seguinte:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/4/filter-less.zip

para baixar um ZIP chamado `filter-less.zip` em seu espaço de código.

Então execute

    unzip filter-less.zip

para criar uma pasta chamada `filter-less`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm filter-less.zip

e responda com “y” seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd filter-less

seguido por Enter para se mover (ou seja, abrir) aquele diretório. Seu prompt agora deve se assemelhar ao seguinte.

    filter-less/ $

Execute `ls` sozinho e você verá alguns arquivos: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` e `Makefile`. Você também verá uma pasta, `images/`, com quatro arquivos BMP. Se você tiver algum problema, siga os mesmos passos novamente e veja se consegue determinar em que errou!

## Histórico

### Um pouco(mapa) mais técnico

Lembre-se de que um arquivo é apenas uma sequência de bits, organizados de alguma forma. Um arquivo BMP de 24 bits, então, é essencialmente apenas uma sequência de bits, (quase) cada 24 dos quais representam a cor de algum pixel. Mas um arquivo BMP também contém alguns "metadados", informações como a altura e a largura de uma imagem. Esses metadados são armazenados no início do arquivo na forma de duas estruturas de dados geralmente chamadas de "cabeçalhos", que não devem ser confundidas com os arquivos de cabeçalho do C. (Aliás, esses cabeçalhos evoluíram ao longo do tempo. Este problema usa a última versão do formato BMP da Microsoft, 4.0, que estreou com o Windows 95.)

O primeiro desses cabeçalhos, chamado `BITMAPFILEHEADER`, tem 14 bytes de comprimento. (Lembre-se de que 1 byte é igual a 8 bits.) O segundo desses cabeçalhos, chamado `BITMAPINFOHEADER`, tem 40 bytes de comprimento. Imediatamente após esses cabeçalhos está o bitmap real: uma matriz de bytes, triplos dos quais representam a cor de um pixel. No entanto, o BMP armazena esses triplos ao contrário (ou seja, como BGR), com 8 bits para azul, seguidos por 8 bits para verde e 8 bits para vermelho. (Alguns BMPs também armazenam o bitmap inteiro ao contrário, com a primeira linha da imagem no final do arquivo BMP. Mas nós armazenamos os BMPs deste conjunto de problemas conforme descrito aqui, com a primeira linha de cada bitmap primeiro e a última linha por último .) Em outras palavras, se convertêssemos o smiley de 1 bit acima para um smiley de 24 bits, substituindo o vermelho pelo preto, um BMP de 24 bits armazenaria este bitmap da seguinte forma, onde `0000ff` significa vermelho e `ffffff` significa branco; destacamos em vermelho todas as instâncias de `0000ff`.

![sorriso vermelho](https://cs50.harvard.edu/x/2024/psets/4/filter/less/red_smile.png)

Como apresentamos esses bits da esquerda para a direita, de cima para baixo, em 8 colunas, você pode realmente ver o smiley vermelho se der um passo para trás.

Para ser claro, lembre-se de que um dígito hexadecimal representa 4 bits. Consequentemente, `ffffff` em hexadecimal na verdade significa `111111111111111111111111` em binário.

Observe que você poderia representar um bitmap como uma matriz bidimensional de pixels: onde a imagem é uma matriz de linhas, cada linha é uma matriz de pixels. De fato, é assim que escolhemos representar imagens de bitmap neste problema.

### Filtragem de Imagem

O que significa filtrar uma imagem? Você pode pensar em filtrar uma imagem como pegar os pixels de alguma imagem original e modificar cada pixel de tal forma que um efeito particular seja aparente na imagem resultante.

## Entendendo

Vamos agora dar uma olhada em alguns dos arquivos fornecidos a você como código de distribuição para entender o que há dentro deles.

### `bmp.h`

Abra `bmp.h` (clicando duas vezes nele no navegador de arquivos) e dê uma olhada.

Você verá as definições dos cabeçalhos que mencionamos (`BITMAPINFOHEADER` e `BITMAPFILEHEADER`). Além disso, esse arquivo define `BYTE`, `DWORD`, `LONG` e `WORD`, tipos de dados normalmente encontrados no mundo da programação do Windows. Observe como eles são apenas apelidos para primitivas com as quais você (espero) já está familiarizado. Parece que `BITMAPFILEHEADER` e `BITMAPINFOHEADER` fazem uso desses tipos.

Talvez o mais importante para você, este arquivo também define uma `struct` chamada `RGBTRIPLE` que, muito simplesmente, "encapsula" três bytes: um azul, um verde e um vermelho (a ordem, lembre-se, na qual esperamos encontrar os triplos RGB realmente no disco).

Por que essas `structs` são úteis? Bem, lembre-se de que um arquivo é apenas uma sequência de bytes (ou, em última análise, bits) no disco. Mas esses bytes são geralmente ordenados de tal forma que os primeiros representam algo, os próximos representam outra coisa e assim por diante. "Formatos de arquivo" existem porque o mundo padronizou o que os bytes significam. Agora, poderíamos simplesmente ler um arquivo do disco para a RAM como um grande array de bytes. E poderíamos apenas lembrar que o byte em `array[i]` representa uma coisa, enquanto o byte em `array[j]` representa outra. Mas por que não dar a alguns desses bytes nomes para que possamos recuperá-los da memória mais facilmente? Isso é precisamente o que as structs em `bmp.h` nos permitem fazer. Em vez de pensar em algum arquivo como uma longa sequência de bytes, podemos pensar nele como uma sequência de `structs`.

### `filter.c`

Agora, vamos abrir `filter.c`. Este arquivo já foi escrito para você, mas há alguns pontos importantes dignos de nota aqui.

Primeiro, observe a definição de `filters` na linha 10. Essa string informa ao programa quais são os argumentos de linha de comando permitidos para o programa: `b`, `g`, `r` e `s`. Cada um deles especifica um filtro diferente que podemos aplicar às nossas imagens: desfoque, tons de cinza, reflexo e sépia.

As próximas linhas abrem um arquivo de imagem, certificam-se de que é realmente um arquivo BMP e lêem todas as informações de pixel em um array 2D chamado `image`.

Role para baixo até a instrução `switch` que começa na linha 101. Observe que, dependendo de qual `filter` escolhemos, uma função diferente é chamada: se o usuário escolher o filtro `b`, o programa chama a função `blur`; se `g`, então `graycale` é chamado; se `r`, então `reflect` é chamado; e se `s`, então `sepia` é chamado. Observe também que cada uma dessas funções recebe como argumentos a altura da imagem, a largura da imagem e a matriz 2D de pixels.

Estas são as funções que você (em breve!) implementará. Como você pode imaginar, o objetivo é que cada uma dessas funções edite a matriz 2D de pixels de forma que o filtro desejado seja aplicado à imagem.

As demais linhas do programa pegam a `image` resultante e as escrevem em um novo arquivo de imagem.

### `helpers.h`

Em seguida, dê uma olhada em `helpers.h`. Este arquivo é bem curto e apenas fornece os protótipos de função para as funções que você viu anteriormente.

Aqui, observe o fato de que cada função recebe um array 2D chamado `image` como argumento, onde `image` é um array de `height` de linhas e cada linha é outro array de `width` de `RGBTRIPLE`s. Então, se `image` representa a imagem inteira, então `image[0]` representa a primeira linha e `image[0][0]` representa o pixel no canto superior esquerdo da imagem.

### `helpers.c`

Agora, abra `helpers.c`. Aqui é onde ficam as implementações das funções declaradas em `helpers.h`. Mas note que, agora, as implementações estão ausentes! Esta parte é sua responsabilidade.

### `Makefile`

Finalmente, vamos ver `Makefile`. Este arquivo especifica o que deve acontecer quando executamos um comando de terminal como `make filter`. Considerando que os programas que você pode ter escrito antes estavam confinados a um único arquivo, `filter` parece usar vários arquivos: `filter.c` e `helpers.c`. Portanto, precisaremos dizer ao `make` como compilar este arquivo.

Tente compilar `filter` por você mesmo indo até seu terminal e executando

    $ make filter

Então, você pode executar o programa executando:

    $ ./filter -g images/jardim.bmp saida.bmp

que pega a imagem em `images/jardim.bmp` e gera uma nova imagem chamada `saida.bmp` após executar os pixels pela função `grayscale` (escala de cinza). No entanto, `grayscale` ainda não faz nada, então a imagem de saída deve parecer igual ao jardim original.

## Especificação

Implemente as funções em `helpers.c` para que um usuário possa aplicar filtros de escala de cinza, sépia, reflexão ou desfoque às suas imagens.

- A função `grayscale` (escala de cinza) deve receber uma imagem e transformá-la em uma versão em preto e branco da mesma imagem.
- A função `sepia` deve receber uma imagem e transformá-la em uma versão sépia da mesma imagem.
- A função `reflect` deve receber uma imagem e refleti-la horizontalmente.
- Finalmente, a função `blur` deve receber uma imagem e transformá-la em uma versão desfocada da mesma imagem.

Você não deve modificar nenhuma das assinaturas de função, nem deve modificar nenhum outro arquivo além de `helpers.c`.

## Dicas

### Implementar `grayscale`

Um filtro comum é o filtro "escala de cinza", onde pegamos uma imagem e queremos convertê-la em preto e branco. Como isso funciona?

- Lembre-se de que se os valores de vermelho, verde e azul forem todos definidos como `0x00` (hexadecimal para `0`), o pixel ficará preto. E se todos os valores forem definidos como `0xff` (hexadecimal para `255`), o pixel ficará branco. Contanto que os valores de vermelho, verde e azul sejam todos iguais, o resultado será vários tons de cinza no espectro preto e branco, com valores mais altos significando tons mais claros (mais próximos ao branco) e valores mais baixos significando tons mais escuros (mais próximos ao preto).
- Então, para converter um pixel em escala de cinza, você só precisa garantir que os valores de vermelho, verde e azul sejam todos o mesmo valor. Mas como você sabe qual valor definir para eles? Bem, provavelmente é razoável esperar que, se os valores originais de vermelho, verde e azul forem todos muito altos, o novo valor também deva ser muito alto. E se os valores originais fossem todos baixos, o novo valor também deveria ser baixo.
- Na verdade, para garantir que cada pixel da nova imagem ainda tenha o mesmo brilho ou escuridão geral da imagem antiga, você pode fazer a **média** dos valores vermelho, verde e azul para determinar em que tom de cinza fazer o novo pixel.

Se você aplicar o algoritmo acima a cada pixel da imagem, o resultado será uma imagem convertida para escala de cinza. Escreva algum pseudocódigo para ajudá-lo a resolver esse problema.

    void grayscale(int altura, int largura, RGBTRIPLE imagem[altura][largura])
    {
        // Loop em todos os pixels

            // Faz a média de vermelho, verde e azul

            // Atualiza os valores dos pixels
    }

Primeiro, como você pode percorrer todos os pixels? Lembre-se de que os pixels da imagem são armazenados na matriz bidimensional `image`. Para iterar sobre uma matriz bidimensional, você precisará de dois loops, um aninhado dentro do outro.

    void grayscale(int altura, int largura, RGBTRIPLE imagem[altura][largura])
    {
        // Loop em todos os pixels
        for (int i = 0; i < altura; i++)
        {
            for (int j = 0; j < largura; j++)
            {
                // Faz a média de vermelho, verde e azul

                // Atualiza os valores dos pixels
            }
        }
    }

Agora, você pode usar `image[i][j]` para acessar qualquer pixel individual da imagem. Mas como obter a média dos elementos vermelho, verde e azul? Lembre-se de que cada elemento de `image` é um `RGBTRIPLE`, que é a `struct` definida em `bmp.h` para representar um pixel. A sintaxe usual para acessar membros de uma `struct` se aplica, em que `image[i][j].rgbtRed` lhe dará acesso ao valor vermelho do `RGBTRIPLE`, `image[i][j].rgbtGreen` lhe dará acesso ao seu valor verde e assim por diante.

Ao calcular a média, lembre-se de que os valores dos componentes `rgbtRed`, `rgbtGreen` e `rgbtBlue` de um pixel são todos inteiros. Portanto, certifique-se de [arredondar](https://manual.cs50.io/3/round) quaisquer números de ponto flutuante para o inteiro mais próximo ao atribuí-los a um valor de pixel! E por que você pode querer dividir a soma desses inteiros por 3,0 e não por 3?

Depois de calcular a média dos valores vermelho, verde e azul do pixel em uma única cor de escala de cinza resultante, vá em frente e atualize os valores vermelho, verde e azul do pixel. A esta altura, você já está familiarizado com a sintaxe de atribuição!

### Implementando `sepia`

A maioria dos programas de edição de imagem suporta um filtro "sépia", que dá às imagens uma sensação antiga ao fazer com que toda a imagem pareça um pouco marrom avermelhada.

- Uma imagem pode ser convertida em sépia pegando cada pixel e calculando novos valores vermelho, verde e azul com base nos valores originais dos três.
- Há uma série de algoritmos para converter uma imagem em sépia, mas para este problema, pediremos que você use o seguinte algoritmo. Para cada pixel, os valores da cor sépia devem ser calculados com base nos valores da cor original conforme abaixo.
```
sepiaRed = .393 _ originalRed + .769 _ originalGreen + .189 _ originalBlue
sepiaGreen = .349 _ originalRed + .686 _ originalGreen + .168 _ originalBlue
sepiaBlue = .272 _ originalRed + .534 _ originalGreen + .131 \* originalBlue
```

- Claro, o resultado de cada uma dessas fórmulas pode não ser um número inteiro, mas cada valor pode ser arredondado para o número inteiro mais próximo. Também é possível que o resultado da fórmula seja um número maior que 255, o valor máximo para um valor de cor de 8 bits. Nesse caso, os valores vermelho, verde e azul devem ser limitados a 255. Como resultado, podemos garantir que os valores vermelho, verde e azul resultantes serão números inteiros entre 0 e 255, inclusive.

Escreva um pseudocódigo para ajudá-lo a resolver este problema e relembre o uso de `for` aninhados para visitar cada pixel.

```
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop sobre todos os pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calcula valores de sépia

            // Atualiza pixel com valores de sépia
        }
    }
}
```

Para calcular os valores `sepia`, revise os marcadores acima. Você tem uma fórmula para calcular os valores de sépia, mas ainda há alguns detalhes a serem considerados. Em particular, você precisará...

- Arredondar o resultado de cada cálculo para o número inteiro mais próximo
- Garantir que o valor resultante não seja maior que 255

Como uma função que retorna o menor de dois inteiros pode ser útil ao implementar `sepia`, particularmente quando você precisa garantir que o valor de uma cor não seja maior que 255? Fique à vontade para escrever uma função auxiliar para fazer exatamente isso!

### Implementando `reflect`

Alguns filtros também podem mover pixels para outros lugares. Inverter uma imagem, por exemplo, é um filtro em que a imagem resultante é o que você obteria se colocasse a imagem original na frente de um espelho.

- Quaisquer pixels no lado esquerdo da imagem devem terminar no lado direito e vice-versa.
- Observe que todos os pixels originais da imagem original ainda estarão presentes na imagem refletida, apenas esses pixels podem ter sido reorganizados para estarem em um lugar diferente na imagem.

Assim, na função `reflect`, você precisará trocar os valores dos pixels em lados opostos de uma linha. Escreva um pseudocódigo para ajudá-lo a começar:

```
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop sobre todos os pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Troca pixels
        }
    }
}
```

Lembre-se de como implementamos a troca de dois valores com uma variável temporária na aula. Não há necessidade de usar uma função separada para troca, a menos que você queira!

E agora é um bom momento para pensar em seus for aninhados. O `for` externo itera sobre cada linha, enquanto o `for` interno itera sobre cada pixel nessa linha. Para refletir uma linha com sucesso, você precisa iterar sobre cada pixel nela?

### Implementar `desfoque`

Há várias formas de criar o efeito de desfocar ou suavizar uma imagem. Para este problema, nós usaremos o "desfoque de caixa", que funciona pegando cada pixel e, para cada valor de cor, dando a ele um novo valor pela média dos valores das cores dos pixels vizinhos.

- Considere a seguinte grade de pixels, onde nós numeramos cada pixel.
  ![uma grade de pixels](grid.png)
- O novo valor de cada pixel seria a média dos valores de todos os pixels que estão dentro de 1 linha e coluna do pixel original (formando uma caixa 3x3). Por exemplo, cada um dos valores de cor para o pixel 6 seria obtido fazendo a média dos valores de cor originais dos pixels 1, 2, 3, 5, 6, 7, 9, 10 e 11 (observe que o próprio pixel 6 está incluso na média). Da mesma forma, os valores de cor para o pixel 11 seriam obtidos fazendo a média dos valores de cor dos pixels 6, 7, 8, 10, 11, 12, 14, 15 e 16.
- Para um pixel ao longo da borda ou canto, como o pixel 15, nós procuraríamos por todos os pixels dentro de 1 linha e coluna: nesse caso, os pixels 10, 11, 12, 14, 15 e 16.

Ao implementar a função `desfoque`, você pode descobrir que desfocar um pixel acaba afetando o desfoque de outro pixel. Pode ser melhor criar uma cópia de `image` declarando uma nova matriz bidimensional com um código como `RGBTRIPLE copy[altura][largura];`. Então, copie `image` para `copy`, pixel por pixel, com loops `for` aninhados, similarmente a isso:

    void blur(int altura, int largura, RGBTRIPLE image[altura][largura])
    {
        // Cria uma cópia de image
        RGBTRIPLE copy[altura][largura];
        for (int i = 0; i < altura; i++)
        {
            for (int j = 0; j < largura; j++)
            {
                copy[i][j] = image[i][j];
            }
        }
    }

Agora, você pode ler as cores dos pixels de `copy` mas escrever (i.e., mudar) as cores dos pixels em `image`!

## Guia

**Observe que há 5 vídeos nessa lista de reprodução.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/K0v9byp9jd0?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T3837jmUt0ep7Tpmnxdv9NVut"></iframe></div>

## Como testar

Tenha certeza de testar seus filtros em todos os arquivos bitmap de exemplo fornecidos!

### Correção

    check50 cs50/problems/2024/x/filter/less

### Estilo

    style50 helpers.c

## Como enviar

    submit50 cs50/problems/2024/x/filter/less

