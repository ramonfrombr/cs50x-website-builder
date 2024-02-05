# Estações do Amor

> Quinhentos e vinte e cinco mil, seiscentos minutos  
> Quinhentos e vinte e cinco mil momentos tão queridos  
> Quinhentos e vinte e cinco mil, seiscentos minutos  
> Como medir, medir um ano?
>
> — "[Estações do Amor](https://en.wikipedia.org/wiki/Seasons_of_Love)," [_Rent_](<https://en.wikipedia.org/wiki/Rent_(musical)>)

Assumindo que há 365 dias em um ano, existem \\(365 \\times 24 \\times 60 = 525,600\\) minutos no mesmo ano (porque há 24 horas em um dia e 60 minutos em uma hora). Mas quantos minutos existem em dois ou mais anos? Bem, isso depende de quantos destes são [anos bissextos](https://en.wikipedia.org/wiki/Leap_year) com 366 dias, de acordo com o [calendário Gregoriano](https://en.wikipedia.org/wiki/Gregorian_calendar), pois alguns deles podem ter \\(1 \\times 24 \\times 60 = 1,440\\) minutos adicionais. Na verdade, quantos minutos se passaram desde que você nasceu? Bem, isso também depende de quantos anos bissextos aconteceram desde então! Existe um [algoritmo](https://en.wikipedia.org/wiki/Leap_year#Algorithm) para isso, mas não vamos reinventar a roda. Vamos usar uma biblioteca em vez disso. Felizmente, o Python vem com um módulo `datetime` que possui uma classe chamada `date` que pode ajudar, de acordo com [docs.python.org/3/library/datetime.html#date-objects](https://docs.python.org/3/library/datetime.html#date-objects).

Em um arquivo chamado `seasons.py`, implemente um programa que solicita ao usuário a sua data de nascimento no formato `AAAA-MM-DD` e então imprime quantos anos eles têm em minutos, arredondado para o inteiro mais próximo, usando palavras em inglês ao invés de numeráis, assim como a música de _Rent_, sem nenhum `and` entre as palavras. Como o usuário pode não saber o horário em que nasceu, assuma, para simplicidade, que o usuário nasceu à meia-noite (ou seja, 00:00:00) nessa data. E assuma que a hora atual também é meia-noite. Em outras palavras, mesmo que o usuário execute o programa ao meio-dia, assuma que na verdade são meia-noite, na mesma data. Use `datetime.date.today` para obter a data de hoje, de acordo com [docs.python.org/3/library/datetime.html#datetime.date.today](https://docs.python.org/3/library/datetime.html#datetime.date.today).

Estruture seu programa conforme abaixo, não apenas com uma função `main`, mas também com uma ou mais outras funções:

    from datetime import date


    def main():
        ...


    ...


    if __name__ == "__main__":
        main()

Fique à vontade para importar outras bibliotecas (internas), ou qualquer que esteja especificado nas dicas abaixo. Saia via `sys.exit` se o usuário não inserir uma data no formato `AAAA-MM-DD`. Garanta que seu programa não lançará exceções.

Antes ou depois de implementar `seasons.py`, adicionalmente implemente, em um arquivo chamado `test_seasons.py`, **uma ou mais** funções que testam sua implementação de quaisquer funções além de `main` em `seasons.py` minuciosamente, cujos nomes devem iniciar com `test_` para que você possa executar seus testes com:

    pytest test_seasons.py

Dicas

- Note que a classe `date` possui diversos métodos e "operações suportadas", de acordo com [docs.python.org/3/library/datetime.html#date-objects](https://docs.python.org/3/library/datetime.html#date-objects). Em particular, a classe implementa `__sub__`, de acordo com [docs.python.org/3/library/operator.html#operator.\_\_sub\_\_](https://docs.python.org/3/library/operator.html#operator.__sub__), sobrecarregando `-` de tal forma que subtrair um objeto `date` de outro retorna um objeto `timedelta`, que por sua vez possui vários "atributos de instância" (apenas leitura), de acordo com [docs.python.org/3/library/datetime.html#timedelta-objects](https://docs.python.org/3/library/datetime.html#timedelta-objects).
- Note que o módulo `inflect` possui diversos métodos, de acordo com [pypi.org/project/inflect](https://pypi.org/project/inflect/). Você pode instalá-lo com:

      pip install inflect

## Demonstração

Assuma que esta demonstração foi gravada em 1 de janeiro de 2000.

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela de terminal se parece com o seguinte:

    $

Em seguida, execute

    mkdir seasons

para criar uma pasta chamada `seasons` no seu espaço de códigos.

Então execute

    cd seasons

para mudar para esse diretório. Agora você deverá ver o seu prompt do terminal como `seasons/ $`. Você pode então executar

    code seasons.py

para criar um arquivo chamado `seasons.py` onde você escreverá seu programa. Certifique-se também de executar

    code test_seasons.py

para criar um arquivo chamado `test_seasons.py` onde você escreverá testes para seu programa.

## Como Testar

#### Como Testar `seasons.py`

Veja como testar `seasons.py` manualmente:

- Execute seu programa com `python seasons.py`. Certifique-se de que seu programa solicite sua data de nascimento. Digite uma data do ano passado a partir de hoje, no formato especificado, e pressione Enter. Seu programa deve imprimir `Quinhentos e vinte e cinco mil, seiscentos minutos`.
- Execute seu programa com `python seasons.py`. Digite uma data de dois anos atrás a partir de hoje, no formato especificado, e pressione Enter. Seu programa deve imprimir `Um milhão, cinquenta e um mil, duzentos minutos`.
- Execute seu programa com `python seasons.py`. Digite uma data de sua escolha, mas desta vez use um formato inválido. Pressione Enter e seu programa deve sair usando `sys.exit` sem levantar uma Exceção.

#### Como Testar `test_seasons.py`

Para testar seus testes, execute `pytest test_seasons.py`. Tente usar versões corretas e incorretas de `seasons.py` para determinar quão bem seus testes identificam erros:

- Garanta que você tenha uma versão correta de `seasons.py`. Execute seus testes executando `pytest test_seasons.py`. O `pytest` deve mostrar que todos os seus testes passaram.
- Modifique uma das funções que você implementou em `seasons.py` e importou em `test_seasons.py`. Uma de suas funções pode, por exemplo, falhar em lançar um `ValueError` quando deveria. Execute seus testes executando `pytest test_seasons.py`. O `pytest` deve mostrar que pelo menos um de seus testes falhou.
- Continue modificando o comportamento de `seasons.py`, criando versões incorretas da sua implementação (previsivelmente). Execute seus testes executando `pytest test_seasons.py`. Os testes que você espera que falhem, falham?

Você pode executar o seguinte para verificar seu código usando `check50`, um programa que a CS50 usará para testar seu código quando você enviar. Mas certifique-se de testá-lo também!

    check50 cs50/problems/2022/python/seasons

Smiles verdes significam que seu programa passou em um teste! Carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que `check50` imprime para ver a entrada que o `check50` entregou ao seu programa, qual saída ele esperava e a saída que seu programa realmente deu.

## Como Enviar

No seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/problems/2022/python/seasons
