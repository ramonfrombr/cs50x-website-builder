## # Extensões de Arquivo

Embora o Windows e o macOS às vezes as ocultem, a maioria dos arquivos possui [extensões de arquivo](https://en.wikipedia.org/wiki/Filename_extension), um sufixo que começa com um ponto (`.`) ao final do seu nome. Por exemplo, os nomes de arquivos para [GIFs](https://en.wikipedia.org/wiki/GIF) terminam com `.gif`, e os nomes de arquivos para [JPEGs](https://en.wikipedia.org/wiki/JPEG) terminam com `.jpg` ou `.jpeg`. Quando você clica duas vezes em um arquivo para abri-lo, seu computador usa sua extensão de arquivo para determinar qual programa iniciar.

Navegadores da web, por outro lado, dependem de [tipos de mídia](https://en.wikipedia.org/wiki/Media_type), anteriormente conhecidos como tipos MIME, para determinar como exibir arquivos que estão na web. Quando você faz o download de um arquivo de um servidor web, esse servidor envia um [cabeçalho HTTP](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields), juntamente com o arquivo, indicando o tipo de mídia do arquivo. Por exemplo, o tipo de mídia para um GIF é `image/gif`, e o tipo de mídia para um JPEG é `image/jpeg`. Para determinar o tipo de mídia de um arquivo, um servidor web normalmente analisa a extensão do arquivo, mapeando um para o outro.

Consulte [developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) para obter tipos comuns.

Em um arquivo chamado `extensions.py`, implemente um programa que solicita ao usuário o nome de um arquivo e, em seguida, exibe o tipo de mídia desse arquivo se o nome do arquivo terminar, sem diferenciação de maiúsculas e minúsculas, em qualquer um desses sufixos:

- `.gif`
- `.jpg`
- `.jpeg`
- `.png`
- `.pdf`
- `.txt`
- `.zip`

Se o nome do arquivo terminar com outro sufixo ou não tiver nenhum sufixo, exiba `application/octet-stream` como resultado, que é um valor padrão comum.

Dicas

- Lembre-se de que uma `str` possui diversos métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Demonstração

## Antes de começar

Acesse [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` sozinho. Você deve ver que o prompt da janela do terminal se parece com o seguinte:

    $

Em seguida, execute

    mkdir extensions

para criar uma pasta chamada `extensions` no seu codespace.

Depois, execute

    cd extensions

para mudar para o diretório dessa pasta. Agora você deve ver o prompt do seu terminal como `extensions/ $`. Agora você pode executar

    code extensions.py

para criar um arquivo chamado `extensions.py`, onde você vai escrever o seu programa.

## Como Testar

Aqui está como testar o seu código manualmente:

- Execute o programa com `python extensions.py`. Digite `happy.jpg` e pressione Enter. Seu programa deve gerar a seguinte saída:

      image/jpeg

- Execute o programa com `python extensions.py`. Digite `document.pdf` e pressione Enter. Seu programa deve gerar a seguinte saída:

      application/pdf

Certifique-se de testar cada um dos outros formatos de arquivo, variar a capitalização da entrada e "acidentalmente" adicionar espaços antes e depois da entrada antes de pressionar enter. Seu programa deve se comportar como esperado, sem diferenciar maiúsculas e minúsculas e espaços.

Você pode executar o código abaixo para verificar seu programa usando `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas lembre-se de testar também por conta própria!

    check50 cs50/problems/2022/python/extensions

Sorrisos verdes significam que o seu programa passou em um teste! Carinhas tristes vermelhas indicarão que o seu programa gerou uma saída inesperada. Visite a URL que o `check50` gera para ver a entrada que o `check50` fornecido ao seu programa, a saída esperada e a saída que o seu programa realmente retornou.

## Como Enviar

No seu terminal, execute o seguinte comando para enviar o seu trabalho.

    submit50 cs50/problems/2022/python/extensions
