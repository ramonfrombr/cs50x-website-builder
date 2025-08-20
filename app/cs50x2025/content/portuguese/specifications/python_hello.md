# Olá, novamente

## Problema para resolver

Em um arquivo chamado `hello.py` em uma pasta chamada `sentimental-hello`, implemente um programa que peça o nome do usuário e, em seguida, imprima `olá, fulano`, no qual `fulano` é o nome fornecido pelo usuário, exatamente como você fez no [conjunto de problemas 1](../../1/). Exceto que o programa deve ser escrito em Python desta vez!

### Dicas

- Lembre-se de que você pode obter uma `str` do usuário com `get_string`, que é declarada na biblioteca `cs50`.
- Lembre-se de que você pode imprimir uma `str` com `print`.
- Lembre-se de que você pode criar strings formatadas em Python adicionando `f` a uma string. Por exemplo, `f"{name}"` substituirá (interpolará) o valor da variável `name` onde você escreveu `{name}`.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-gqi2voQFzbKlna6WkQR0G2W93" src="https://asciinema.org/a/gqi2voQFzbKlna6WkQR0G2W93.js"></script>

## Como testar

Embora o `check50` esteja disponível para este problema, é recomendável testar primeiro seu próprio código para cada um dos seguintes.

- Execute o programa como `python hello.py` e aguarde um prompt para a entrada. Digite `David` e pressione enter. Seu programa deve gerar `olá, David`.
- Execute o programa como `python hello.py` e aguarde um prompt para a entrada. Digite `Inno` e pressione enter. Seu programa deve gerar `olá, Inno`.
- Execute o programa como `python hello.py` e aguarde um prompt para a entrada. Digite `Kamryn` e pressione enter. Seu programa deve gerar `olá, Kamryn`.

### Correção

    check50 cs50/problems/2024/x/sentimental/hello

### Estilo

    style50 hello.py

## Como enviar

    submit50 cs50/problems/2024/x/sentimental/hello