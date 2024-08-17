# Filtro

![Harvard Yard com detecção de borda](https://cs50.harvard.edu/x/2024/psets/4/filter/more/yard-edges.bmp)

## Problema a resolver

Talvez a maneira mais simples de representar uma imagem seja com uma grade de pixels (ou seja, pontos), cada um dos quais pode ser de uma cor diferente. Portanto, para imagens em preto e branco, precisamos de 1 bit por pixel, já que 0 pode representar preto e 1 pode representar branco, como abaixo.

![um bitmap simples](https://cs50.harvard.edu/x/2024/psets/4/filter/more/bitmap.png)

Nesse sentido, então, uma imagem é apenas um bitmap (ou seja, um mapa de bits). Para imagens mais coloridas, você simplesmente precisa de mais bits por pixel. Um formato de arquivo (como [BMP](https://pt.wikipedia.org/wiki/BMP), [JPEG](https://pt.wikipedia.org/wiki/JPEG) ou [PNG](https://pt.wikipedia.org/wiki/Portable_Network_Graphics)) que suporte "cores de 24 bits" usa 24 bits por pixel. (Na verdade, o BMP suporta cores de 1, 4, 8, 16, 24 e 32 bits.)

Um BMP de 24 bits usa 8 bits para indicar a quantidade de vermelho na cor de um pixel, 8 bits para indicar a quantidade de verde na cor de um pixel e 8 bits para indicar a quantidade de azul na cor de um pixel. Se você já ouviu falar da cor RGB, bem, aí está: vermelho, verde, azul.

Se os valores R, G e B de algum pixel em um BMP forem, digamos, `0xff`, `0x00` e `0x00` em hexadecimal, esse pixel será puramente vermelho, pois `0xff` (também conhecido como `255` em decimal) implica "muito vermelho", enquanto `0x00` e `0x00` implicam "sem verde" e "sem azul", respectivamente. Neste problema, você manipulará esses valores R, G e B de pixels individuais, criando, por fim, seus próprios filtros de imagem.

Em um arquivo chamado `helpers.c` em uma pasta chamada `filter-more`, grave um programa para aplicar filtros a BMPs.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-DC5vtWOatmXC3Ff825YxHE0CZ" src="https://asciinema.org/a/DC5vtWOatmXC3Ff825YxHE0CZ.js"></script>

## Código de distribuição

Para este problema, você estenderá a funcionalidade do código fornecido a você pela equipe da CS50.

Faça login no [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd` sozinho. Você deve descobrir que o prompt da janela do seu terminal se assemelha ao abaixo:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/4/filter-more.zip

para baixar um ZIP chamado `filter-more.zip` no seu codespace.

Em seguida, execute

    unzip filter-more.zip

para criar uma pasta chamada `filter-more`. Você não precisa mais do arquivo ZIP, então pode executar

    rm filter-more.zip

e responder com "y" seguido de Enter no prompt para remover o arquivo ZIP baixado.

Agora digite

    cd filter-more

seguido de Enter para se mover para (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    filter-more/ $

Execute `ls` sozinho, e você deverá ver alguns arquivos: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` e `Makefile`. Você também deve ver uma pasta chamada `images` com quatro arquivos BMP. Se você tiver algum problema, siga estas mesmas etapas novamente e veja se consegue determinar onde errou!

## Contexto

### Um mapa (bitmap) mais técnico

Lembre-se de que um arquivo é apenas uma sequência de bits, dispostos de alguma forma. Um arquivo BMP de 24 bits, então, é essencialmente apenas uma sequência de bits, (quase) cada 24 dos quais representam a cor de algum pixel. Mas um arquivo BMP também contém alguns "metadados", informações como a altura e a largura de uma imagem. Esses metadados são armazenados no início do arquivo na forma de duas estruturas de dados geralmente chamadas de "cabeçalhos", não devem ser confundidas com os arquivos de cabeçalho C. (Aliás, esses cabeçalhos evoluíram ao longo do tempo. Este problema usa a versão mais recente do formato BMP da Microsoft, 4.0, que estreou com o Windows 95.)

O primeiro desses cabeçalhos, chamado `BITMAPFILEHEADER`, tem 14 bytes de comprimento. (Lembre-se de que 1 byte é igual a 8 bits.) O segundo desses cabeçalhos, chamado `BITMAPINFOHEADER`, tem 40 bytes de comprimento. Imediatamente após esses cabeçalhos está o bitmap real: uma matriz de bytes, triplos dos quais representam a cor de um pixel. No entanto, o BMP armazena esses triplos ao contrário (ou seja, como BGR), com 8 bits para azul, seguidos por 8 bits para verde, seguidos por 8 bits para vermelho. (Alguns BMPs também armazenam o bitmap inteiro ao contrário, com a linha superior de uma imagem no final do arquivo BMP. Mas armazenamos os BMPs deste conjunto de problemas conforme descrito aqui, com a primeira linha de cada bitmap primeiro e a última linha por último.) Em outras palavras, se convertêssemos o smiley de 1 bit acima em um smiley de 24 bits, substituindo o vermelho pelo preto, um BMP de 24 bits armazenaria este bitmap da seguinte forma, onde `0000ff` significa vermelho e `ffffff` significa branco; destacamos em vermelho todas as instâncias de `0000ff`.

![sorriso vermelho](https://cs50.harvard.edu/x/2024/psets/4/filter/more/red_smile.png)

Como apresentamos esses bits da esquerda para a direita, de cima para baixo, em 8 colunas, você pode realmente ver o smiley vermelho se der um passo para trás.

Para deixar claro, lembre-se de que um dígito hexadecimal representa 4 bits. Da mesma forma, `ffffff` em hexadecimal na verdade significa `111111111111111111111111` em binário.

Observe que você pode representar um bitmap como uma matriz bidimensional de pixels: onde a imagem é uma matriz de linhas, cada linha é uma matriz de pixels. Na verdade, é assim que optamos por representar imagens de bitmap neste problema.

### Filtro de Imagem

O que significa filtrar uma imagem? Você pode pensar em filtrar uma imagem como pegar os pixels de uma imagem original e modificar cada pixel de tal forma que um efeito particular fique aparente na imagem resultante.

#### Tons de Cinza

Um filtro comum é o filtro de "tons de cinza", no qual pegamos uma imagem e queremos convertê-la para preto e branco. Como isso funciona?

Lembre-se de que se os valores de vermelho, verde e azul forem todos definidos como `0x00` (hexadecimal para `0`), o pixel será preto. E se todos os valores forem definidos como `0xff` (hexadecimal para `255`), o pixel será branco. Desde que os valores de vermelho, verde e azul sejam todos iguais, o resultado será variações de tons de cinza ao longo do espectro preto-branco, com valores mais altos significando tons mais claros (mais próximos do branco) e valores mais baixos significando tons mais escuros (mais próximos do preto).

Portanto, para converter um pixel em tons de cinza, precisamos apenas garantir que os valores de vermelho, verde e azul sejam todos do mesmo valor. Mas como sabemos que valor atribuir a eles? Bem, provavelmente é razoável esperar que, se os valores originais de vermelho, verde e azul forem todos muito altos, o novo valor também deva ser muito alto. E se os valores originais forem todos baixos, o novo valor também deverá ser baixo.

Na verdade, para garantir que cada pixel da nova imagem ainda tenha o mesmo brilho ou escuridão geral da imagem antiga, podemos tirar a média dos valores de vermelho, verde e azul para determinar que tom de cinza deve ser o novo pixel.

Se você aplicar isso a cada pixel da imagem, o resultado será uma imagem convertida para tons de cinza.

#### Reflexo

Alguns filtros também podem mover pixels. Refletir uma imagem, por exemplo, é um filtro em que a imagem resultante é o que você obteria colocando a imagem original na frente de um espelho. Portanto, todos os pixels do lado esquerdo da imagem devem terminar do lado direito e vice-versa.

Observe que todos os pixels originais da imagem original ainda estarão presentes na imagem refletida, apenas esses pixels podem ter sido reorganizados para ficarem em um local diferente na imagem.

#### Desfoque

Há várias maneiras de criar o efeito de desfocagem ou suavização de uma imagem. Para este problema, usaremos o "desfoque de caixa", que funciona pegando cada pixel e, para cada valor de cor, atribuindo a ele um novo valor calculando a média dos valores de cor dos pixels vizinhos.

Considere a seguinte grade de pixels, onde numeramos cada pixel.

![uma grade de pixels](https://cs50.harvard.edu/x/2024/psets/4/filter/more/grid.png)

O novo valor de cada pixel seria a média dos valores de todos os pixels que estão dentro de 1 linha e coluna do pixel original (formando uma caixa 3x3). Por exemplo, cada um dos valores de cor para o pixel 6 seria obtido pela média dos valores de cor originais dos pixels 1, 2, 3, 5, 6, 7, 9, 10 e 11 (observe que o próprio pixel 6 está incluído na média). Da mesma forma, os valores de cor para o pixel 11 seriam obtidos calculando a média dos valores de cor dos pixels 6, 7, 8, 10, 11, 12, 14, 15 e 16.

Para um pixel ao longo da borda ou canto, como o pixel 15, ainda procuraríamos todos os pixels dentro de 1 linha e coluna: neste caso, os pixels 10, 11, 12, 14, 15 e 16.

#### Bordas

Em algoritmos de inteligência artificial para processamento de imagem, muitas vezes é útil detectar bordas em uma imagem: linhas na imagem que criam uma fronteira entre um objeto e outro. Uma maneira de obter esse efeito é aplicando o [operador de Sobel](https://pt.wikipedia.org/wiki/Operador_Sobel) à imagem.

Como o desfoque de imagem, a detecção de bordas também funciona pegando cada pixel e modificando-o com base na grade 3x3 de pixels que envolve esse pixel. Mas em vez de apenas pegar a média dos nove pixels, o operador de Sobel calcula o novo valor de cada pixel pegando uma soma ponderada dos valores dos pixels circundantes. E como as bordas entre objetos podem ocorrer em uma direção vertical e horizontal, você realmente calculará duas somas ponderadas: uma para detectar bordas na direção x e outra para detectar bordas na direção y. Em particular, você usará os dois seguintes "kernels":

![kernels de Sobel](https://cs50.harvard.edu/x/2024/psets/4/filter/more/sobel.png)

Como interpretar esses kernels? Em suma, para cada um dos três valores de cor para cada pixel, calcularemos dois valores `Gx` e `Gy`. Para calcular `Gx` para o valor do canal vermelho de um pixel, por exemplo, pegaremos os valores vermelhos originais para os nove pixels que formam uma caixa 3x3 ao redor do pixel, multiplicaremos cada um deles pelo valor correspondente no kernel `Gx` e tomaremos a soma dos valores resultantes.

Por que esses valores específicos para o kernel? Na direção `Gx`, por exemplo, estamos multiplicando os pixels à direita do pixel de destino por um número positivo e multiplicando os pixels à esquerda do pixel de destino por um número negativo. Quando pegamos a soma, se os pixels à direita forem de uma cor semelhante aos pixels à esquerda, o resultado será próximo a 0 (os números se anulam). Mas se os pixels à direita forem muito diferentes dos pixels à esquerda, o valor resultante será muito positivo ou muito negativo, indicando uma mudança de cor que provavelmente é o resultado de uma fronteira entre objetos. E um argumento semelhante é válido para calcular bordas na direção `y`.

Usando esses kernels, podemos gerar um valor `Gx` e `Gy` para cada um dos canais vermelho, verde e azul de um pixel. Mas cada canal só pode assumir um valor, não dois: então, precisamos de uma maneira de combinar `Gx` e `Gy` em um único valor. O algoritmo do filtro de Sobel combina `Gx` e `Gy` em um valor final calculando a raiz quadrada de `Gx^2 + Gy^2`. E como os valores do canal só podem assumir valores inteiros de 0 a 255, certifique-se de que o valor resultante seja arredondado para o inteiro mais próximo e limitado a 255!

E quanto a lidar com pixels na borda ou no canto da imagem? Existem muitas maneiras de lidar com pixels na borda, mas para os propósitos deste problema, pediremos que você trate a imagem como se houvesse uma borda sólida preta de 1 pixel ao redor da borda da imagem: portanto, tentar acessar um pixel além da borda da imagem deve ser tratado como um pixel preto sólido (valores de 0 para cada um de vermelho, verde e azul). Isso efetivamente ignorará esses pixels de nossos cálculos de `Gx` e `Gy`.

## Especificação

Implemente as funções em `helpers.c` de modo que o usuário possa aplicar filtros de escala de cinza, reflexão, desfoque ou detecção de bordas em suas imagens.

- A função `grayscale` deve receber uma imagem e transformá-la em uma versão em preto e branco da mesma imagem.
- A função `reflect` deve receber uma imagem e refleti-la horizontalmente.
- A função `blur` deve receber uma imagem e gerar uma versão com desfoque de caixa da mesma imagem.
- A função `edges` deve receber uma imagem e destacar as bordas entre os objetos, de acordo com o operador Sobel.

Você não deve modificar nenhuma das assinaturas de função, nem modificar nenhum outro arquivo além de `helpers.c`.

## Entendendo

Agora, vamos dar uma olhada em alguns dos arquivos fornecidos a você como código de distribuição para entender o que há dentro deles.

### `bmp.h`

Abra `bmp.h` (clicando duas vezes nele no explorador de arquivos) e dê uma olhada.

Você verá as definições dos cabeçalhos que mencionamos (`BITMAPINFOHEADER` e `BITMAPFILEHEADER`). Além disso, esse arquivo define `BYTE`, `DWORD`, `LONG` e `WORD`, tipos de dados normalmente encontrados no mundo da programação do Windows. Perceba como eles são apenas aliases para primitivos com os quais você (espero) já está familiarizado. Parece que `BITMAPFILEHEADER` e `BITMAPINFOHEADER` fazem uso desses tipos.

Talvez o mais importante para você, esse arquivo também define um `struct` chamado `RGBTRIPLE` que, muito simplesmente, "encapsula" três bytes: um azul, um verde e um vermelho (a ordem, lembre-se, na qual esperamos encontrar triplos RGB realmente no disco).

Por que esses `struct`s são úteis? Bem, lembre-se de que um arquivo é apenas uma sequência de bytes (ou, em última análise, bits) no disco. Mas esses bytes geralmente são ordenados de tal forma que os primeiros representam algo, os próximos representam outra coisa e assim por diante. "Formatos de arquivo" existem porque o mundo padronizou o que os bytes significam. Agora, podemos simplesmente ler um arquivo do disco para a RAM como um único grande array de bytes. E poderíamos apenas lembrar que o byte em `array[i]` representa uma coisa, enquanto o byte em `array[j]` representa outra. Mas por que não dar alguns nomes a esses bytes para que possamos recuperá-los da memória mais facilmente? É exatamente isso que os `structs` em `bmp.h` nos permitem fazer. Em vez de pensar em algum arquivo como uma longa sequência de bytes, podemos, em vez disso, pensar nele como uma sequência de `structs`.

### `filter.c`

Agora, vamos abrir `filter.c`. Este arquivo já foi escrito para você, mas há alguns pontos importantes a serem observados aqui.

Primeiro, observe a definição de `filters` na linha 10. Essa string informa ao programa quais são os argumentos de linha de comando permitidos para o programa: `b`, `e`, `g` e `r`. Cada um deles especifica um filtro diferente que podemos aplicar às nossas imagens: desfoque, detecção de borda, escala de cinza e reflexão.

As próximas linhas abrem um arquivo de imagem, certificam-se de que é realmente um arquivo BMP e leem todas as informações do pixel em um array 2D chamado `image`.

Role até a instrução `switch` que começa na linha 101. Observe que, dependendo de qual `filter` escolhemos, uma função diferente é chamada: se o usuário escolher o filtro `b`, o programa chama a função `blur`; se `e`, então `edges` é chamado; se `g`, então `grayscale` é chamado; e se `r`, então `reflect` é chamado. Observe também que cada uma dessas funções recebe como argumentos a altura da imagem, a largura da imagem e a matriz 2D de pixels.

Essas são as funções que você (em breve!) implementará. Como você pode imaginar, o objetivo é que cada uma dessas funções edite o array 2D de pixels de forma que o filtro desejado seja aplicado à imagem.

As linhas restantes do programa pegam a `image` resultante e as gravam em um novo arquivo de imagem.

### `helpers.h`

Em seguida, dê uma olhada em `helpers.h`. Este arquivo é bem curto e apenas fornece os protótipos de função para as funções que você viu anteriormente.

Aqui, observe o fato de que cada função recebe um array 2D chamado `image` como argumento, onde `image` é um array de `height` linhas, e cada linha é outro array de `width` `RGBTRIPLE`s. Então, se `image` representa a imagem inteira, então `image[0]` representa a primeira linha e `image[0][0]` representa o pixel no canto superior esquerdo da imagem.

### `helpers.c`

Agora, abra `helpers.c`. É aqui que pertence a implementação das funções declaradas em `helpers.h`. Mas observe que, no momento, as implementações estão faltando! Esta parte é com você.

### `Makefile`

Finalmente, vamos dar uma olhada em `Makefile`. Este arquivo especifica o que deve acontecer quando executamos um comando de terminal como `make filter`. Considerando que os programas que você pode ter escrito antes estavam confinados a apenas um arquivo, `filter` parece usar vários arquivos: `filter.c` e `helpers.c`. Portanto, precisaremos dizer ao `make` como compilar este arquivo.

Tente compilar `filter` por conta própria indo para o seu terminal e executando

```
$ make filter
```

Depois, você pode executar o programa executando:

```
$ ./filter -g images/yard.bmp out.bmp
```

que pega a imagem em `images/yard.bmp` e gera uma nova imagem chamada `out.bmp` após executar os pixels por meio da função `grayscale`. `grayscale` não faz nada ainda, no entanto, então a imagem de saída deve ser igual ao quintal original.

## Dicas

- Os valores dos componentes `rgbtRed`, `rgbtGreen` e `rgbtBlue` de um pixel são todos inteiros, portanto, certifique-se de arredondar quaisquer números de ponto flutuante para o número inteiro mais próximo ao atribuí-los a um valor de pixel!

## Passo a passo

**Observe que há 5 vídeos nesta playlist.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/vsOsctDernw?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382OwvMbZuaMGtD9wZkhnhYj"></iframe></div>

## Como testar

Certifique-se de testar todos os seus filtros nos arquivos de bitmap de amostra fornecidos!

### Correção

```
check50 cs50/problems/2024/x/filter/more
```

### Estilo

```
style50 helpers.c
```

## Como enviar

```
submit50 cs50/problems/2024/x/filter/more
```

