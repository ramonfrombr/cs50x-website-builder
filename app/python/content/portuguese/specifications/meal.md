# Hora das Refeições

Suponha que você esteja em um país onde é costume comer o café da manhã entre 7:00 e 8:00, o almoço entre 12:00 e 13:00 e o jantar entre 18:00 e 19:00. Não seria legal se você tivesse um programa que pudesse dizer a você o que comer quando?

No arquivo `meal.py`, implemente um programa que solicita ao usuário um horário e informa se é `hora do café da manhã`, `hora do almoço` ou `hora do jantar`. Se não for hora de uma refeição, não exiba nada. Assuma que a entrada do usuário será formatada em horário de 24 horas como `#:##` ou `##:##`. E assuma que o intervalo de tempo de cada refeição é inclusivo. Por exemplo, seja 7:00, 7:01, 7:59 ou 8:00, ou a qualquer momento no intervalo, é hora do café da manhã.

Estruture seu programa conforme abaixo, em que `convert` é uma função (que pode ser chamada por `main`) que converte `time`, uma `str` em formato de 24 horas, para o número correspondente de horas como um `float`. Por exemplo, dado um `time` como `"7:30"` (ou seja, 7 horas e 30 minutos), `convert` deve retornar `7.5` (ou seja, 7,5 horas).

    def main():
        ...


    def convert(time):
        ...


    if __name__ == "__main__":
        main()

Dicas

- Lembre-se de que uma `str` vem com vários métodos, conforme [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), incluindo `split`, que separa uma `str` em uma sequência de valores, todos os quais podem ser atribuídos a variáveis de uma vez. Por exemplo, se `time` é uma `str` como `"7:30"`, então

      horas, minutos = time.split(":")

  atribuirá `"7"` para `horas` e `"30"` para `minutos`.

- Tenha em mente que existem 60 minutos em 1 hora.

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela do terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela do terminal se assemelha ao seguinte:

    $

Em seguida, execute

    mkdir meal

para criar uma pasta chamada `meal` no seu espaço de códigos.

Depois, execute

    cd meal

para mudar de diretório para essa pasta. Agora você deverá ver o prompt do terminal como `meal/ $`. Agora você pode executar

    code meal.py

para criar um arquivo chamado `meal.py` onde você escreverá seu programa.

## Desafio

Se estiver disposto a um desafio, adicione opcionalmente suporte para horas de 12 horas, permitindo que o usuário insira horas nesses formatos também:

- `#:## a.m.` e `##:## a.m.`
- `#:## p.m.` e `##:## p.m.`

## Como Testar

Veja como testar seu código manualmente:

- Execute seu programa com `python meal.py`. Digite `7:00` e pressione Enter. Seu programa deverá exibir:

      hora do café da manhã

- Execute seu programa com `python meal.py`. Digite `7:30` e pressione Enter. Seu programa deverá exibir:

      hora do café da manhã

- Execute seu programa com `python meal.py`. Digite `12:42` e pressione Enter. Seu programa deverá exibir

      hora do almoço

- Execute seu programa com `python meal.py`. Digite `18:32` e pressione Enter. Seu programa deverá exibir

      hora do jantar

- Execute seu programa com `python meal.py`. Digite `11:11` e pressione Enter. Seu programa não deverá exibir nada.

Você pode executar o abaixo para verificar seu código usando o `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas certifique-se de testá-lo por conta própria também!

    check50 cs50/problems/2022/python/meal

Os smiles verdes significam que seu programa passou em um teste! Os smiles vermelhos indicarão que seu programa gerou algo inesperado. Visite a URL que o `check50` gera para ver a entrada que o `check50` passou para o seu programa, qual saída ele esperava e qual saída seu programa realmente deu.

Se você estiver falhando nos testes, mas tiver certeza de que seu programa se comporta corretamente, verifique se você não removeu a linha

    if __name__ == "__main__":
        main()

da estrutura do código que foi fornecida. Isso permite que o `check50` teste sua função de conversão separadamente. Você aprenderá mais sobre isso nas próximas semanas.

## Como Enviar

No seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/meal
