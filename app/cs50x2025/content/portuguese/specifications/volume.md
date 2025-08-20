## Volume

![Forma de onda do arquivo WAV](https://cs50.harvard.edu/x/2024/psets/4/volume/wav_file.png)

## Problema a resolver

[Arquivos WAV](https://docs.fileformat.com/audio/wav/) são um formato de arquivo comum para representar áudio. Os arquivos WAV armazenam o áudio como uma sequência de "amostras": números que representam o valor de algum sinal de áudio em um ponto específico no tempo. Os arquivos WAV começam com um "cabeçalho" de 44 bytes que contém informações sobre o arquivo em si, incluindo o tamanho do arquivo, o número de amostras por segundo e o tamanho de cada amostra. Após o cabeçalho, o arquivo WAV contém uma sequência de amostras, cada uma delas um único inteiro de 2 bytes (16 bits) representando o sinal de áudio em um ponto específico no tempo.

Escalar cada valor de amostra por um determinado fator tem o efeito de alterar o volume do áudio. Multiplicar cada valor de amostra por 2.0, por exemplo, terá o efeito de dobrar o volume do áudio de origem. Multiplicar cada amostra por 0,5, por sua vez, terá o efeito de reduzir o volume pela metade.

Em um arquivo chamado `volume.c` em uma pasta chamada `volume`, escreva um programa para modificar o volume de um arquivo de áudio.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-mc2hPhYDt1spoMjlqNMuqC4Uc" src="https://asciinema.org/a/mc2hPhYDt1spoMjlqNMuqC4Uc.js"></script>

## Código de distribuição

Para este problema, você estenderá a funcionalidade do código fornecido a você pela equipe do CS50.

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` sozinho. Você deve descobrir que o prompt da janela do seu terminal se parece com o abaixo:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/4/volume.zip

para baixar um ZIP chamado `volume.zip` no seu codespace.

Em seguida, execute

    unzip volume.zip

para criar uma pasta chamada `volume`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm volume.zip

e responda com "y" seguido por Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd volume

seguido por Enter para mover-se para (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    volume/ $

Se tudo foi bem-sucedido, você deve executar

    ls

e ver um arquivo chamado `volume.c`. Executar o `código volume.c` deve abrir o arquivo onde você digitará seu código para este conjunto de problemas. Se não, refaça seus passos e veja se consegue determinar onde você errou!

## Detalhes da implementação

Conclua a implementação de `volume.c` para que ele altere o volume de um arquivo de som por um determinado fator.

- O programa deve aceitar três argumentos de linha de comando. O primeiro é `input`, que representa o nome do arquivo de áudio original. O segundo é `output`, que representa o nome do novo arquivo de áudio que deve ser gerado. O terceiro é `factor`, que é a quantidade pela qual o volume do arquivo de áudio original deve ser escalado.
  - Por exemplo, se `factor` for `2.0`, seu programa deve dobrar o volume do arquivo de áudio em `input` e salvar o arquivo de áudio recém-gerado em `output`.
- Seu programa deve primeiro ler o cabeçalho do arquivo de entrada e gravar o cabeçalho no arquivo de saída.
- Seu programa deve então ler o restante dos dados do arquivo WAV, uma amostra de 16 bits (2 bytes) por vez. Seu programa deve multiplicar cada amostra pelo `factor` e gravar a nova amostra no arquivo de saída.
  - Você pode assumir que o arquivo WAV usará valores assinados de 16 bits como amostras. Na prática, os arquivos WAV podem ter vários números de bits por amostra, mas assumiremos amostras de 16 bits para este problema.
- Seu programa, se usar `malloc`, não deve vazar nenhuma memória.

## Dicas

### Entenda o código em `volume.c`

Observe primeiro que `volume.c` já está configurado para receber três argumentos de linha de comando, `input`, `output` e `factor`.

- `main` usa um `int`, `argc`, e uma matriz de `char *`s (strings!), `argv`.
- Se `argc`, o número de argumentos na linha de comando incluindo o próprio programa, não for igual a 4, o programa imprimirá seu uso adequado e sairá com o código de status 1.

        int main(int argc, char \*argv[])
        {
            // Verifique os argumentos da linha de comando
            if (argc != 4)
            {
                printf("Uso: ./volume input.wav output.wav factor\n");
                return 1;
            }

            // ...
        }

O `volume.c` seguinte usa o [`fopen`](https://manual.cs50.io/3/fopen) para abrir os dois arquivos fornecidos como argumentos de linha de comando.

- É uma boa prática verificar se o resultado de chamar `fopen` é `NULL`. Se for, o arquivo não foi encontrado ou não pôde ser aberto.

        // Abra arquivos e determine o fator de escala
        FILE *input = fopen(argv[1], "r");
        if (input == NULL)
        {
            printf("Não foi possível abrir o arquivo.\n");
            return 1;
        }

        FILE *output = fopen(argv[2], "w");
        if (output == NULL)
        {
            printf("Não foi possível abrir o arquivo.\n");
            return 1;
        }

Mais tarde, esses arquivos são fechados com `fclose`. Sempre que você chamar `fopen`, chame `fclose` posteriormente!

        // Feche os arquivos
        fclose(input);
        fclose(output);

Antes de fechar os arquivos, perceba que temos alguns TODOs.

        // TODO: Copie o cabeçalho do arquivo de entrada para o arquivo de saída

        // TODO: Leia as amostras do arquivo de entrada e grave os dados atualizados no arquivo de saída

Provavelmente você precisará saber o fator pelo qual escalar o volume, por isso `volume.c` já converte o terceiro argumento da linha de comando em um `float` para você!

        float factor = atof(argv[3]);

### Copiar o cabeçalho WAV do arquivo de entrada para o arquivo de saída

Sua primeira tarefa é copiar o cabeçalho do arquivo WAV de `entrada` e gravá-lo em `saída`. Antes disso, porém, você precisará aprender alguns tipos de dados especiais.

Até agora, vimos vários tipos diferentes em C, incluindo `int`, `bool`, `char`, `double`, `float` e `long`. No entanto, dentro de um cabeçalho chamado `stdint.h` há declarações de vários tipos _outros_ que nos permitem definir com muita precisão o tamanho (em bits) e o sinal (com ou sem sinal) de um inteiro. Dois tipos em particular serão úteis quando trabalharmos com arquivos WAV:

- `uint8_t` é um tipo que armazena um inteiro de 8 bits (portanto, `8`!) sem sinal (ou seja, não negativo) (portanto `uint`!). Podemos tratar cada byte do cabeçalho de um arquivo WAV como um valor `uint8_t`.
- `int16_t` é um tipo que armazena um inteiro de 16 bits com sinal (ou seja, positivo ou negativo). Podemos tratar cada amostra de áudio em um arquivo WAV como um valor `int16_t`.

Você provavelmente vai querer criar uma matriz de bytes para armazenar os dados do cabeçalho do arquivo WAV que você lerá do arquivo de entrada. Usando o tipo `uint8_t` para representar um byte, você pode criar uma matriz de `n` bytes para seu cabeçalho com sintaxe como

    uint8_t header[n];

substituindo `n` pelo número de bytes. Você pode então usar `header` como um argumento para [`fread`](https://manual.cs50.io/3/fread) ou [`fwrite`](https://manual.cs50.io/3/fwrite) para ler ou gravar no cabeçalho.

Lembre-se de que o cabeçalho de um arquivo WAV sempre tem exatamente 44 bytes de comprimento. Observe que `volume.c` já define uma variável para você chamada `HEADER_SIZE`, igual ao número de bytes no cabeçalho.

O que está abaixo é uma dica e tanto, mas aqui está como você pode realizar essa tarefa!

    // Copiar cabeçalho do arquivo de entrada para o arquivo de saída
    uint8_t header[HEADER_SIZE];
    fread(header, HEADER_SIZE, 1, input);
    fwrite(header, HEADER_SIZE, 1, output);

### Gravar dados atualizados no arquivo de saída

Sua próxima tarefa é ler amostras de `entrada`, atualizar essas amostras e gravar as amostras atualizadas em `saída`. Ao ler arquivos, é comum criar um "buffer" no qual os dados são temporariamente armazenados. Lá, você pode modificar os dados e, quando estiverem prontos, gravar os dados do buffer em um novo arquivo.

Lembre-se de que podemos usar o tipo `int16_t` para representar uma amostra de um arquivo WAV. Para armazenar uma amostra de áudio, então, você pode criar uma variável de buffer com sintaxe como:

    // Criar um buffer para uma única amostra
    int16_t buffer;

Com um buffer para amostras no lugar, agora você pode ler dados nele, uma amostra por vez. Tente usar `fread` para esta tarefa! Você pode usar `&buffer`, o endereço de `buffer`, como um argumento para `fread` ou `fwrite` para ler ou gravar no buffer. (Lembre-se que o operador `&` é usado para obter o endereço da variável.)

    // Criar um buffer para uma única amostra
    int16_t buffer;

    // Ler amostra única no buffer
    fread(&buffer, sizeof(int16_t), 1, input)

Agora, para aumentar (ou diminuir) o volume de uma amostra, você só precisa multiplicá-la por algum fator.

    // Criar um buffer para uma única amostra
    int16_t buffer;

    // Ler amostra única no buffer
    fread(&buffer, sizeof(int16_t), 1, input)

    // Atualizar volume da amostra
    buffer *= factor;

E, finalmente, você pode gravar essa amostra atualizada em `saída`:

    // Criar um buffer para uma única amostra
    int16_t buffer;

    // Ler amostra única da entrada para o buffer
    fread(&buffer, sizeof(int16_t), 1, input)

    // Atualizar volume da amostra
    buffer *= factor;

    // Gravar amostra atualizada no novo arquivo
    fwrite(&buffer, sizeof(int16_t), 1, output);

Há apenas um problema: você precisará _continuar_ lendo uma amostra em seu buffer, atualizando seu volume e gravando a amostra atualizada no arquivo de saída enquanto ainda houver amostras para ler.

- Felizmente, de acordo com sua documentação, `fread` retornará o número de itens de dados lidos com sucesso. Você pode achar útil verificar quando você chegou ao final do arquivo!
- Tenha em mente que não há razão para que você não possa chamar `fread` dentro da condicional de um loop `while`. Você poderia, por exemplo, fazer uma chamada para `fread` como a seguinte:

        while (fread(...))
        {

        }

É uma grande dica, mas veja abaixo uma maneira eficiente de resolver esse problema:

    // Criar um buffer para uma única amostra
    int16_t buffer;

    // Ler amostra única da entrada para o buffer enquanto houver amostras para ler
    while (fread(&buffer, sizeof(int16_t), 1, input) != 0)
    {
        // Atualizar volume da amostra
        buffer *= factor;

        // Gravar amostra atualizada no novo arquivo
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

Como a versão de C que você está usando trata valores diferentes de zero como `true` e valores zero como `false`, você pode simplificar a sintaxe acima para o seguinte:

    // Criar um buffer para uma única amostra
    int16_t buffer;

    // Ler amostra única da entrada para o buffer enquanto houver amostras para ler
    while (fread(&buffer, sizeof(int16_t), 1, input))
    {
        // Atualizar volume da amostra
        buffer *= factor;

        // Gravar amostra atualizada no novo arquivo
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

## Passo a passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/LiGhjz9ColQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

<details><summary>Não tem certeza como resolver?</summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-rtZkTAK2gg?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

## Como testar

O seu programa deve comportar-se de acordo com os exemplos abaixo.

    $ ./volume input.wav output.wav 2.0

Quando ouvir `output.wav` (por exemplo, clicando com controle em `output.wav` no navegador de arquivos, escolhendo **Baixar**, e depois abrindo o arquivo em um player de áudio em seu computador), ele deve estar duas vezes mais alto que `input.wav`!

    $ ./volume input.wav output.wav 0.5

Quando ouvir `output.wav`, ele deve estar na metade da altura de `input.wav`!

### Precisão

    check50 cs50/problems/2024/x/volume

### Estilo

    style50 volume.c

## Como enviar

    submit50 cs50/problems/2024/x/volume

