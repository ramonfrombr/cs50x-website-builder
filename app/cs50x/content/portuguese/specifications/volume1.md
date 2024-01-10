# Lab 4: Volume (Volume)

<div class="alert" data-alert="warning" role="alert"><p>Você pode colaborar com um ou dois colegas neste laboratório, mas é esperado que todos os alunos do grupo contribuam igualmente para o laboratório.</p></div>

Escreva um programa para modificar o volume de um arquivo de áudio.

    $ ./volume INPUT.wav OUTPUT.wav 2.0
    

Onde `INPUT.wav` é o nome de um arquivo de áudio original e `OUTPUT.wav` é o nome de um arquivo de áudio cujo volume foi escalado pelo fator dado (por exemplo, 2.0).

Arquivos WAV
---------

Os arquivos WAV são um formato de arquivo comum para representar áudio. Os arquivos WAV armazenam o áudio como uma sequência de "amostras": números que representam o valor de algum sinal de áudio em um determinado ponto no tempo. Os arquivos WAV começam com um "header" de 44 bytes que contém informações sobre o próprio arquivo, incluindo o tamanho do arquivo, o número de amostras por segundo e o tamanho de cada amostra. Após o cabeçalho, o arquivo WAV contém uma sequência de amostras, cada uma sendo um inteiro de 2 bytes (16 bits) representando o sinal de áudio em um determinado ponto no tempo.

Escalando cada valor de amostra por um determinado fator tem o efeito de alterar o volume do áudio. Multiplicar cada valor de amostra por 2.0, por exemplo, terá o efeito de duplicar o volume do áudio original. Multiplicar cada amostra por 0.5, por outro lado, terá o efeito de cortar o volume pela metade.

Tipos
-----

Até agora, vimos vários tipos diferentes em C, incluindo `int`, `bool`, `char`, `double`, `float` e `long`. Dentro de um arquivo de cabeçalho chamado `stdint.h`, estão as declarações de outros tipos que nos permitem definir com precisão o tamanho (em bits) e o sinal (positivo ou negativo) de um inteiro. Dois tipos em particular serão úteis neste laboratório.

*   `uint8_t` é um tipo que armazena um inteiro sem sinal de 8 bits (ou seja, não negativo). Podemos tratar cada byte do cabeçalho de um arquivo WAV como um valor `uint8_t`.
*   `int16_t` é um tipo que armazena um inteiro de 16 bits com sinal (ou seja, positivo ou negativo). Podemos tratar cada amostra de áudio em um arquivo WAV como um valor `int16_t`.

Começando
---------------

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do seu terminal e execute `cd` sozinho. Você deve ver que o "prompt" se parece com o seguinte.

    $
    

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2022/fall/labs/4/volume.zip
    

seguido de Enter para baixar um arquivo ZIP chamado `volume.zip` no seu espaço de códigos. Tome cuidado para não ignorar o espaço entre `wget` e a URL seguinte, ou qualquer outro caractere!

Agora execute

    unzip volume.zip
    

para criar uma pasta chamada `volume`. Você não precisa mais do arquivo ZIP, então execute

    rm volume.zip
    

e responda com "y" seguido de Enter na solicitação para remover o arquivo ZIP que você baixou.

Agora digite

    cd volume
    

seguido de Enter para mover-se para (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o seguinte.

    volume/ $
    

Se tudo correu bem, você deve executar

    ls
    

e você deve ver um arquivo `volume.c` ao lado de um arquivo `input.wav`.

Se você tiver algum problema, siga essas mesmas etapas novamente e veja se consegue determinar onde errou!