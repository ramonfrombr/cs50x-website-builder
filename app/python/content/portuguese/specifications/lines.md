# Linhas de Código

Uma maneira de medir a complexidade de um programa é contar o número de [linhas de código](https://en.wikipedia.org/wiki/Source_lines_of_code) (LOC), excluindo linhas em branco e comentários. Por exemplo, um programa como

    # Say hello

    name = input("Qual é o seu nome? ")
    print(f"Olá, {name}")

possui apenas duas linhas de código, não quatro, já que sua primeira linha é um comentário e sua segunda linha está em branco (ou seja, apenas espaços em branco). Isso não é muita coisa, então é provável que o programa não seja tão complexo. Claro, apenas porque um programa (ou até mesmo uma função) tem mais linhas de código do que outro não significa necessariamente que seja mais complexo. Por exemplo, uma função como

    def is_even(n):
        if n % 2 == 0:
            return True
        else:
            return False

não é realmente duas vezes mais complexa do que uma função como

    def is_even(n):
        return n % 2 == 0

mesmo que a primeira tenha (mais do que) o dobro de linhas de código. Na verdade, a primeira pode ser considerada mais simples se for mais fácil de ler! Portanto, as linhas de código devem ser consideradas com um [grão de sal](https://en.wikipedia.org/wiki/Grain_of_salt).

Ainda assim, em um arquivo chamado `lines.py`, implemente um programa que espera exatamente um argumento de linha de comando, o nome (ou caminho) de um arquivo Python, e exibe o número de linhas de código nesse arquivo, excluindo comentários e linhas em branco. Se o usuário não especificar exatamente um argumento de linha de comando, ou se o nome do arquivo especificado não terminar em `.py`, ou se o arquivo especificado não existir, o programa deverá sair usando `sys.exit`.

Assuma que qualquer linha que comece com `#`, opcionalmente antecedida por espaços em branco, é um comentário. (Uma [docstring](https://peps.python.org/pep-0257/) não deve ser considerada um comentário.) Assuma que qualquer linha que contenha apenas espaços em branco é considerada vazia.

Dicas

- Lembre-se de que um `str` possui vários métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), incluindo `lstrip` e `startswith`.
- Note que `open` pode `raise` um `FileNotFoundError`, conforme [docs.python.org/3/library/exceptions.html#FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError).
- Pode ser útil testar seu programa, por exemplo, em alguns [códigos-fonte da Semana 6](https://cdn.cs50.net/python/2022/x/lectures/6/src6/) bem como em programas próprios.

## Demonstração

## Antes de Começar

Faça login no [cs50.dev](https://cs50.dev/), clique na sua janela do terminal e execute `cd` sozinho. Você deve ver que o prompt da janela do terminal se parece com o seguinte:

    $

Em seguida, execute

    mkdir lines

para criar uma pasta chamada `lines` no seu espaço de código.

Depois, execute

    cd lines

para mudar para o diretório dessa pasta. Agora você deve ver o prompt do terminal como `lines/ $`. Agora você pode executar

    code lines.py

para criar um arquivo chamado `lines.py` onde você vai escrever seu programa.

## Como Testar

Veja como testar o seu código manualmente:

- Execute seu programa com `python lines.py`. Seu programa deve sair com `sys.exit` e fornecer uma mensagem de erro:

      Poucos argumentos de linha de comando

- Crie dois programas em Python, `hello.py` e `goodbye.py`. Execute `python lines.py hello.py goodbye.py`. Seu programa deve sair com `sys.exit` e fornecer uma mensagem de erro:

      Muitos argumentos de linha de comando

- Crie um arquivo de texto chamado `invalid_extension.txt`. Execute seu programa com `python lines.py invalid_extension.txt`. Seu programa deve sair com `sys.exit` e fornecer uma mensagem de erro:

      Não é um arquivo Python

- Execute seu programa com `python lines.py non_existent_file.py`. Assumindo que `non_existent_file.py` não exista, seu programa deve sair com `sys.exit` e fornecer uma mensagem de erro:

      Arquivo não existe

- Crie programas adicionais em Python que variam em complexidade: crie alguns com comentários, alguns com docstrings e alguns com espaços em branco. Para cada um desses arquivos, execute `python lines.py NOME_ARQUIVO`, onde `NOME_ARQUIVO` é o nome do arquivo. `lines.py` deve exibir o número de linhas, excluindo comentários e espaços em branco, presentes no arquivo fornecido.

Você pode executar o comando a seguir para verificar seu código usando `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas lembre-se de testá-lo por conta própria também!

    check50 cs50/problems/2022/python/lines

Os sorrisos verdes significam que seu programa passou em um teste! Carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que `check50` exibe para ver a entrada que o `check50` passou para o seu programa, qual saída ele esperava e qual saída seu programa forneceu de fato.

## Como Enviar

No seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/lines
