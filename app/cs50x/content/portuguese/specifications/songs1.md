Lab 7: Músicas
============

<div class="alert" data-alert="warning" role="alert"><p>Você pode colaborar com um ou dois colegas neste laboratório, embora seja esperado que todos os estudantes de tal grupo contribuam igualmente para o laboratório.</p></div>

Escreva consultas SQL para responder a perguntas sobre um banco de dados de músicas.

Primeiros Passos
---------------

Abra o [VS Code](https://code.cs50.io/).

Comece clicando dentro da janela do terminal e execute `cd` sozinho. Você deverá encontrar um "prompt" como o abaixo.

    $
    

Clique dentro dessa janela do terminal e depois execute

    wget https://cdn.cs50.net/2022/fall/labs/7/songs.zip
    

seguido por Enter para baixar um arquivo ZIP chamado `songs.zip` em seu espaço de códigos. Tenha cuidado para não ignorar o espaço entre `wget` e a URL seguinte, ou qualquer outro caractere também!

Agora execute

    unzip songs.zip
    

para criar uma pasta chamada `songs`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm songs.zip
    

e responder com “y” seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd songs
    

seguido de Enter para se mover para dentro (ou seja, abrir) esse diretório. Seu prompt agora deve se assemelhar ao abaixo.

    songs/ $
    

Se tudo foi bem-sucedido, você deve executar

    ls
    

e você deve ver 8 arquivos .sql, `songs.db` e `answers.txt`.

Se você encontrar algum problema, siga essas mesmas etapas novamente e veja se consegue determinar onde você errou!

Compreensão
-------------

Fornecido a você está um arquivo chamado `songs.db`, um banco de dados SQLite que armazena dados do [Spotify](https://developer.spotify.com/documentation/web-api/) sobre músicas e seus artistas. Este conjunto de dados contém as 100 músicas mais ouvidas no Spotify em 2018. Em uma janela do terminal, execute `sqlite3 songs.db` para começar a executar consultas no banco de dados.

Primeiro, quando o `sqlite3` pedir para você fornecer uma consulta, digite `.schema` e pressione enter. Isso mostrará as instruções `CREATE TABLE` que foram usadas para gerar cada uma das tabelas no banco de dados. Ao examinar essas instruções, você pode identificar as colunas presentes em cada tabela.

Observe que cada `artista` possui um `id` e um `nome`. Observe também que cada música possui um `nome`, um `artist_id` (correspondente ao `id` do artista da música), bem como valores para a "danceability" (dançabilidade), energia, chave, volume, "speechiness" (presença de palavras faladas em uma faixa), valência, tempo e duração da música (medida em milissegundos).

O desafio à sua frente é escrever consultas SQL para responder a uma variedade de perguntas diferentes selecionando dados de uma ou mais dessas tabelas. Depois de fazer isso, você vai refletir sobre as formas como o Spotify pode usar esses mesmos dados em sua campanha anual do [Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) para caracterizar os hábitos dos ouvintes.