# Validação de Resposta

Ao criar um [Google Form](https://www.google.com/forms/about/) que solicita aos usuários uma resposta curta (ou parágrafo), é possível habilitar a [validação de resposta](https://support.google.com/docs/answer/3378864) e exigir que a entrada do usuário corresponda a uma [expressão regular](https://support.google.com/a/answer/1371415). Por exemplo, você pode exigir que um usuário insira um endereço de e-mail com uma regex como [esta](https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address):

.html pre { white-space: pre-wrap; }

    ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

Ou você pode usar facilmente o suporte integrado do Google para validar um endereço de e-mail, conforme a captura de tela abaixo, assim como você pode usar uma biblioteca em seu próprio código:

![Google Form](form.png)

Em um arquivo chamado `response.py`, usando ou [validator-collection](https://pypi.org/project/validator-collection/) ou [validators](https://github.com/kvesteri/validators) do PyPI, implemente um programa que solicita ao usuário um endereço de e-mail via `input` e então imprime `Válido` ou `Inválido`, respectivamente, se a entrada for um endereço de e-mail sintaticamente válido. Você não pode usar `re`. E não valide se o nome de domínio do endereço de e-mail realmente existe.

Dicas

- Note que você pode instalar o validator-collection com:

      pip install validator-collection

  Clique em **Página Inicial** para encontrar o caminho para a documentação da biblioteca.

- Note que você pode instalar o validators com:

      pip install validators

  Clique em **Página Inicial** para encontrar o caminho para a documentação da biblioteca.

## Demonstração

## Antes de Começar

Faça login no [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd` sozinho. Você deverá ver que o seu prompt na janela do terminal se assemelha ao abaixo:

    $

Depois, execute

    mkdir response

para criar uma pasta chamada `response` no seu espaço de códigos.

Em seguida, execute

    cd response

para mudar para o diretório dessa pasta. Agora você deverá ver o prompt do seu terminal como `response/ $`. Agora, execute

    code response.py

para criar um arquivo chamado `response.py`, onde você escreverá seu programa.

## Como Testar

Aqui está como testar seu código manualmente:

- Execute seu programa com `python response.py`. Certifique-se de que seu programa solicita um e-mail, em seguida, digite `malan@harvard.edu`, seguido de Enter. Seu programa deverá exibir `Válido`.
- Execute seu programa com `python response.py`. Digite seu próprio e-mail, seguido de Enter. Seu programa deverá exibir `Válido`.
- Execute seu programa com `python response.py`. Digite `malan@@@harvard.edu`, seguido de Enter. Seu programa deverá exibir `Inválido`.
- Execute seu programa com `python response.py`. Dê um erro de digitação em seu próprio e-mail, incluindo um `.` extra antes do `.com`, por exemplo. Pressione Enter e seu programa deverá exibir `Inválido`.

Você pode executar o código abaixo para verificar seu código usando `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas certifique-se de testá-lo também!

    check50 cs50/problems/2022/python/response

Os sorrisos verdes significam que seu programa passou em um teste! As carinhas vermelhas indicarão que seu programa gerou algo inesperado. Visite o URL que o `check50` imprime para ver a entrada que `check50` forneceu ao seu programa, a saída esperada e a saída real que seu programa forneceu.

## Como Enviar

No terminal, execute o código abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/response
