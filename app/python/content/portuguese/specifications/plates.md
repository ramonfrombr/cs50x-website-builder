# Placas Personalizadas

![Placa de licença CS50](plate.png)

Em Massachusetts, lar da Universidade Harvard, é possível [solicitar uma placa de licença personalizada](https://www.mass.gov/how-to/request-a-vanity-license-plate) para o seu carro, com sua escolha de letras e números em vez de aleatórios. Entre os requisitos, estão:

- "Todas as placas personalizadas devem começar com pelo menos duas letras."
- "... as placas personalizadas podem conter no máximo 6 caracteres (letras ou números) e no mínimo 2 caracteres."
- "Números não podem ser usados no meio de uma placa; eles devem vir no fim. Por exemplo, AAA222 seria uma placa de licença personalizada aceitável...; AAA22A não seria aceitável. O primeiro número usado não pode ser um '0'."
- "Não são permitidos pontos, espaços ou sinais de pontuação."

No arquivo `plates.py`, implemente um programa que solicita ao usuário uma placa personalizada e então exiba `Valid` se atender a todos os requisitos ou `Invalid` se não atender. Assuma que quaisquer letras na entrada do usuário serão maiúsculas. Estruture seu programa conforme abaixo, onde `is_valid` retorna `True` se `s` atende a todos os requisitos e `False` se não. Assuma que `s` será uma `str`. Você pode implementar funções adicionais para `is_valid` chamar (por exemplo, uma função por requisito).

    def main():
        plate = input("Placa: ")
        if is_valid(plate):
            print("Valid")
        else:
            print("Invalid")


    def is_valid(s):
        ...


    main()

Dicas

- Lembre-se de que uma `str` possui diversos métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Assim como uma `list`, uma `str` é uma "sequência" (de caracteres), o que significa que pode ser "fatiada" em strings mais curtas com uma sintaxe como `s[i:j]`. Por exemplo, se `s` for `"CS50"`, então `s[0:2]` será `"CS"`.

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique em sua janela do terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela do terminal se parece com o abaixo:

    $

Em seguida, execute

    mkdir plates

para criar uma pasta chamada `plates` em seu espaço de códigos.

Depois execute

    cd plates

para mudar para esse diretório. Agora seu prompt do terminal deverá estar como `plates/ $`. Você pode agora executar

    code plates.py

para criar um arquivo chamado `plates.py`, onde você escreverá seu programa.

## Como Testar

Veja como testar seu código manualmente:

- Execute seu programa com `python plates.py`. Digite `CS50` e pressione Enter. Seu programa deve exibir:

      Válido

- Execute seu programa com `python plates.py`. Digite `CS05` e pressione Enter. Seu programa deve exibir:

      Inválido

- Execute seu programa com `python plates.py`. Digite `CS50P` e pressione Enter. Seu programa deve exibir:

      Inválido

- Execute seu programa com `python plates.py`. Digite `PI3.14` e pressione Enter. Seu programa deve exibir:

      Inválido

- Execute seu programa com `python plates.py`. Digite `H` e pressione Enter. Seu programa deve exibir:

      Inválido

- Execute seu programa com `python plates.py`. Digite `OUTATIME` e pressione Enter. Seu programa deve exibir:

      Inválido

Você pode executar o comando abaixo para verificar seu código usando `check50`, um programa que o CS50 usará para testar seu código ao enviar. Mas lembre-se de testar por conta própria também!

    check50 cs50/problems/2022/python/plates

Emojis verdes significam que seu programa passou em um teste! Emojis vermelhos indicam que seu programa produziu algo inesperado. Visite a URL que `check50` exibe para ver a entrada que `check50` forneceu ao seu programa, a saída esperada e a saída real do seu programa.

## Como Enviar

Em seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/plates
