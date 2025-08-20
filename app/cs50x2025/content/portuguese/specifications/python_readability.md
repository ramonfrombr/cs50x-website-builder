# Legibilidade

## Problema a ser resolvido

Escreva, em um arquivo chamado `readability.py` em uma pasta chamada `sentimental-readability`, um programa que primeiro pede ao usuário para digitar algum texto e então exibe o nível para o texto, de acordo com a fórmula de Coleman-Liau, exatamente como você fez no [Conjunto de Problemas 2](../../2/), exceto que dessa vez seu programa deve ser escrito em Python.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-WnE6pZNnDkDm8NtuxrTqY1Nu4" src="https://asciinema.org/a/WnE6pZNnDkDm8NtuxrTqY1Nu4.js"></script>

## Especificação

- Lembre-se de que o índice de Coleman-Liau é calculado como `0,0588 * L - 0,296 * S - 15,8`, onde `L` é o número médio de letras por 100 palavras no texto, e `S` é o número médio de frases por 100 palavras no texto.
- Use `get_string` da Biblioteca CS50 para obter a entrada do usuário, e `print` para exibir sua resposta.
- Seu programa deve contar o número de letras, palavras e frases no texto. Você pode assumir que uma letra é qualquer caractere minúsculo de `a` a `z` ou qualquer caractere maiúsculo de `A` a `Z`, qualquer sequência de caracteres separados por espaços deve contar como uma palavra, e que qualquer ocorrência de um ponto, ponto de exclamação ou ponto de interrogação indica o final de uma frase.
- Seu programa deve imprimir como saída `"Ano X"` onde `X` é o nível do ano calculado pela fórmula de Coleman-Liau, arredondado para o inteiro mais próximo.
- Se o número do índice resultante for 16 ou superior (equivalente ou maior que o nível de leitura de graduação sênior), seu programa deve exibir `"Ano 16+"` ao invés de fornecer o número exato do índice. Se o número do índice for menor que 1, seu programa deve exibir `"Antes do Ano 1"`.

## Como testar

Embora `check50` esteja disponível para esse problema, você é incentivado a testar seu código por conta própria para cada um dos seguintes itens.

- Execute seu programa como `python readability.py` e aguarde um prompt para entrada. Digite `One fish. Two fish. Red fish. Blue fish.` e pressione enter. Seu programa deve exibir `Before Grade 1` (Antes do Ano 1).
- Execute seu programa como `python readability.py` e aguarde um prompt para entrada. Digite `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` e pressione enter. Seu programa deve exibir `Grade 2` (Ano 2).
- Execute seu programa como `python readability.py` e aguarde um prompt para entrada. Digite `Congratulations! Today is your day. You're off to Great Places! You're off and away!` e pressione enter. Seu programa deve exibir `Grade 3` (Ano 3).
- Execute seu programa como `python readability.py` e aguarde um prompt para entrada. Digite `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` e pressione enter. Seu programa deve exibir `Grade 5` (Ano 5).
- Execute seu programa como `python readability.py` e aguarde um prompt para entrada. Digite `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` e pressione enter. Seu programa deve exibir `Grade 7` (Ano 7).
- Execute seu programa como `python readability.py` e aguarde um prompt para entrada. Digite `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` e pressione enter. Seu programa deve exibir `Grade 8` (Ano 8).
- Execute seu programa como `python readability.py` e aguarde um prompt para entrada. Digite `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` e pressione enter. Seu programa deve exibir `Grade 8` (Ano 8).
- Execute seu programa como `python readability.py` e aguarde um prompt para entrada. Digite `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` e pressione enter. Seu programa deve exibir `Grade 9` (Ano 9).
- Execute seu programa como `python readability.py` e aguarde um prompt para entrada. Digite `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` e pressione enter. Seu programa deve exibir `Grade 10` (Ano 10).
- Execute seu programa como `python readability.py` e aguarde um prompt para entrada. Digite `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` e pressione enter. Seu programa deve exibir `Grade 16+` (Ano 16+).

### Correção

    check50 cs50/problems/2024/x/sentimental/readability

### Estilo

    style50 readability.py

## Como enviar

    submit50 cs50/problems/2024/x/sentimental/readability