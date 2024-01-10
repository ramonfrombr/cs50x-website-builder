Uso
-----

Além de executar suas consultas no `sqlite3`, você pode testar suas consultas no terminal do VS Code executando

    $ cat filename.sql | sqlite3 songs.db
    

onde `filename.sql` é o arquivo que contém sua consulta SQL.

### Sugestões

*   Consulte [este guia de palavras-chave do SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para obter alguma sintaxe SQL que pode ser útil!


<details><summary>Não sabe como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/7hydPL9ZswE"></iframe></details>


### Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) é um recurso que apresenta as 100 músicas mais reproduzidas pelos usuários do Spotify no ano passado. Em 2021, o Spotify Wrapped calculou uma ["Audio Aura"](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) para cada usuário, uma "leitura das duas emoções mais proeminentes \[deles\] conforme ditado por \[suas\] principais músicas e artistas do ano". Suponha que o Spotify determine uma aura de áudio analisando a energia média, a valência e a dançabilidade das 100 principais músicas de uma pessoa no ano anterior. No arquivo `answers.txt`, reflita sobre as seguintes perguntas:

*   Se `songs.db` contém as 100 principais músicas de um ouvinte em 2018, como você caracterizaria sua aura de áudio?
*   Faça uma hipótese sobre o motivo pelo qual a forma como você calculou essa aura pode _não_ ser muito representativa do ouvinte. Que maneiras melhores de calcular essa aura você proporia?

Certifique-se de enviar o arquivo `answers.txt` juntamente com cada um dos seus arquivos `.sql`!

### Teste

Execute o seguinte para avaliar a correção do seu código usando o `check50`.

    check50 cs50/labs/2023/x/songs
    

Como Enviar
-------------

No seu terminal, execute o seguinte para enviar seu trabalho.

    submit50 cs50/labs/2023/x/songs
    

Agradecimentos
----------------

Conjunto de dados de [Kaggle](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018).