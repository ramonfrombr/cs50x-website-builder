## Canções

![Logotipo do Spotify Wrapped '22](https://cs50.harvard.edu/x/2024/psets/7/songs/wrapped.png)

## Problema a resolver

Escreva consultas SQL para responder a perguntas sobre um banco de dados das 100 músicas mais transmitidas no [Spotify](https://en.wikipedia.org/wiki/Spotify) em 2018.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-DsiNSGFrMq2J6t9aDYhIQUQHy" src="https://asciinema.org/a/DsiNSGFrMq2J6t9aDYhIQUQHy.js"></script>

## Introdução

Para este problema, você usará um banco de dados fornecido pela equipe do CS50.

Abra o [VS Code](https://cs50.dev/).

Comece clicando dentro da janela do terminal e execute `cd` sozinho. Você verá que o "prompt" é semelhante ao abaixo.

    $

Clique dentro da janela do terminal e execute

    wget https://cdn.cs50.net/2023/fall/psets/7/songs.zip

seguido por Enter para baixar um ZIP chamado `songs.zip` no seu codespace. Tome cuidado para não ignorar o espaço entre `wget` e a URL a seguir, ou qualquer outro caractere!

Agora execute

    unzip songs.zip

para criar uma pasta chamada `songs`. Você não precisa mais do arquivo ZIP, então pode executar

    rm songs.zip

e responder com "y" seguido por Enter no prompt para remover o arquivo ZIP baixado.

Agora digite

    cd songs

seguido por Enter para se mover (ou seja, abrir) para esse diretório. Seu prompt agora deve ser semelhante ao abaixo.

    songs/ $

Se tudo foi bem-sucedido, você deve executar

    ls

e verá 8 arquivos .sql, `songs.db` e `answers.txt`.

Se você tiver algum problema, siga os mesmos passos novamente e veja se consegue determinar onde errou!

## Compreensão

Há um arquivo chamado `songs.db`, um banco de dados SQLite que armazena dados do [Spotify](https://developer.spotify.com/documentation/web-api/) sobre músicas e seus artistas. Este conjunto de dados contém as 100 músicas mais transmitidas no Spotify em 2018. Em uma janela de terminal, execute `sqlite3 songs.db` para começar a executar consultas no banco de dados.

Primeiro, quando o `sqlite3` solicitar que você forneça uma consulta, digite `.schema` e pressione Enter. Isso exibirá as instruções `CREATE TABLE` usadas para gerar cada uma das tabelas no banco de dados. Ao examinar essas instruções, você pode identificar as colunas presentes em cada tabela.

Observe que cada `artist` tem um `id` e um `name`. Observe também que cada música tem um `name`, um `artist_id` (correspondente ao `id` do artista da música), bem como valores para a capacidade de dança, energia, tecla, volume, fala (presença de palavras faladas em uma faixa), valência, andamento e duração da música (medida em milissegundos).

O desafio à sua frente é escrever consultas SQL para responder a uma variedade de perguntas diferentes selecionando dados de uma ou mais dessas tabelas. Depois de fazer isso, você refletirá sobre as maneiras pelas quais o Spotify pode usar esses mesmos dados em sua campanha anual [Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) para caracterizar os hábitos dos ouvintes.

## Detalhes de implementação

Para cada um dos problemas a seguir, você deve escrever uma única consulta SQL que gere os resultados especificados por cada problema. Sua resposta deve assumir a forma de uma única consulta SQL, embora você possa aninhar outras consultas dentro dela. Você **não deve** presumir nada sobre os `id`s de nenhuma música ou artista em particular: suas consultas devem ser precisas, mesmo que o `id` de alguma música ou pessoa em particular seja diferente. Finalmente, cada consulta deve retornar apenas os dados necessários para responder à pergunta: se o problema apenas solicitar que você exiba os nomes das músicas, por exemplo, sua consulta não deve exibir também o andamento de cada música.

1.  No `1.sql`, escreva uma consulta SQL para listar os nomes de todas as músicas no banco de dados.
    - Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada música.
2.  No `2.sql`, escreva uma consulta SQL para listar os nomes de todas as músicas em ordem crescente de andamento.
    - Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada música.
3.  No `3.sql`, escreva uma consulta SQL para listar os nomes das 5 músicas mais longas, em ordem decrescente de duração.
    - Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada música.
4.  No `4.sql`, escreva uma consulta SQL que liste os nomes de todas as músicas com capacidade de dança, energia e valência superiores a 0,75.
    - Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada música.
5.  No `5.sql`, escreva uma consulta SQL que retorne a energia média de todas as músicas.
    - Sua consulta deve gerar uma tabela com uma única coluna e uma única linha contendo a energia média.
6.  No `6.sql`, escreva uma consulta SQL que liste os nomes das músicas que são de Post Malone.
    - Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada música.
    - Você não deve fazer suposições sobre o `artist_id` de Post Malone.
7.  No `7.sql`, escreva uma consulta SQL que retorne a energia média das músicas de Drake.
    - Sua consulta deve gerar uma tabela com uma única coluna e uma única linha contendo a energia média.
    - Você não deve fazer suposições sobre o `artist_id` de Drake.
8.  No `8.sql`, escreva uma consulta SQL que liste os nomes das músicas que apresentam outros artistas.
    - Músicas que apresentam outros artistas incluirão "feat." no nome da música.
    - Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada música.

## Dicas

Veja [esta referência de palavras-chave SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para algumas sintaxes SQL que podem ser úteis!

Clique nos botões abaixo para ler alguns conselhos!

### Liste os nomes de todas as músicas no banco de dados

Lembre-se de que, para selecionar todos os valores na coluna de uma tabela, você pode usar a palavra-chave `SELECT` do SQL. `SELECT` é seguido pela coluna (ou colunas) que você deseja selecionar, que por sua vez é seguida por `FROM table` onde `table` é o nome da tabela da qual você deseja selecionar.

No `1.sql`, então, tente escrever o seguinte:

    -- Todas as músicas no banco de dados.
    SELECT name
    FROM songs;

### Liste os nomes de todas as músicas em ordem crescente de andamento

Lembre-se de que o SQL tem uma palavra-chave `ORDER BY`, pela qual você pode ordenar os resultados de sua consulta pelo valor em uma determinada coluna. Por exemplo, `ORDER BY tempo` ordenará os resultados pela coluna `tempo`.

No `2.sql`, então, tente escrever o seguinte:

    -- Todas as músicas em ordem crescente de andamento.
    SELECT name
    FROM songs
    ORDER BY tempo;

### Liste os nomes das 5 músicas mais longas, em ordem decrescente de duração

Lembre-se de que `ORDER BY` nem sempre precisa classificar em ordem crescente. Você pode especificar que seus resultados sejam classificados em ordem _decrescente_ anexando `DESC`. Por exemplo, `ORDER BY duration_ms DESC` listará os resultados em ordem decrescente, por duração.

E lembre-se também que `LIMIT n` pode especificar que você deseja apenas as primeiras \\(n\\) linhas que correspondem a uma consulta específica. Por exemplo, `LIMIT 5` retornará apenas os cinco primeiros resultados da consulta.

No `3.sql`, então, tente escrever o seguinte:

    -- Os nomes das 5 músicas mais longas, em ordem decrescente de duração.
    SELECT name
    FROM songs
    ORDER BY duration_ms DESC
    LIMIT 5;

### Liste os nomes de todas as músicas que têm uma capacidade de dança, energia e valência maiores que 0,75

Lembre-se de que você pode filtrar resultados em SQL com cláusulas `WHERE`, que são seguidas por alguma condição que normalmente testa os valores nas colunas de uma linha.

Lembre-se também de que os operadores da SQL funcionam da mesma forma que os da C. Por exemplo, `>` avalia como "verdadeiro" quando o valor à esquerda é maior que o valor à direita. Você pode encadear essas expressões junto, usando `AND` ou `OR`, para formar uma condição maior.

No `4.sql`, então, tente escrever o seguinte:

    -- Os nomes de todas as músicas que têm capacidade de dança, energia e valência maiores que 0,75.
    SELECT nome
    FROM musicas
    WHERE capacidade_danca > 0,75 AND energia > 0,75 AND valência > 0,75;

### Encontre a energia média de todas as músicas

Lembre-se de que o SQL suporta palavras-chaves não apenas para selecionar linhas específicas, mas também para _agregar_ os dados nessas linhas. Em particular, você pode achar a palavra-chave `AVG` (para calcular médias) útil. Para agregar os resultados de uma coluna, basta aplicar a função de agregação a essa coluna. Por exemplo, `SELECT AVG(energia)` encontrará a média dos valores na coluna de energia para a consulta fornecida.

No `5.sql`, então, tente escrever o seguinte:

    -- A energia média de todas as músicas.
    SELECT AVG(energia)
    FROM musicas;

### Liste os nomes das músicas que são do Post Malone

Observe que, se você executar `.schema musicas` no seu prompt do sqlite, a tabela `musicas` tem nomes de músicas, mas não o nome do artista! Em vez disso, `musicas` tem uma coluna `id_artista`. Para listar os nomes de músicas do Post Malone, você primeiro precisa identificar o id do artista do Post Malone.

    -- Identifique o id do artista do Post Malone
    SELECT id
    FROM artistas
    WHERE nome = 'Post Malone';

Esta consulta retorna 54. Agora, você pode consultar a tabela `musicas` para qualquer música com o id do Post Malone.

    SELECT nome
    FROM musicas
    WHERE id_artista = 54;

Mas, de acordo com a especificação, você deve estar atento para não assumir conhecimento de nenhum id. Você pode melhorar o design desta consulta _aninhado_ duas consultas.

No `6.sql`, então, tente escrever o seguinte:

    -- Os nomes das músicas que são do Post Malone.
    SELECT nome
    FROM musicas
    WHERE id_artista =
    (
        SELECT id
        FROM artistas
        WHERE nome = 'Post Malone'
    );

### Encontre a energia média das músicas que são do Drake

Observe que, semelhante à consulta anterior, você precisará combinar várias tabelas para executar esta consulta com êxito. Você pode usar novamente subconsultas aninhadas, mas considere também outra abordagem!

Lembre-se de que você pode usar a palavra-chave `JOIN` da SQL para combinar várias tabelas em uma, desde que você especifique quais colunas entre essas tabelas devem corresponder em última análise. Por exemplo, a consulta a seguir une as tabelas `musicas` e `artistas`, indicando que a coluna `id_artista` na tabela `musicas` e a coluna `id` na tabela `artistas` devem corresponder:

    SELECT *
    FROM musicas
    JOIN artistas ON musicas.id_artista = artistas.id

Com essas duas tabelas combinadas, é apenas uma questão de filtrar sua seleção para encontrar a energia média das músicas do Drake.

No `7.sql`, então, tente escrever o seguinte:

    -- A energia média das músicas que são do Drake
    SELECT AVG(energia)
    FROM musicas
    JOIN artistas ON musicas.id_artista = artistas.id
    WHERE artistas.nome = 'Drake';

### Liste os nomes das músicas que apresentam outros artistas

Para esta consulta, observe que músicas que apresentam outros artistas normalmente têm alguma menção de “feat.” no título. Lembre-se de que a palavra-chave `LIKE` da SQL pode ser usada para corresponder strings com certas frases (como “feat.”!). Para fazer isso, você pode usar `%`: um caractere curinga que corresponde a qualquer sequência de caracteres.

No `8.sql`, então, tente escrever o seguinte:

    -- Os nomes das músicas que apresentam outros artistas.
    SELECT nome
    FROM musicas
    WHERE nome LIKE '%feat.%';

## Passo a passo

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/wgKPUd_95AA"></iframe>

<details><summary>Não sabe como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/7hydPL9ZswE"></iframe></details>

## Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) é um recurso que apresenta aos usuários do Spotify suas 100 músicas mais tocadas no ano passado. Em 2021, o Spotify Wrapped calculou uma [“Aura Áudio”](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) para cada usuário, uma “leitura de \[seus\] dois humores mais proeminentes ditados por \[suas\] principais músicas e artistas do ano.” Suponha que o Spotify determine uma aura de áudio observando a energia média, a valência e a capacidade de dança das 100 melhores músicas de uma pessoa no ano passado. No `answers.txt`, reflita sobre as seguintes questões:

- Se `musicas.db` contém as 100 melhores músicas de um ouvinte de 2018, como você caracterizaria sua aura de áudio?
- Suponha sobre por que o jeito que você calculou essa aura pode _não_ ser muito representativo do ouvinte. Que outras formas de calcular essa aura você propõe?

Certifique-se de enviar `answers.txt` junto com cada um dos seus arquivos `.sql`!

## Como testar

### Correção

    check50 cs50/problems/2024/x/musicas

## Como enviar

    submit50 cs50/problems/2024/x/musicas

## Reconhecimentos

Conjunto de dados do [Kaggle](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018).

