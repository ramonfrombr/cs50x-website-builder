# NÚMEROS

Na Temporada 5, Episódio 23 de [NÚMEROS](<https://en.wikipedia.org/wiki/Numbers_(TV_series)>), um suposto [endereço IP](https://en.wikipedia.org/wiki/IP_address) aparece na tela, `275.3.6.28`, que na verdade não é um endereço válido de [IPv4](https://en.wikipedia.org/wiki/IPv4) (ou [IPv6](https://en.wikipedia.org/wiki/IPv6)).

Um endereço IPv4 é um identificador numérico que um dispositivo (ou, na TV, hacker) usa para se comunicar na internet, semelhante a um endereço postal no mundo real, normalmente formatado na notação [ponto-decimal](https://en.wikipedia.org/wiki/Dot-decimal_notation) como `#.#.#.#`. Mas cada `#` deve ser um número entre `0` e `255`, inclusive. Diga-se que `275` não está nesse intervalo! Se ao menos NÚMEROS tivesse validado o endereço nessa cena!

Em um arquivo chamado `numb3rs.py`, implemente uma função chamada `validate` que espera um endereço IPv4 como entrada em formato de `str` e então retorna `True` ou `False`, respectivamente, se essa entrada é um endereço IPv4 válido ou não.

Estruture `numb3rs.py` da seguinte forma, em que você pode modificar `main` e/ou implementar outras funções conforme achar adequado, mas sem importar outras bibliotecas. Você pode, mas não é obrigado, usar `re` e/ou `sys`.

```python
import re
import sys

def main():
    print(validate(input("Endereço IPv4: ")))

def validate(ip):
    ...

...

if __name__ == "__main__":
    main()
```

Antes ou depois de implementar `validate` no arquivo `numb3rs.py`, implemente adicionalmente, em um arquivo chamado `test_numb3rs.py`, **duas ou mais** funções que testem de forma abrangente sua implementação de `validate`, cujos nomes devem começar com `test_` para que você possa executar seus testes com:

```bash
pytest test_numb3rs.py
```

Dicas

- Lembre-se de que o módulo `re` vem com várias funções, conforme [docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html), incluindo `search`.
- Lembre-se de que expressões regulares suportam vários caracteres especiais, conforme [docs.python.org/3/library/re.html#regular-expression-syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax).
- Devido a que barras invertidas em expressões regulares podem ser confundidas com sequências de escape (como `\n`), é melhor usar [a notação de string bruta do Python para padrões de expressão regular](https://docs.python.org/3/ library/re.html#module-re), senão o `pytest` emitirá um aviso de `DeprecationWarning: invalid escape sequence`. Assim como as strings de formatação são prefixadas com `f`, as strings brutas são prefixadas com `r`. Por exemplo, em vez de `"harvard\.edu"`, use `r"harvard\.edu"`.
- Note que `re.search`, se passado um padrão com "grupos de captura" (ou seja, parênteses), retorna um "objeto de correspondência", conforme [docs.python.org/3/library/re.html#match-objects](https://docs.python.org/3/library/re.html#match-objects), em que as correspondências são indexadas em 1 e podem ser acessadas individualmente com `group`, conforme [docs.python.org/3/library/re.html#re.Match.group](https://docs.python.org/3/library/re.html#re.Match.group), ou coletivamente com `groups`, conforme [docs.python.org/3/library/re.html#re.Match.groups](https://docs.python.org/3/library/re.html#re.Match.groups).

## Demonstração

## Antes de Começar

Faça login no [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute `cd`. Você deverá ver que o prompt da sua janela do terminal se parece com o seguinte:

```
$
```

Em seguida, execute

```bash
mkdir numb3rs
```

para criar uma pasta chamada `numb3rs` no seu espaço de códigos.

Depois, execute

```bash
cd numb3rs
```

para mudar para o diretório dessa pasta. Agora você deve ver o prompt do seu terminal como `numb3rs/ $`. Agora você pode executar

```bash
code numb3rs.py
```

para criar um arquivo chamado `numb3rs.py`, onde você escreverá seu programa. Certifique-se também de executar

```bash
code test_numb3rs.py
```

para criar um arquivo chamado `test_numb3rs.py`, onde você escreverá os testes para o seu programa.

## Como Testar

#### Como Testar `numb3rs.py`

Veja como testar `numb3rs.py` manualmente:

- Execute seu programa com `python numb3rs.py`. Certifique-se de que seu programa solicita um endereço IPv4. Digite `127.0.0.1`, seguido de Enter. Sua função `validate` deve retornar `True`.
- Execute seu programa com `python numb3rs.py`. Digite `255.255.255.255`, seguido de Enter. Sua função `validate` deve retornar `True`.
- Execute seu programa com `python numb3rs.py`. Digite `512.512.512.512`, seguido de Enter. Sua função `validate` deve retornar `False`.
- Execute seu programa com `python numb3rs.py`. Digite `1.2.3.1000`, seguido de Enter. Sua função `validate` deve retornar `False`.
- Execute seu programa com `python numb3rs.py`. Digite `cat`, seguido de Enter. Sua função `validate` deve retornar `False`.

#### Como Testar `test_numb3rs.py`

Para testar seus testes, execute `pytest test_numb3rs.py`. Tente usar versões corretas e incorretas de `numb3rs.py` para determinar quão bem seus testes identificam erros:

- Verifique se você tem uma versão correta de `numb3rs.py`. Execute seus testes executando `pytest test_numb3rs.py`. `pytest` deve mostrar que todos os seus testes passaram.
- Modifique a função `validate` na versão correta de `numb3rs.py`. `validate` pode, por exemplo, verificar apenas se o primeiro byte do endereço IPv4 é válido. Execute seus testes executando `pytest test_numb3rs.py`. `pytest` deve mostrar que pelo menos um dos seus testes falhou.
- Modifique novamente a versão correta de `numb3rs.py`. `validate` pode, por exemplo, erroneamente retornar `True` quando o usuário insere um formato IPv4 incorreto. Execute seus testes executando `pytest test_numb3rs.py`. `pytest` deve mostrar que pelo menos um dos seus testes falhou.

Você pode executar o comando abaixo para verificar seu código usando `check50`, um programa que a CS50 usará para testar seu código quando você enviar. Mas certifique-se de testar por conta própria também!

```bash
check50 cs50/problems/2022/python/numb3rs
```

Smiles verdes significam que seu programa passou em um teste! Carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que `check50` imprime para ver a entrada que `check50` forneceu ao seu programa, qual saída ele esperava e qual saída seu programa realmente deu.

## Como Enviar

No seu terminal, execute o comando abaixo para enviar seu trabalho.

```bash
submit50 cs50/problems/2022/python/numb3rs
```
