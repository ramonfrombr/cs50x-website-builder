Uso
---

Aqui estão alguns exemplos de como o programa deveria funcionar. Por exemplo, se o usuário omitir um dos argumentos da linha de comando:

    $ ./reverse input.wav
    Uso: ./reverse input.wav output.wav
    

Ou se o usuário omitir ambos os argumentos da linha de comando:

    $ ./reverse
    Uso: ./reverse input.wav output.wav
    

Aqui está como o programa deveria funcionar se o usuário fornecer um arquivo de entrada que não seja um arquivo WAV real:

    $ ./reverse image.jpg output.wav
    Entrada não é um arquivo WAV.
    

Você pode assumir que o usuário insere um nome de arquivo de saída válido, como `output.wav`.

Um programa executado com sucesso não deve mostrar nenhum texto e deve criar um arquivo WAV com o nome especificado pelo usuário, reproduzindo o áudio do arquivo de entrada WAV de forma reversa. Por exemplo:

    $ ./reverse input.wav output.wav
    

Testando
--------

Execute o seguinte para avaliar a correção do seu código usando o `check50`. Mas certifique-se de compilar e testá-lo também!

    check50 cs50/problems/2023/x/reverse
    

Execute o seguinte para avaliar o estilo do seu código usando `style50`.

    style50 reverse.c
    

Como Enviar
-----------

No seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2023/x/reverse