Detalhes da Implementação
-------------------------

Complete a implementação de `volume.c`, de modo que ele mude o volume de um arquivo de áudio por um fator dado.

*   O programa aceita três argumentos da linha de comando: `input` representa o nome do arquivo de áudio original, `output` representa o nome do novo arquivo de áudio que deve ser gerado e `factor` é a quantidade pela qual o volume do arquivo de áudio original deve ser escalado.
    *   Por exemplo, se `factor` for `2.0`, então seu programa deve dobrar o volume do arquivo de áudio em `input` e salvar o novo arquivo de áudio gerado em `output`.
*   Seu programa deve primeiro ler o cabeçalho do arquivo de entrada e escrever o cabeçalho no arquivo de saída. Lembre-se de que esse cabeçalho sempre tem exatamente 44 bytes.
    *   Observe que `volume.c` já define uma variável para você chamada `HEADER_SIZE`, igual ao número de bytes no cabeçalho.
*   Seu programa deve então ler o restante dos dados do arquivo WAV, um amostra de 16 bits (2 bytes) de cada vez. Seu programa deve multiplicar cada amostra pelo `factor` e escrever a nova amostra no arquivo de saída.
    *   Você pode assumir que o arquivo WAV usará valores de 16 bits assinados como amostras. Na prática, arquivos WAV podem ter números variáveis de bits por amostra, mas vamos assumir amostras de 16 bits para este laboratório.
*   Seu programa, se usar `malloc`, não deve vazar memória.

### Passo a passo

<div class="alert" data-alert="primary" role="alert"><p>Este vídeo foi gravado quando o curso ainda usava o CS50 IDE para escrever código. Embora a interface possa parecer diferente do seu Codespace, o comportamento dos dois ambientes deve ser muito similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/LiGhjz9ColQ"></iframe>


### Dicas

*   Provavelmente você desejará criar um array de bytes para armazenar os dados do cabeçalho do arquivo WAV que você lerá do arquivo de entrada. Usando o tipo `uint8_t` para representar um byte, você pode criar um array de `n` bytes para o cabeçalho com a sintaxe

<pre>
uint8_t header[n];
</pre>    

substituindo `n` pelo número de bytes. Em seguida, você pode usar `header` como argumento para `fread` ou `fwrite` para ler do cabeçalho ou escrever nele.

*   Provavelmente você desejará criar um "buffer" para armazenar as amostras de áudio que você lerá do arquivo WAV. Usando o tipo `int16_t` para armazenar uma amostra de áudio, você pode criar uma variável do tipo buffer com a sintaxe

<pre>
int16_t buffer;
</pre>   

Você pode então usar `&buffer` como argumento para `fread` ou `fwrite` para ler do buffer ou escrever nele. (Lembre-se de que o operador `&` é usado para obter o endereço da variável.)

*   Você pode achar a documentação de [`fread`](https://man.cs50.io/3/fread) e [`fwrite`](https://man.cs50.io/3/fwrite) útil aqui.
    *   Em particular, observe que ambas as funções aceitam os seguintes argumentos:
        *   `ptr`: um ponteiro para o local na memória onde armazenar dados (ao ler de um arquivo) ou de onde escrever dados (ao escrever dados em um arquivo)
        *   `size`: o número de bytes em um item de dados
        *   `nmemb`: o número de itens de dados (cada um com `size` bytes) a serem lidos ou escritos
        *   `stream`: o ponteiro de arquivo a ser lido ou gravado
    *   De acordo com a documentação, `fread` retornará o número de itens de dados lidos com sucesso. Você pode achar isso útil para verificar quando chegou ao final do arquivo!


<details><summary>Não tem certeza de como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/-rtZkTAK2gg"></iframe></details>


### Como testar seu código

Seu programa deve se comportar conforme os exemplos abaixo.

    $ ./volume input.wav output.wav 2.0
    

Quando você ouvir `output.wav` (ao clicar com o botão direito no `output.wav` no navegador de arquivos, escolher **Download** e, em seguida, abrir o arquivo em um reprodutor de áudio em seu computador), ele deve ser duas vezes mais alto do que `input.wav`!

    $ ./volume input.wav output.wav 0.5
    

Quando você ouvir `output.wav`, ele deve ser a metade do volume de `input.wav`!

Execute o comando abaixo para verificar a correção do seu código usando `check50`. Mas certifique-se de compilar e testar você mesmo também!

    check50 cs50/labs/2023/x/volume
    

Execute o comando abaixo para verificar o estilo do seu código usando `style50`.

    style50 volume.c
    

Como enviar seu trabalho
------------------------

No terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/labs/2023/x/volume