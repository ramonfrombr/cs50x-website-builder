# Pequeno Professor

Um dos primeiros brinquedos de David quando criança, engraçado o suficiente, foi o [Pequeno Professor](https://en.wikipedia.org/wiki/Little_Professor), uma "calculadora" que gerava dez diferentes problemas de matemática para David resolver. Por exemplo, se o brinquedo exibisse `4 + 0 =`, David responderia (esperançosamente) com `4`. Se o brinquedo exibisse `4 + 1 =`, David responderia (esperançosamente) com `5`. Se David respondesse incorretamente, o brinquedo exibiria `EEE`. E após três respostas incorretas para o mesmo problema, o brinquedo simplesmente exibiria a resposta correta (por exemplo, `4 + 0 = 4` ou `4 + 1 = 5`).

Em um arquivo chamado `professor.py`, implemente um programa que:

- Solicite ao usuário um nível, \\(n\\). Se o usuário não inserir `1`, `2` ou `3`, o programa deve solicitar novamente.
- Gere aleatoriamente dez (10) problemas de matemática formatados como `X + Y =`, onde cada `X` e `Y` é um número inteiro não negativo com \\(n\\) dígitos. Não é necessário suportar operações além da adição (`+`).
- Solicite ao usuário que resolva cada um desses problemas. Se uma resposta estiver incorreta (ou nem mesmo for um número), o programa deve exibir `EEE` e solicitar ao usuário novamente, permitindo até três tentativas no total para esse problema. Se o usuário ainda não tiver respondido corretamente após três tentativas, o programa deve exibir a resposta correta.
- O programa deve finalmente exibir a pontuação do usuário: o número de respostas corretas em 10.

Estruture seu programa da seguinte forma, em que `get_level` solicita (e, se necessário, reinicia a solicitação) o nível ao usuário e retorna `1`, `2` ou `3`, e `generate_integer` retorna um número inteiro não negativo gerado aleatoriamente com `nível` dígitos ou gera um `ValueError` se `nível` não for `1`, `2` ou `3`:

    import random

    def main():
        ...

    def get_level():
        ...

    def generate_integer(level):
        ...


    if __name__ == "__main__":
        main()

Dicas

- Note que você pode gerar uma exceção como `ValueError` com o código:

      raise ValueError

- Observe que o módulo `random` vem com várias funções, conforme [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` sozinho. Você deve ver que o prompt da janela do terminal se parece com o abaixo:

    $

Em seguida, execute

    mkdir professor

para criar uma pasta chamada `professor` no seu ambiente de códigos.

Depois execute

    cd professor

para mudar para o diretório dessa pasta. Agora seu prompt do terminal deve aparecer como `professor/ $`. Você pode então executar

    code professor.py

para criar um arquivo chamado `professor.py` onde você escreverá seu programa.

## Como Testar

Aqui está como testar manualmente seu código:

- Execute seu programa com `python professor.py`. Digite `-1` e pressione Enter. Seu programa deve pedir para você digitar novamente:

      Nível:

- Execute seu programa com `python professor.py`. Digite `4` e pressione Enter. Seu programa deve pedir para você digitar novamente:

      Nível:

- Execute seu programa com `python professor.py`. Digite `1` e pressione Enter. Seu programa deve começar a apresentar problemas de adição com inteiros positivos de um dígito. Por exemplo:

      6 + 6 =

  Seu programa deve gerar 10 problemas distintos antes de imprimir o número de perguntas respondidas corretamente e sair.

- Execute seu programa com `python professor.py`. Digite `1` e pressione Enter. Responda a primeira pergunta incorretamente. Seu programa deve exibir:

      EEE

  antes de solicitar novamente a mesma pergunta.

- Execute seu programa com `python professor.py`. Digite `1` e pressione Enter. Responda incorretamente à primeira pergunta três vezes. Seu programa deve exibir a resposta correta. Por exemplo:

      6 + 6 = 12

  e então passar para outra pergunta. Responda corretamente às questões restantes. Seu programa deve exibir uma pontuação de `9`.

- Execute seu programa com `python professor.py`. Digite `1` e pressione Enter. Responda corretamente a todas as 10 perguntas. Seu programa deve exibir uma pontuação de `10`.

Você pode executar o código abaixo para verificar o seu código usando `check50`, um programa que a CS50 usará para testar o seu código quando você enviar. Mas lembre-se de testá-lo por si mesmo também!

    check50 cs50/problems/2022/python/professor

Os sorrisos verdes significam que seu programa passou em um teste! As carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` fornece para ver a entrada que o `check50` passou para o seu programa, qual saída era esperada e qual saída seu programa realmente produziu.

## Como Enviar

No seu terminal, execute o código abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/professor
