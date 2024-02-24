# Trabalhando das 9 às 17

Enquanto [a maioria dos países](https://en.wikipedia.org/wiki/Date_and_time_representation_by_country#Time) usa um [relógio de 24 horas](https://en.wikipedia.org/wiki/24-hour_clock), os Estados Unidos tendem a usar um [relógio de 12 horas](https://en.wikipedia.org/wiki/12-hour_clock). Portanto, em vez de "09:00 às 17:00", muitos americanos diriam que trabalham "9:00 AM às 5:00 PM" (ou "9 AM às 5 PM"), onde "AM" é uma abreviação de "ante meridiem" e "PM" é uma abreviação de "post meridiem", em que "meridiem" significa meio-dia (ou seja, meio-dia).

<details><summary>Tabela de Conversão</summary><p>Assim como “12:00 AM” no formato de 12 horas seria “00:00” no formato de 24 horas, "12:01 AM" a "12:59 AM" seriam "00:01" a "00:59", respectivamente.</p>
| 12-Horas | 24-Horas |
| -------- | ------- |
| 12:00 AM | 00:00   |
| 1:00 AM  | 01:00   |
| 2:00 AM  | 02:00   |
| ... |
</details>

Em um arquivo chamado `working.py`, implemente uma função chamada `convert` que espera uma `str` em um dos formatos de 12 horas abaixo e retorna a `str` correspondente no formato de 24 horas (ou seja, `9:00 to 17:00`). Espere que `AM` e `PM` sejam em maiúsculas (sem pontos) e que haja um espaço antes de cada um. Considere que esses horários representam horários reais, não necessariamente 9:00 AM e 5:00 PM especificamente.

- `9:00 AM to 5:00 PM`
- `9 AM to 5 PM`

Lance um `ValueError` se a entrada em `convert` não estiver em nenhum desses formatos ou se algum dos horários for inválido (por exemplo, `12:60 AM`, `13:00 PM`, etc.). Mas não assuma que as horas de alguém começarão ante meridiem e terminarão post meridiem; alguém pode trabalhar até tarde e até longas horas (por exemplo, `5:00 PM to 9:00 AM`).

Estruture `working.py` da seguinte forma, em que você pode modificar `main` e/ou implementar outras funções conforme achar melhor, mas não pode importar outras bibliotecas. Você pode optar, mas não é obrigatório, por usar `re` e/ou `sys`.

    import re
    import sys

    def main():
        print(convert(input("Horas: "))

    def convert(s):
        ...

    ...

    if __name__ == "__main__":
        main()

Antes ou depois de implementar `convert` em `working.py`, implemente também, em um arquivo chamado `test_working.py`, **três ou mais** funções que testem cuidadosamente sua implementação de `convert`, cada uma com nomes começando com `test_`, para que você possa executar seus testes com:

    pytest test_working.py

<details><summary>Dicas</summary><ul>
  <li data-marker="*">Recorde que o módulo <code class="language-plaintext highlighter-rouge">re</code> tem muitas funções, consulte <a href="https://docs.python.org/3/library/re.html">docs.python.org/3/library/re.html</a>, incluindo <code class="language-plaintext highlighter-rouge">search</code>.</li>
  <li data-marker="*">Recorde que expressões regulares suportam diversos caracteres especiais, consulte <a href="https://docs.python.org/3/library/re.html#regular-expression-syntax">docs.python.org/3/library/re.html#regular-expression-syntax</a>.</li>
  <li data-marker="*">Porque barras invertidas em expressões regulares podem ser confundidas com sequências de escape (como <code class="language-plaintext highlighter-rouge">\n</code>), é melhor usar a <a href="https://docs.python.org/3/library/re.html#module-re">notação raw string do Python para padrões de expressões regulares</a>, senão o `pytest` emitirá um aviso de <code class="language-plaintext highlighter-rouge">DeprecationWarning: invalid escape sequence</code>. Assim como as strings de formatação são prefixadas com <code class="language-plaintext highlighter-rouge">f</code>, as strings raw são prefixadas com <code class="language-plaintext highlighter-rouge">r</code>. Por exemplo, em vez de <code class="language-plaintext highlighter-rouge">"harvard\.edu"</code>, use <code class="language-plaintext highlighter-rouge">r"harvard\.edu"</code>.</li>
  <li data-marker="*">Note que <code class="language-plaintext highlighter-rouge">re.search</code>, se passado um padrão com "grupos de captura" (ou seja, parênteses), retorna um “objeto de correspondência”, consulte <a href="https://docs.python.org/3/library/re.html#match-objects">docs.python.org/3/library/re.html#match-objects</a>, onde as correspondências são indexadas em 1, que podem ser acessadas individualmente com <code class="language-plaintext highlighter-rouge">group</code>, consulte <a href="https://docs.python.org/3/library/re.html#re.Match.group">docs.python.org/3/library/re.html#re.Match.group</a>, ou coletivamente com <code class="language-plaintext highlighter-rouge">groups</code>, consulte <a href="https://docs.python.org/3/library/re.html#re.Match.groups">docs.python.org/3/library/re.html#re.Match.groups</a>.</li>
  <li data-marker="*">Note que você pode formatar um <code class="language-plaintext highlighter-rouge">int</code> com zeros à esquerda com um código como
    <div class="language-py highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="si">{</span><span class="n">n</span><span class="si">:</span><span class="mi">02</span><span class="si">}</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div>    </div>
    <p>onde, se <code class="language-plaintext highlighter-rouge">n</code> for um dígito único, ele será prefixado com um <code class="language-plaintext highlighter-rouge">0</code>, consulte <a href="https://docs.python.org/3/library/string.html#format-string-syntax">docs.python.org/3/library/string.html#format-string-syntax</a>.</p>
  </li>
</ul></details>
## Demonstração

## Antes de Começar

Faça login em [cs50.dev](https://cs50.dev/), clique na sua janela de terminal e execute `cd` sozinho. Você deverá ver que o prompt da sua janela de terminal se parece com o seguinte:

    $

Em seguida, execute

    mkdir working

para criar uma pasta chamada `working` no seu espaço de códigos.

Depois execute

    cd working

para entrar na pasta recém-criada. Agora você deve ver o prompt do terminal como `working/ $`. Você pode então executar

    code working.py

para criar um arquivo chamado `working.py`, onde você escreverá seu programa. Certifique-se também de executar

    code test_working.py

para criar um arquivo chamado `test_working.py`, onde você escreverá os testes para seu programa.

## Como Testar

#### Como Testar `working.py`

Aqui está como testar `working.py` manualmente:

- Execute seu programa com `python working.py`. Verifique se o programa solicita um horário. Digite `9 AM to 5 PM` e pressione Enter. Seu programa deve exibir `09:00 to 17:00`.
- Execute seu programa com `python working.py`. Digite `9:00 AM to 5:00 PM` e pressione Enter. Seu programa deve novamente exibir `09:00 to 17:00`.
- Execute seu programa com `python working.py`. Verifique se o programa solicita um horário. Digite `10 PM to 8 AM` e pressione Enter. Seu programa deve exibir `22:00 to 08:00`.
- Execute seu programa com `python working.py`. Verifique se o programa solicita um horário. Digite `10:30 PM to 8:50 AM` e pressione Enter. Seu programa deve novamente exibir `22:30 to 08:50`.
- Execute seu programa com `python working.py`. Verifique se o programa solicita um horário. Tente intencionalmente induzir um `ValueError` digitando `9:60 AM to 5:60 PM` e pressione Enter. Seu programa deve de fato lançar um `ValueError`.
- Execute seu programa com `python working.py`. Verifique se o programa solicita um horário. Tente intencionalmente induzir um `ValueError` digitando `9 AM - 5 PM` e pressione Enter. Seu programa deve de fato lançar um `ValueError`.
- Execute seu programa com `python working.py`. Verifique se o programa solicita um horário. Tente intencionalmente induzir um `ValueError` digitando `09:00 AM - 17:00 PM` e pressione Enter. Seu programa deve de fato lançar um `ValueError`.

#### Como Testar `test_working.py`

Para testar seus testes, execute `pytest test_working.py`. Use versões corretas e incorretas de `working.py` para verificar se seus testes identificam erros:

- Verifique se você tem uma versão correta de `working.py`. Execute seus testes com `pytest test_working.py`. O `pytest` deve mostrar que todos os testes foram aprovados.
- Modifique a versão correta de `working.py`, especialmente sua função `convert`. Por exemplo, seu programa pode falhar em lançar um `ValueError` quando deveria. Execute seus testes com `pytest test_working.py`. O `pytest` deve mostrar que pelo menos um teste falhou.
- Da mesma forma, modifique a versão correta de `working.py`, alterando os valores de retorno de `convert`. Seu programa, por exemplo, pode inadvertidamente omitir minutos. Execute seus testes com `pytest test_working.py`. O `pytest` deve mostrar que pelo menos um teste falhou.

Você pode executar o código abaixo para verificar o seu código usando `check50`, um programa que o CS50 usará para testar seu código quando você enviar. Mas lembre-se de testá-lo também!

    check50 cs50/problems/2022/python/working

Carinhas sorridentes verdes significam que seu programa passou no teste! Carinhas tristes vermelhas indicarão que seu programa produziu algo inesperado. Visite a URL que o `check50` fornece para ver a entrada que o `check50` forneceu ao seu programa, a saída esperada e a saída real do seu programa.

## Como Enviar

No seu terminal, execute o comando abaixo para enviar seu trabalho.

    submit50 cs50/problems/2022/python/working
