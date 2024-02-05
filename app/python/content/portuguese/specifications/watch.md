# Assista no YouTube

Acontece que (a maioria) dos vídeos do YouTube podem ser incorporados em outros websites, assim como o acima. Por exemplo, se você visitar [https://youtu.be/xvFZjo5PgG0](https://youtu.be/xvFZjo5PgG0) em um laptop ou desktop, clique em **Compartilhar**, e então clique em **Incorporar**, você verá [HTML](https://en.wikipedia.org/wiki/HTML) (a linguagem na qual as páginas web são escritas) como abaixo, que você pode então copiar para o código-fonte do seu próprio site, em que [`iframe`](https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/iframe) é um “elemento” HTML, e `src` é um dos vários “atributos” HTML lá dentro, cujo valor, entre aspas, é `https://www.youtube.com/embed/xvFZjo5PgG0`.

.html pre { white-space: pre-wrap; }

    <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="Reprodutor de vídeo do YouTube" frameborder="0" allow="acelerômetro; reprodução automática; escrita da área de transferência; mídia criptografada; giroscópio; imagem na imagem" allowfullscreen></iframe>

Como alguns atributos HTML são opcionais, você poderia incorporar minimamente apenas o abaixo.

    <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

Suponha que você gostaria de extrair os URLs de vídeos do YouTube que estão incorporados em páginas (por exemplo, `https://www.youtube.com/embed/xvFZjo5PgG0`), convertendo-os de volta para URLs mais curtos e compartilháveis do `youtu.be` (por exemplo, `https://youtu.be/xvFZjo5PgG0`), onde eles podem ser assistidos no próprio YouTube.

Em um arquivo chamado `watch.py`, implemente uma função chamada `parse` que espera uma `str` de HTML como entrada, extrai qualquer URL do YouTube que seja o valor de um atributo `src` de um elemento `iframe` ali dentro, e retorna sua versão mais curta e compartilhável do `youtu.be` como uma `str`. Espere que tal URL esteja em um dos formatos abaixo. Assuma que o valor de `src` estará entre aspas duplas. E assuma que a entrada não conterá mais do que um URL desse tipo. Se a entrada não contiver nenhum URL desse tipo, retorne `None`.

- `http://youtube.com/embed/xvFZjo5PgG0`
- `https://youtube.com/embed/xvFZjo5PgG0`
- `https://www.youtube.com/embed/xvFZjo5PgG0`

Estruture `watch.py` da seguinte forma, em que você pode modificar `main` e/ou implementar outras funções conforme achar adequado, mas não poderá importar outras bibliotecas. Você está livre, mas não é necessário, usar `re` e/ou `sys`.

    import re
    import sys


    def main():
        print(parse(input("HTML: ")))


    def parse(s):
        ...


    ...


    if __name__ == "__main__":
        main()

Dicas

- Lembre-se de que o módulo `re` vem com várias funções, conforme [docs.python.org/pt-BR/3/library/re.html](https://docs.python.org/pt-BR/3/library/re.html), incluindo `search`.
- Lembre-se de que expressões regulares suportam vários caracteres especiais, conforme [docs.python.org/pt-BR/3/library/re.html#regular-expression-syntax](https://docs.python.org/pt-BR/3/library/re.html#regular-expression-syntax).
- Como barras invertidas em expressões regulares podem ser confundidas com sequências de escape (como `\n`), é melhor usar [a notação de string bruta do Python para padrões de expressões regulares](https://docs.python.org/pt-BR/3/library/re.html#module-re). Assim como as strings de formatação são prefixadas com `f`, as raw strings são prefixadas com `r`. Por exemplo, em vez de `"harvard\.edu"`, use `r"harvard\.edu"`.
- Observe que `re.search`, se passado um padrão com “grupos de captura” (ou seja, parênteses), retorna um “objeto de correspondência”, conforme [docs.python.org/pt-BR/3/library/re.html#match-objects](https://docs.python.org/pt-BR/3/library/re.html#match-objects), em que as correspondências são indexadas em 1, o que você pode acessar individualmente com `group`, conforme [docs.python.org/pt-BR/3/library/re.html#re.Match.group](https://docs.python.org/pt-BR/3/library/re.html#re.Match.group), ou coletivamente com `groups`, conforme [docs.python.org/pt-BR/3/library/re.html#re.Match.groups](https://docs.python.org/pt-BR/3/library/re.html#re.Match.groups).
- Observe que `*` e `+` são “gananciosos”, na medida em que “correspondem o máximo possível de texto”, conforme [docs.python.org/pt-BR/3/library/re.html#regular-expression-syntax](https://docs.python.org/pt-BR/3/library/re.html#regular-expression-syntax). Adicionar `?` imediatamente após um deles, como `*?` ou `+?`, “faz com que a correspondência seja feita de forma não gananciosa ou mínima; o mínimo possível de caracteres será correspondido”.

## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela de terminal se assemelha ao abaixo:

    $

Em seguida, execute

    mkdir watch

para criar uma pasta chamada `watch` no seu espaço de códigos.

Depois execute

    cd watch

para entrar nessa pasta. Agora você deverá ver o prompt do terminal como `watch/ $`. Agora, execute

    code watch.py

para criar um arquivo chamado `watch.py`, onde você escreverá seu programa.

## Como Testar

Segue a forma de testar seu código manualmente:

- Execute seu programa com `python watch.py`. Verifique se o programa solicita HTML, então copie/cole o seguinte:

      <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

  Pressione enter e seu programa deverá exibir `https://youtu.be/xvFZjo5PgG0`. Observe como, embora o atributo `src` seja prefixado com `http://www.youtube.com/embed/`, o link resultante é prefixado com `https://youtu.be/`.

- Execute seu programa com `python watch.py`. Verifique se o programa solicita HTML, então copie/cole o seguinte:

      <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="Reprodutor de vídeo do YouTube" frameborder="0" allow="acelerômetro; reprodução automática; escrita da área de transferência; mídia criptografada; giroscópio; imagem na imagem" allowfullscreen></iframe>

  Pressione enter e seu programa ainda deverá exibir `https://youtu.be/xvFZjo5PgG0`.

- Execute seu programa com `python watch.py`. Verifique se o programa solicita HTML, então copie/cole o seguinte:

      <iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>

  Pressione enter e seu programa deverá exibir `None`. Observe como o atributo `src` não aponta para um link do YouTube!

Você pode executar o abaixo para verificar seu código usando `check50`, um programa que o CS50 usará para testar seu código quando você o enviar. Mas certifique-se de testá-lo também por conta própria!

    check50 cs50/problems/2022/python/watch

Carinhas verdes significam que seu programa passou no teste! Carinhas vermelhas indicarão que seu programa produziu algo inesperado. Visite o URL que o `check50` fornecer para ver a entrada que `check50` passou para seu programa, o resultado esperado e o resultado real fornecido por seu programa.

## Como Enviar

No seu terminal, execute o abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/watch
