# Substituição

## Problema a resolver

Em uma cifra de substituição, nós "criptografamos" (ou seja, ocultamos de forma reversível) uma mensagem, substituindo cada letra por outra letra. Para fazer isso, nós usamos uma _chave_: neste caso, um mapeamento de cada uma das letras do alfabeto à letra à qual ela deve corresponder quando criptografamos. Para "descriptografar" a mensagem, o receptor da mensagem precisará saber a chave, para que ele possa reverter o processo: traduzindo o texto criptografado (chamado geralmente de _texto cifrado_) de volta para a mensagem original (chamada geralmente de _texto claro_).

Uma chave, por exemplo, pode ser a string `NQXPOMAFTRHLZGECYJIUWSKDVB`. Esta chave de 26 caracteres significa que `A` (a primeira letra do alfabeto) deve ser convertida em `N` (o primeiro caractere da chave), `B` (a segunda letra do alfabeto) deve ser convertida em `Q` (o segundo caractere da chave) e assim por diante.

Uma mensagem como `HELLO`, então, seria criptografada como `FOLLE`, substituindo cada uma das letras de acordo com o mapeamento determinado pela chave.

Em um arquivo chamado `substitution.c` em uma pasta chamada `substitution`, crie um programa que permite que você criptografe mensagens usando uma cifra de substituição. No momento em que o usuário executa o programa, ele deve decidir, fornecendo um argumento de linha de comando, qual deve ser a chave na mensagem secreta que ele fornecerá em tempo de execução.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-HWzT4fngSv4KtdNFgfgpdLxZY" src="https://asciinema.org/a/HWzT4fngSv4KtdNFgfgpdLxZY.js"></script>

## Especificação

Projete e implemente um programa, `substitution`, que criptografa mensagens usando uma cifra de substituição.

- Implemente seu programa em um arquivo chamado `substitution.c` em um diretório chamado `substitution`.
- Seu programa deve aceitar um único argumento de linha de comando, a chave a ser usada para a substituição. A chave em si deve ser insensível a maiúsculas e minúsculas, portanto, qualquer caractere na chave ser maiúsculo ou minúsculo não deve afetar o comportamento do seu programa.
- Se o seu programa for executado sem nenhum argumento de linha de comando ou com mais de um argumento de linha de comando, seu programa deve imprimir uma mensagem de erro de sua escolha (com `printf`) e retornar de `main` um valor de `1` (que tende a significar um erro) imediatamente.
- Se a chave for inválida (por não conter 26 caracteres, conter qualquer caractere que não seja um caractere alfabético ou não conter cada letra exatamente uma vez), seu programa deve imprimir uma mensagem de erro de sua escolha (com `printf`) e retornar da função `main` um valor de `1` imediatamente.
- Seu programa deve emitir `texto claro:` (sem uma quebra de linha) e, em seguida, solicitar ao usuário uma `string` de texto claro (usando `get_string`).
- Seu programa deve emitir `texto cifrado:` (sem uma quebra de linha) seguido pelo texto cifrado correspondente ao texto claro, com cada caractere alfabético no texto claro substituído pelo caractere correspondente no texto cifrado; caracteres não alfabéticos devem ser emitidos inalterados.
- Seu programa deve preservar as maiúsculas e minúsculas: letras maiúsculas devem permanecer maiúsculas; letras minúsculas devem permanecer minúsculas.
- Depois de imprimir o texto cifrado, você deve imprimir uma nova linha. Seu programa então deve sair retornando `0` de `main`.

Você pode achar uma ou mais funções declaradas em `ctype.h` úteis, conforme [manual.cs50.io](https://manual.cs50.io/).

## Passo a passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cXAoZAsgxJ4?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Como testar

### Correção

Em seu terminal, execute o comando abaixo para verificar a correção do seu trabalho.

    check50 cs50/problems/2024/x/substitution

#### Como usar `debug50`

Deseja executar `debug50`? Você pode fazer isso da seguinte forma, depois de compilar seu código com sucesso com `make`:

    debug50 ./substitution KEY

em que `KEY` é a chave que você fornece como um argumento de linha de comando para seu programa. Observe que a execução de

    debug50 ./substitution

irá (de preferência!) fazer com que seu programa termine solicitando ao usuário uma chave.

### Estilo

Execute o código abaixo para avaliar o estilo do seu código usando `style50`.

    style50 substitution.c

## Como enviar

Em seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2024/x/substitution