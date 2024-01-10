## Detalhes de Implementação

Complete a implementação de uma aplicação web que permita aos usuários armazenar e acompanhar aniversários.

- Quando a rota `/` é solicitada com um método `GET`, sua aplicação web deve exibir, em uma tabela, todas as pessoas do seu banco de dados juntamente com suas datas de aniversário.
  - Primeiro, em `app.py`, adicione lógica no tratamento da requisição `GET` para consultar o banco de dados `birthdays.db` por todos os aniversários. Passe todos esses dados para o template `index.html`.
  - Em seguida, em `index.html`, adicione lógica para renderizar cada aniversário como uma linha na tabela. Cada linha deve ter duas colunas: uma coluna para o nome da pessoa e outra coluna para a data de aniversário da pessoa.
- Quando a rota `/` é solicitada com um método `POST`, sua aplicação web deve adicionar um novo aniversário ao banco de dados e em seguida renderizar a página de índice novamente.
  - Primeiro, em `index.html`, adicione um formulário HTML. O formulário deve permitir que os usuários digitem um nome, um mês de aniversário e um dia de aniversário. Certifique-se de que o formulário seja enviado para `/` (sua "ação") com um método `post`.
  - Em seguida, em `app.py`, adicione lógica no tratamento da requisição `POST` para `INSERT` uma nova linha na tabela `birthdays` com base nos dados fornecidos pelo usuário.

Opcionalmente, você também pode:

- Adicionar a capacidade de excluir e/ou editar entradas de aniversário.
- Adicionar quaisquer recursos adicionais de sua escolha!

### Passo a Passo

<div class="alert" data-alert="primary" role="alert"><p>Este vídeo foi gravado quando o curso ainda estava usando o CS50 IDE para escrever código. Embora a interface possa parecer diferente do seu ambiente de codificação, o comportamento dos dois ambientes deve ser semelhante!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/HXwvj8x1Fcs"></iframe>


### Dicas

- Lembre-se de que você pode chamar `db.execute` para executar consultas SQL dentro de `app.py`.
  - Se você chamar `db.execute` para executar uma consulta `SELECT`, lembre-se de que a função retornará para você uma lista de dicionários, onde cada dicionário representa uma linha retornada pela consulta.
- Provavelmente será útil passar dados adicionais para `render_template()` em sua função `index` para que seja possível acessar os dados de aniversário dentro do seu template `index.html`.
- Lembre-se de que a tag `tr` pode ser usada para criar uma linha de tabela e a tag `td` pode ser usada para criar uma célula de dados de tabela.
- Lembre-se de que, com o Jinja, é possível criar um [`loop for`](https://jinja.palletsprojects.com/en/2.11.x/templates/#for) dentro do arquivo `index.html`.
- Em `app.py`, é possível obter os dados enviados pelo formulário do usuário através de `request.form.get(campo)`, em que `campo` é uma string que representa o atributo `name` de um `input` de seu formulário.
  - Por exemplo, se em `index.html`, você tiver um `<input name="foo" type="text">`, você pode usar `request.form.get("foo")` em `app.py` para extrair a entrada do usuário.

<details><summary>Não sabe como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/lVwv4o8vmvI"></iframe></details>


### Testando

Não há `check50` para este laboratório! Mas certifique-se de testar sua aplicação web adicionando alguns aniversários e garantindo que os dados aparecem na tabela como esperado.

Execute o comando `flask run` no terminal enquanto estiver no diretório `birthdays` para iniciar um servidor web que registra sua aplicação Flask.

## Como Enviar

No terminal, execute o seguinte comando para enviar seu trabalho.

    submit50 cs50/labs/2023/x/birthdays