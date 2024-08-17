# Filmes

![Logotipo do IMDb](https://cs50.harvard.edu/x/2024/psets/7/movies/imdb.png)

## Problema aResolver

Foi fornecido um arquivo chamado `movies.db`, um banco de dados SQLite que armazena dados do [IMDb](https://www.imdb.com/) sobre filmes, as pessoas que os dirigiram e estrelaram e suas classificações. Escreva consultas SQL para responder a perguntas sobre esse banco de dados de filmes.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-uPWDqSe0NjjqXLF3qxzpsMnfv" src="https://asciinema.org/a/uPWDqSe0NjjqXLF3qxzpsMnfv.js"></script>

## Introdução

Para este problema, você usará um banco de dados fornecido pela equipe do CS50.

Faça login em [cs50.dev](https://cs50.dev/), clique em sua janela de terminal e execute apenas `cd`. Você deve observar que o prompt de sua janela de terminal se assemelha ao abaixo:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/7/movies.zip

para baixar um ZIP chamado `movies.zip` para o seu espaço de códigos.

Em seguida, execute

    unzip movies.zip

para criar uma pasta chamada `movies`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm movies.zip

e responda com "s" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd movies

seguido de Enter para se mover (ou seja, abrir) esse diretório. Seu prompt agora deve se parecer com o abaixo.

    movies/ $

Execute `ls` sozinho e você verá 13 arquivos .sql, bem como `movies.db`.

Se você tiver algum problema, siga os mesmos passos novamente e veja se consegue determinar onde errou!

## Especificação

Para cada um dos problemas a seguir, você deve escrever uma única consulta SQL que gere os resultados especificados por cada problema. Sua resposta deve assumir a forma de uma única consulta SQL, embora você possa aninhar outras consultas dentro de sua consulta. Você **não deve** presumir nada sobre os `id`s de quaisquer filmes ou pessoas em particular: suas consultas devem ser precisas mesmo que o `id` de qualquer filme ou pessoa em particular seja diferente. Finalmente, cada consulta deve retornar apenas os dados necessários para responder à pergunta: se o problema apenas pedir que você emita os nomes dos filmes, por exemplo, então sua consulta não deve também emitir o ano de lançamento de cada filme.

Você é bem-vindo para checar os resultados de suas consultas em [IMDb](https://www.imdb.com/) em si, mas perceba que as classificações no site podem diferir daquelas em `movies.db`, pois mais votos podem ter sido emitidos desde que baixamos os dados!

1. Em `1.sql`, escreva uma consulta SQL para listar os títulos de todos os filmes lançados em 2008.
    - Sua consulta deve retornar uma tabela com uma única coluna para o título de cada filme.
2. Em `2.sql`, escreva uma consulta SQL para determinar o ano de nascimento de Emma Stone.
    - Sua consulta deve retornar uma tabela com uma única coluna e uma única linha (sem contar o cabeçalho) contendo o ano de nascimento de Emma Stone.
    - Você pode presumir que haja apenas uma pessoa no banco de dados com o nome Emma Stone.
3. Em `3.sql`, escreva uma consulta SQL para listar os títulos de todos os filmes com uma data de lançamento em ou após 2018, em ordem alfabética.
    - Sua consulta deve retornar uma tabela com uma única coluna para o título de cada filme.
    - Filmes lançados em 2018 devem ser incluídos, assim como filmes com datas de lançamento no futuro.
4. Em `4.sql`, escreva uma consulta SQL para determinar o número de filmes com uma classificação do IMDb de 10,0.
    - Sua consulta deve retornar uma tabela com uma única coluna e uma única linha (sem contar o cabeçalho) contendo o número de filmes com uma classificação de 10,0.
5. Em `5.sql`, escreva uma consulta SQL para listar os títulos e anos de lançamento de todos os filmes de Harry Potter, em ordem cronológica.
    - Sua consulta deve retornar uma tabela com duas colunas, uma para o título de cada filme e outra para o ano de lançamento de cada filme.
    - Você pode presumir que o título de todos os filmes de Harry Potter começará com as palavras "Harry Potter" e que se um título de filme começar com as palavras "Harry Potter", é um filme de Harry Potter.
6. Em `6.sql`, escreva uma consulta SQL para determinar a classificação média de todos os filmes lançados em 2012.
    - Sua consulta deve retornar uma tabela com uma única coluna e uma única linha (sem contar o cabeçalho) contendo a classificação média.
7. Em `7.sql`, escreva uma consulta SQL para listar todos os filmes lançados em 2010 e suas classificações, em ordem decrescente por classificação. Para filmes com a mesma classificação, ordene-os alfabeticamente por título.
    - Sua consulta deve retornar uma tabela com duas colunas, uma para o título de cada filme e outra para a classificação de cada filme.
    - Filmes que não possuem classificações não devem ser incluídos no resultado.
8. Em `8.sql`, escreva uma consulta SQL para listar os nomes de todas as pessoas que estrelaram Toy Story.
    - Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada pessoa.
    - Você pode presumir que haja apenas um filme no banco de dados com o título Toy Story.
9. Em `9.sql`, escreva uma consulta SQL para listar os nomes de todas as pessoas que estrelaram um filme lançado em 2004, ordenados por ano de nascimento.
    - Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada pessoa.
    - Pessoas com o mesmo ano de nascimento podem ser listadas em qualquer ordem.
    - Não precisa se preocupar com pessoas que não têm um ano de nascimento listado, contanto que aqueles que têm um ano de nascimento sejam listados em ordem.
    - Se uma pessoa apareceu em mais de um filme em 2004, ela só deve aparecer em seus resultados uma vez.
10. Em `10.sql`, escreva uma consulta SQL para listar os nomes de todas as pessoas que dirigiram um filme que recebeu uma classificação de pelo menos 9,0.
    - Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada pessoa.
    - Se uma pessoa dirigiu mais de um filme que recebeu uma classificação de pelo menos 9,0, ela só deve aparecer em seus resultados uma vez.
11. Em `11.sql`, escreva uma consulta SQL para listar os títulos dos cinco filmes mais bem avaliados (em ordem) que Chadwick Boseman estrelou, começando com o mais bem avaliado.
    - Sua consulta deve retornar uma tabela com uma única coluna para o título de cada filme.
    - Você pode presumir que haja apenas uma pessoa no banco de dados com o nome Chadwick Boseman.
12. Em `12.sql`, escreva uma consulta SQL para listar os títulos de todos os filmes em que Bradley Cooper e Jennifer Lawrence estrelaram.
    - Sua consulta deve retornar uma tabela com uma única coluna para o título de cada filme.
    - Você pode presumir que haja apenas uma pessoa no banco de dados com o nome Bradley Cooper.
    - Você pode presumir que haja apenas uma pessoa no banco de dados com o nome Jennifer Lawrence.
13. Em `13.sql`, escreva uma consulta SQL para listar os nomes de todas as pessoas que estrelaram um filme em que Kevin Bacon também estrelou.
    - Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada pessoa.
    - Pode haver várias pessoas chamadas Kevin Bacon no banco de dados. Certifique-se de selecionar apenas o Kevin Bacon nascido em 1958.
    - O próprio Kevin Bacon não deve ser incluído na lista resultante.

## Dicas

### Entenda o esquema de `movies.db`

Sempre que você se envolve com um novo banco de dados, é melhor entender primeiro seu _esquema_. Em uma janela de terminal, execute `sqlite3 movies.db` para que você possa começar a executar consultas no banco de dados.

Primeiro, quando `sqlite3` solicitar que você forneça uma consulta, digite `.schema` e pressione enter. Isso irá gerar as instruções `CREATE TABLE` que foram usadas para gerar cada uma das tabelas no banco de dados. Ao examinar essas instruções, você pode identificar as colunas presentes em cada tabela.

Observe que a tabela `movies` tem uma coluna `id` que identifica exclusivamente cada filme, bem como colunas para o `title` do filme e o `year` em que o filme foi lançado. A tabela `people` também tem uma coluna `id` e também tem colunas para o `name` e o ano de `birth` de cada pessoa.

As classificações de filmes são armazenadas na tabela `ratings`. A primeira coluna da tabela é `movie_id`: uma chave estrangeira que referencia o `id` da tabela `movies`. O restante da linha contém dados sobre a `rating` de cada filme e o número de `votes` que o filme recebeu no IMDb.

Finalmente, as tabelas `stars` e `directors` fazem a correspondência entre pessoas e filmes nos quais elas atuaram ou dirigiram. (Somente [principais](https://www.imdb.com/interfaces/) estrelas e diretores estão incluídos.) Cada tabela possui apenas duas colunas: `movie_id` e `person_id`, que fazem referência a um filme e pessoa específicos, respectivamente.

O desafio à sua frente é escrever consultas SQL para responder a uma variedade de diferentes perguntas selecionando dados de uma ou mais dessas tabelas.

### Estilos consistentes de consultas

Veja [sqlstyle.guide](https://www.sqlstyle.guide/) para dicas sobre bom estilo em SQL, especialmente à medida que suas consultas ficam mais complexas!

### Liste os títulos de todos os filmes lançados em 2008

Lembre-se de que você pode selecionar uma (ou mais) colunas de um banco de dados usando `SELECT`, de acordo com o exemplo a seguir,

    SELECT coluna0, coluna1 FROM tabela;

onde `coluna0` é o título de uma coluna e `coluna1` é o título de outra.

E lembre-se de que você pode filtrar as linhas retornadas em uma consulta com a palavra-chave `WHERE`, seguida por uma condição. Você pode usar `=`, `>`, `<` e [outros operadores](https://www.w3schools.com/sql/sql_operators.asp) também.

    SELECT coluna FROM tabela
    WHERE condição;

Veja [esta referência de palavras-chave SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para alguma sintaxe SQL que pode ser útil!

### Determine o ano de nascimento de Emma Stone

Lembre-se de que uma cláusula `WHERE` pode avaliar condições não apenas com números, mas com strings.

### Liste os títulos de todos os filmes com data de lançamento em ou após 2018, em ordem alfabética

Tente dividir esta consulta em duas etapas. Primeiro, encontre os filmes com uma data de lançamento em ou após 2018. Em seguida, coloque os títulos desses filmes em ordem alfabética.

Para encontrar os filmes com uma data de lançamento em ou após 2018, lembre-se de que uma condição em SQL oferece suporte ao uso de muitos [operadores de comparação](https://www.w3schools.com/sql/sql_operators.asp) comuns, incluindo `>=` para "maior ou igual a". Verifique se sua consulta retorna o número correto de filmes, de acordo com [Como testar](#como-testar).

Finalmente, classifique os resultados da consulta em ordem alfabética por título. Lembre-se de que `ORDER BY` pode classificar dados por uma coluna em seus resultados, de acordo com o exemplo a seguir.

    ...
    ORDER BY coluna;

### Determine o número de filmes com uma classificação do IMDb de 10.0

Observe que esta pergunta não lhe pede filmes _individuais_ com uma classificação de 10.0, mas sim o _número_ de filmes com essa classificação. Em outras palavras, você deve coletar (“agregar”) os resultados de sua consulta em um único número (o número de linhas). Lembre-se de que o SQL oferece suporte a uma “função de agregação” chamada `COUNT`, que você pode usar em uma coluna de acordo com o exemplo abaixo.

    SELECT COUNT(coluna)
    FROM tabela;

### Liste os títulos e os anos de lançamento de todos os filmes de Harry Potter, em ordem cronológica

Para esta consulta, você provavelmente vai querer usar a palavra-chave `LIKE` do SQL. Lembre-se de que `LIKE` pode fazer uso dos chamados “caracteres curinga”, como `%`, que corresponderá a qualquer caractere (ou sequência deles).

    SELECT coluna0, coluna1
    FROM tabela
    WHERE coluna1 LIKE padrão;

### Determine a classificação média de todos os filmes lançados em 2012

Aqui está outro exemplo de consulta na qual você precisará agregar dados. Considere a função de agregação `AVG` do SQL para calcular uma média.

Considere também que esta consulta faz uso de dados armazenados em duas tabelas separadas: `ratings` e `movies`. Lembre-se de que, desde que uma tabela tenha uma chave estrangeira que corresponda a uma coluna em outra tabela, você pode combinar duas tabelas usando a palavra-chave `JOIN` do SQL. Para usar a palavra-chave `JOIN`, você deve especificar a tabela à qual gostaria de fazer a junção e a coluna pela qual fazer isso.

    SELECT coluna0
    FROM tabela0
    JOIN tabela1 ON tabela0.coluna1 = tabela1.coluna2

### Liste todos os filmes lançados em 2010 e suas classificações, em ordem decrescente por classificação

Lembre-se de que `ORDER BY` não precisa sempre classificar em ordem crescente. Você pode especificar que seus resultados sejam classificados em ordem _decrescente_ anexando `DESC`.

    ...
    ORDER BY coluna DESC;

### Liste os nomes de todas as pessoas que estrelaram em Toy Story

Quando você vê uma consulta mais complexa como essa, é melhor dividi-la em partes menores. No final das contas, sua consulta deve chegar a uma lista de nomes, conforme abaixo.

    -- Selecione nomes
    SELECT name
    FROM people
    WHERE ...

Mas qual é a melhor maneira de chegar aos nomes daqueles que estrelaram em Toy Story? Considere que a tabela `people` sozinha não tem essa informação (mas a tabela `stars` pode ter!). Na verdade, a tabela `stars` combina duas colunas, `person_id` e `movie_id`: qualquer pessoa com um `person_id` associado ao `movie_id` de Toy Story estrelaram em Toy Story.

    -- Selecione nomes
    SELECT name
    FROM people
    WHERE ...

    -- Selecione IDs de pessoa
    SELECT person_id
    FROM stars
    WHERE movie_id = ...

Um próximo passo natural, então, é encontrar o ID do filme Toy Story.

    -- Selecione nomes
    SELECT name
    FROM people
    WHERE ...

    -- Selecione IDs de pessoa
    SELECT person_id
    FROM stars
    WHERE movie_id = ...

    -- Encontre o ID do Toy Story
    SELECT id
    FROM movies
    WHERE title = 'Toy Story';

Claro, você atualmente escreveu três consultas _separadas_. Mas observe que algumas consultas (as duas primeiras) seriam completas incluindo os resultados da consulta diretamente abaixo delas. O processo de fazer uma consulta que depende dos resultados de uma "subconsulta" é chamado de consultas de "aninhamento". É uma dica e tanto, mas aqui está uma maneira de aninhar as consultas acima!

    -- Selecione nomes
    SELECT name
    FROM people
    WHERE id IN
    (
        -- Selecione IDs de pessoa
        SELECT person_id
        FROM stars
        WHERE movie_id = (

            -- Selecione o ID do Toy Story
            SELECT id
            FROM movies
            WHERE title = 'Toy Story'
        )
    );

### Liste os nomes de todas as pessoas que estrelaram em um filme lançado em 2004, ordenado por ano de nascimento

Observe que esta consulta, como a anterior, requer que você use dados de várias tabelas. Lembre-se de que você pode "aninhamento" de consultas em SQL, o que permite dividir uma consulta maior em outras menores. Talvez você possa escrever consultas para…

1. Encontre os IDs dos filmes lançados em 2004
2. Encontre os IDs das pessoas que estrelaram esses filmes
3. Encontre os nomes das pessoas com esses IDs

Em seguida, tente aninhar essas consultas para chegar a uma única consulta que retorne todas as pessoas que estrelaram um filme lançado em 2004. Considere como você pode ordenar os resultados de sua consulta.

### Liste os nomes de todas as pessoas que dirigiram um filme que recebeu uma classificação de pelo menos 9,0

Observe que esta consulta, como a anterior, requer que você use dados de várias tabelas. Lembre-se de que você pode "aninhamento" de consultas em SQL, o que permite dividir uma consulta maior em outras menores. Talvez você possa escrever consultas para…

1. Encontre os IDs dos filmes com pelo menos 9,0 de classificação
2. Encontre os IDs das pessoas que dirigiram esses filmes
3. Encontre os nomes das pessoas com esses IDs

Em seguida, tente aninhar essas consultas para chegar a uma única consulta que retorne os nomes de todas as pessoas que dirigiram um filme que recebeu uma classificação de pelo menos 9,0.

### Liste os títulos dos cinco filmes com maior classificação (em ordem) que Chadwick Boseman estrelou, começando com o de maior classificação

Observe que esta consulta, como a anterior, requer que você use dados de várias tabelas. Lembre-se de que você pode "aninhamento" de consultas em SQL, o que permite dividir uma consulta maior em outras menores. Talvez você possa escrever consultas para…

1. Encontre o ID de Chadwick Boseman
2. Encontre os IDs dos filmes associados ao ID de Chadwick Boseman
3. Encontre os títulos dos filmes com esses IDs de filme

Em seguida, tente aninhar essas consultas para chegar a uma única consulta que retorne os títulos dos filmes de Chadwick Boseman.

A partir daí, você precisará determinar as classificações desses títulos e classificá-los em ordem decrescente. Considere como você pode combinar uma tabela relevante (provavelmente `classificações`!) e ordenar os resultados por uma coluna relevante.

Finalmente, leia sobre a palavra-chave [`LIMIT`](https://www.sqlitetutorial.net/sqlite-limit/) do SQL, que retornará as \\(n\\) linhas principais em uma consulta.

### Listar os títulos de todos os filmes em que tanto Bradley Cooper quanto Jennifer Lawrence estrelaram

Note que esta consulta, assim como a anterior, requer que você use dados de diversas tabelas. Lembre-se que você pode "aninha" consultas em SQL, o que permite que você divida uma consulta maior em consultas menores. Talvez você possa escrever consultas para...

1.  Encontrar o ID de Bradley Cooper
2.  Encontrar o ID de Jennifer Lawrence
3.  Encontrar os IDs dos filmes associados ao ID de Bradley Cooper
4.  Encontrar os IDs dos filmes associados ao ID de Jennifer Lawrence
5.  Encontrar os títulos dos filmes dos IDs dos filmes associados _tanto_ com Bradley Cooper quanto com Jennifer Lawrence

Então, tente aninhar essas consultas para chegar em uma única consulta que retorne os filmes em que tanto Bradley Cooper quanto Jennifer Lawrence estrelaram.

Lembre-se que você pode construir condições compostas em SQL usando `AND` ou `OR`.

### Listar os nomes de todas as pessoas que estrelaram um filme em que Kevin Bacon também estrelou

Note que esta consulta, assim como a anterior, requer que você use dados de diversas tabelas. Lembre-se que você pode "aninha" consultas em SQL, o que permite que você divida uma consulta maior em consultas menores. Talvez você possa escrever consultas para...

1.  Encontrar o ID de Kevin Bacon (aquele que nasceu em 1958!)
2.  Encontrar os IDs dos filmes associados ao ID de Kevin Bacon
3.  Encontrar os IDs das pessoas associadas a esses IDs de filmes
4.  Encontrar os nomes das pessoas com esses IDs de pessoas

Então, tente aninhar essas consultas para chegar em uma única consulta que retorne os nomes de todas as pessoas que estrelaram um filme em que Kevin Bacon também estrelou. **Tenha em mente que você vai querer excluir o próprio Kevin Bacon dos resultados!**

## Passo a passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/v5_A3giDlQs?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Uso

Para testar suas consultas no VS Code, você pode consultar o banco de dados executando

    $ cat filename.sql | sqlite3 movies.db

onde `filename.sql` é o arquivo contendo sua consulta SQL.

Você também pode executar

    $ cat filename.sql | sqlite3 movies.db > output.txt

para redirecionar a saída da consulta para um arquivo de texto chamado `output.txt`. (Isso pode ser útil para verificar quantas linhas são retornadas pela sua consulta!)

## Como testar

Apesar de `check50` estar disponível para este problema, é recomendado que você teste seu código sozinho para cada um dos seguintes. Você pode executar `sqlite3 movies.db` para executar consultas adicionais no banco de dados para garantir que seu resultado esteja correto.

Se você estiver usando o banco de dados `movies.db` fornecido neste conjunto de problemas, você verá que

- Executar `1.sql` resulta em uma tabela com 1 coluna e 10.276 linhas.
- Executar `2.sql` resulta em uma tabela com 1 coluna e 1 linha.
- Executar `3.sql` resulta em uma tabela com 1 coluna e 110.014 linhas.
- Executar `4.sql` resulta em uma tabela com 1 coluna e 1 linha.
- Executar `5.sql` resulta em uma tabela com 2 colunas e 11 linhas.
- Executar `6.sql` resulta em uma tabela com 1 coluna e 1 linha.
- Executar `7.sql` resulta em uma tabela com 2 colunas e 7.192 linhas.
- Executar `8.sql` resulta em uma tabela com 1 coluna e 4 linhas.
- Executar `9.sql` resulta em uma tabela com 1 coluna e 19.325 linhas.
- Executar `10.sql` resulta em uma tabela com 1 coluna e 3.854 linhas.
- Executar `11.sql` resulta em uma tabela com 1 coluna e 5 linhas.
- Executar `12.sql` resulta em uma tabela com 1 coluna e 4 linhas.
- Executar `13.sql` resulta em uma tabela com 1 coluna e 182 linhas.

Observe que as contagens de linhas não incluem linhas de cabeçalho que mostram apenas nomes de colunas.

Se sua consulta retornar um número de linhas ligeiramente diferente da saída esperada, certifique-se de que você está tratando as duplicatas corretamente! Para consultas que pedem uma lista de nomes, nenhuma pessoa deve ser listada duas vezes, mas duas pessoas diferentes com o mesmo nome devem ser listadas.

### Correção

    check50 cs50/problems/2024/x/movies

## Como enviar

    submit50 cs50/problems/2024/x/movies

## Agradecimentos

Informações cedidas por cortesia da IMDb ([imdb.com](https://www.imdb.com)). Usada com permissão.

