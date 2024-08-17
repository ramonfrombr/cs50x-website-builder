# Olá, Mundo

## Problema a Resolver

Graças ao Professor [David Malan](https://en.wikipedia.org/wiki/David_J._Malan) (que lecionou CS50 quando Ramon frequentou o curso!), "olá, mundo" foi implementado em centenas de linguagens. Vamos adicionar sua implementação à lista!

Em um arquivo chamado `hello.c`, em uma pasta chamada `mundo`, implemente um programa em C que imprima `olá, mundo\n`, e é isso!

#### Dica

Aqui está o código real que você deve escrever! (Uma dica e tanto, hein?) É melhor digitá-lo você mesmo, em vez de copiar/colar, para que você comece a desenvolver alguma "memória muscular" para escrever código.

    #include <stdio.h>

    int main(void)
    {
        printf("olá, mundo\n");
    }

## Demonstração

Aqui está um exemplo do que deve acontecer quando você compilar e executar o seu programa.

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-C5rag3703OZpKxGJ6dSwHnUEF" src="https://asciinema.org/a/C5rag3703OZpKxGJ6dSwHnUEF.js"></script>

## Como Começar

Abra o [VS Code](https://cs50.dev/).

Comece clicando dentro da janela do terminal, em seguida, execute `cd` por si só. Você deve descobrir que seu "prompt" se assemelha ao abaixo.

    $

Em seguida, execute

    mkdir mundo

para criar uma pasta chamada `mundo` no seu espaço de códigos.

Em seguida, execute

    cd mundo

para alterar os diretórios para essa pasta. Agora você deve ver seu prompt de terminal como `mundo/ $`. Agora você pode executar

    code hello.c

para criar um arquivo chamado `hello.c` no qual você pode escrever seu código.

## Como Testar

Lembre-se de que você pode compilar `hello.c` com:

    make hello

Se você não vir nenhuma mensagem de erro, ele foi compilado com sucesso! Você pode confirmar isso com

    ls

que deve listar não apenas `hello.c` (que é o código-fonte), mas também `hello` (que é o código de máquina).

Se você vir uma mensagem de erro, tente corrigir seu código e tente compilá-lo novamente. Se você não entender a mensagem de erro, tente executar

    help50 make hello

para conselhos.

Assim que seu código for compilado com sucesso, você pode executar seu programa com:

    ./hello

### Correção

Execute o abaixo para avaliar a correção do seu código usando `check50`, um programa de linha de comando que mostrará carinhas felizes sempre que seu código passar nos testes automatizados do CS50 e carinhas tristes sempre que não passar!

    check50 cs50/problems/2024/x/world

### Estilo

Execute o abaixo para avaliar o estilo do seu código usando `style50`, um programa de linha de comando que mostrará adições (em verde) e exclusões (em vermelho) que você deve fazer em seu programa para melhorar seu estilo. Se você tiver problemas para ver essas cores, o `style50` também oferece suporte a outros [modos](https://cs50.readthedocs.io/style50/)!

    style50 hello.c

## Como Enviar

Não precisa enviar este aqui!