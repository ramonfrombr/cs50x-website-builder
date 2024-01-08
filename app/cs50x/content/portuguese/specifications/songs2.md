Detalhes de Implementação
---------------------------

Para cada um dos problemas a seguir, você deve escrever uma única consulta SQL que retorne os resultados especificados por cada problema. Sua resposta deve ser na forma de uma única consulta SQL, embora você possa aninhar outras consultas dentro da sua consulta. Você **não deve** assumir nada sobre os `id`s de músicas ou artistas específicos: suas consultas devem ser precisas mesmo se o `id` de qualquer música ou pessoa for diferente. Por fim, cada consulta deve retornar apenas os dados necessários para responder à pergunta: se o problema só pede para listar os nomes das músicas, por exemplo, então sua consulta não deve incluir também o tempo de cada música.

1.  Em `1.sql`, escreva uma consulta SQL para listar os nomes de todas as músicas no banco de dados.
    *   Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada música.
2.  Em `2.sql`, escreva uma consulta SQL para listar os nomes de todas as músicas em ordem crescente de tempo.
    *   Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada música.
3.  Em `3.sql`, escreva uma consulta SQL para listar os nomes das 5 músicas mais longas, em ordem decrescente de duração.
    *   Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada música.
4.  Em `4.sql`, escreva uma consulta SQL que liste os nomes de quaisquer músicas que tenham dançabilidade, energia e valência maiores que 0,75.
    *   Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada música.
5.  Em `5.sql`, escreva uma consulta SQL que retorne a energia média de todas as músicas.
    *   Sua consulta deve retornar uma tabela com uma única coluna e uma única linha contendo a energia média.
6.  Em `6.sql`, escreva uma consulta SQL que liste os nomes das músicas que são de autoria de Post Malone.
    *   Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada música.
    *   Você não deve fazer suposições sobre qual é o `artist_id` de Post Malone.
7.  Em `7.sql`, escreva uma consulta SQL que retorne a energia média das músicas que são de autoria de Drake.
    *   Sua consulta deve retornar uma tabela com uma única coluna e uma única linha contendo a energia média.
    *   Você não deve fazer suposições sobre qual é o `artist_id` de Drake.
8.  Em `8.sql`, escreva uma consulta SQL que liste os nomes das músicas que apresentam outros artistas.
    *   Músicas que apresentam outros artistas incluirão "feat." no nome da música.
    *   Sua consulta deve retornar uma tabela com uma única coluna para o nome de cada música.

### Passo a passo

<div class="alert" data-alert="primary" role="alert"><p>Este vídeo foi gravado quando o curso ainda estava usando o CS50 IDE para escrever código. Embora a interface possa parecer diferente do seu ambiente de codificação, o comportamento dos dois ambientes deve ser bastante similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/wgKPUd_95AA"></iframe>