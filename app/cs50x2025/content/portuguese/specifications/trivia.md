# Trivia

Escreva uma página da web que permita que os usuários respondam a perguntas triviais.

![Captura de tela de perguntas triviais](https://cs50.harvard.edu/x/2024/psets/8/trivia/questions.png)

## Introdução

Abra o [VS Code](https://cs50.dev/).

Comece clicando dentro da janela do terminal e, em seguida, execute `cd` sozinho. Você deve descobrir que seu "prompt" se assemelha ao exemplo abaixo.

    $

Clique dentro da janela do terminal e, em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/8/trivia.zip

seguido por Enter para baixar um ZIP chamado `trivia.zip` no seu espaço de codificação. Tome cuidado para não ignorar o espaço entre `wget` e a URL a seguir ou qualquer outro caractere!

Agora execute

    unzip trivia.zip

para criar uma pasta chamada `trivia`. Você não precisa mais do arquivo ZIP, então você pode executar

    rm trivia.zip

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP baixado.

Agora digite

    cd trivia

seguido por Enter para se mover (ou seja, abrir) o diretório. Seu prompt agora deve se parecer com o exemplo abaixo.

    trivia/ $

Se tudo foi bem-sucedido, você deve executar

    ls

e você deverá ver um arquivo `index.html` e um arquivo `styles.css`.

Se você tiver algum problema, siga essas mesmas etapas novamente e veja se consegue determinar onde errou!

## Detalhes de implementação

Crie uma página da web usando HTML, CSS e JavaScript para permitir que os usuários respondam a perguntas triviais.

- Em `index.html`, adicione abaixo de "Parte 1" uma pergunta trivial de múltipla escolha de sua escolha com HTML.
  - Você deve usar um cabeçalho `h3` para o texto da sua pergunta.
  - Você deve ter um `button` para cada uma das opções de resposta possíveis. Deve haver pelo menos três opções de resposta, das quais exatamente uma deve estar correta.
- Usando JavaScript, adicione lógica para que os botões mudem de cor quando um usuário clicar neles.
  - Se um usuário clicar em um botão com uma resposta incorreta, o botão deve ficar vermelho e um texto deve aparecer abaixo da pergunta dizendo "Incorreto".
  - Se um usuário clicar em um botão com a resposta correta, o botão deve ficar verde e um texto deve aparecer abaixo da pergunta dizendo "Correto!".
- Em `index.html`, adicione abaixo de "Parte 2" uma pergunta de resposta livre baseada em texto de sua escolha com HTML.
  - Você deve usar um cabeçalho `h3` para o texto da sua pergunta.
  - Você deve usar um campo `input` para permitir que o usuário digite uma resposta.
  - Você deve usar um `button` para permitir que o usuário confirme sua resposta.
- Usando JavaScript, adicione lógica para que o campo de texto mude de cor quando um usuário confirmar sua resposta.
  - Se o usuário digitar uma resposta incorreta e pressionar o botão de confirmação, o campo de texto deve ficar vermelho e um texto deve aparecer abaixo da pergunta dizendo "Incorreto".
  - Se o usuário digitar a resposta correta e pressionar o botão de confirmação, o campo de entrada deve ficar verde e um texto deve aparecer abaixo da pergunta dizendo "Correto!".

Opcionalmente, você também pode:

- Editar `styles.css` para alterar o CSS da sua página da web!
- Adicione perguntas triviais adicionais ao seu teste se desejar!

### Passo a passo

<div class="alert alert-primary" data-alert="primary" role="alert"><p>Este vídeo foi gravado quando o curso ainda usava o CS50 IDE para escrever código. Embora a interface possa parecer diferente do seu espaço de codificação, o comportamento dos dois ambientes deve ser bastante semelhante!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/WGd0Jx7rxUo"></iframe>

### Dicas

- Use [`document.querySelector`](https://developer.mozilla.org/pt-BR/docs/Web/API/Document/querySelector) para consultar um único elemento HTML.
- Use [`document.querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) para consultar vários elementos HTML que correspondem a uma consulta. A função retorna uma matriz de todos os elementos correspondentes.

<details><summary>Não tem certeza de como resolver?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/FLlI7rSSV_M"></iframe></details>

### Teste

Sem `check50` para este, pois as implementações variam com base nas suas perguntas! Mas certifique-se de testar respostas incorretas e corretas para cada uma de suas perguntas para garantir que sua página da web responda adequadamente.

Execute `http-server` em seu terminal enquanto estiver em seu diretório `trivia` para iniciar um servidor da web que atende sua página da web.

## Como enviar

    submit50 cs50/problems/2024/x/trivia

**Criando ouvintes de evento com JavaScript**

    <!DOCTYPE html>

    <html lang="en">
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
            <link href="styles.css" rel="stylesheet">
            <title>Trivia!</title>
            <script>

                // Aguarde o carregamento do conteúdo do DOM
                document.addEventListener('DOMContentLoaded', function() {

                    // Obter todos os elementos com classe "correto"
                    let corrects = document.querySelectorAll('.correct');

                    // Adicionar ouvintes de evento a cada botão correto
                    for (let i = 0; i < corrects.length; i++) {
                        corrects[i].addEventListener('click', function() {

                            // Definir cor de fundo como verde
                            corrects[i].style.backgroundColor = 'Green';

                            // Vá para o elemento pai do botão correto e encontre o primeiro elemento com classe "feedback" que tenha esse pai
                            corrects[i].parentElement.querySelector('.feedback').innerHTML = 'Correto!';
                        });
                    }

                    // Quando qualquer resposta incorreta for clicada, altere a cor para vermelho.
                    let incorrects = document.querySelectorAll(".incorrect");
                    for (let i = 0; i < incorrects.length; i++) {
                        incorrects[i].addEventListener('click', function() {

                            // Definir cor de fundo como vermelho
                            incorrects[i].style.backgroundColor = 'Red';

                            // Vá para o elemento pai do botão correto e encontre o primeiro elemento com classe "feedback" que tenha esse pai
                            incorrects[i].parentElement.querySelector('.feedback').innerHTML = 'Incorreto';
                        });
                    }

                    // Verificar envio de resposta livre
                    document.querySelector('#check').addEventListener('click', function() {
                        let input = document.querySelector('input');
                        if (input.value === 'Suiça') {
                            input.style.backgroundColor = 'green';
                            input.parentElement.querySelector('.feedback').innerHTML = 'Correto!';
                        }
                        else {
                            input.style.backgroundColor = 'red';
                            input.parentElement.querySelector('.feedback').innerHTML = 'Incorreto';
                        }
                    });
                });
            </script>
        </head>
        <body>
            <div class="header">
                <h1>Trivia!</h1>
            </div>

            <div class="container">
                <div class="section">
                    <h2>Parte 1: Escolha múltipla </h2>
                    <hr>
                    <h3>Qual é a proporção aproximada de pessoas por ovelha na Nova Zelândia?</h3>
                    <button class="incorrect">6 pessoas por 1 ovelha</button>
                    <button class="incorrect">3 pessoas por 1 ovelha</button>
                    <button class="incorrect">1 pessoa por 1 ovelha</button>
                    <button class="incorrect">1 pessoa por 3 ovelhas</button>
                    <button class="correct">1 pessoa por 6 ovelhas</button>
                    <p class="feedback"></p>
                </div>

                <div class="section">
                    <h2>Parte 2: Resposta livre</h2>
                    <hr>
                    <h3>Em que país é ilegal ter apenas uma cobaia, pois uma cobaia solitária pode ficar sozinha?</h3>
                    <input type="text"></input>
                    <button id="check">Verificar Resposta</button>
                    <p class="feedback"></p>
                </div>
            </div>
        </body>
    </html>

**Criando ouvintes de evento com HTML**

    <!DOCTYPE html>

    <html lang="en">
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
            <link href="styles.css" rel="stylesheet">
            <title>Trivia!</title>
            <script>
                function checkMultiChoice(event) {

                    // Obter o elemento que acionou o evento
                    let button = event.target;

                    // Verificar se o HTML interno do elemento corresponde à resposta esperada
                    if (button.innerHTML == '1 pessoa por 6 ovelhas') {
                        button.style.backgroundColor = 'Green';
                        button.parentElement.querySelector('.feedback').innerHTML = 'Correto!';
                    }
                    else {
                        button.style.backgroundColor = 'Red';
                        button.parentElement.querySelector('.feedback').innerHTML = 'Incorreto';
                    }
                }

                function checkFreeResponse(event) {

                    // Obter o elemento que acionou o evento
                    let button = event.target;

                    // Obter o elemento de entrada correspondente ao botão
                    let input = button.parentElement.querySelector('input');

                    // Verificar a resposta correta
                    if (input.value === 'Suíça') {
                        input.style.backgroundColor = 'Green';
                        input.parentElement.querySelector('.feedback').innerHTML = 'Correto!';
                    }
                    else {
                        input.style.backgroundColor = 'Red';
                        input.parentElement.querySelector('.feedback').innerHTML = 'Incorreto';
                    }
                }
            </script>
        </head>
        <body>
            <div class="header">
                <h1>Trivia!</h1>
            </div>

            <div class="container">
                <div class="section">
                    <h2>Parte 1: Escolha múltipla </h2>
                    <hr>
                    <h3>Qual é a proporção aproximada de pessoas por ovelha na Nova Zelândia?</h3>
                    <button onclick="checkMultiChoice(event)">6 pessoas por 1 ovelha</button>
                    <button onclick="checkMultiChoice(event)">3 pessoas por 1 ovelha</button>
                    <button onclick="checkMultiChoice(event)">1 pessoa por 1 ovelha</button>
                    <button onclick="checkMultiChoice(event)">1 pessoa por 3 ovelhas</button>
                    <button onclick="checkMultiChoice(event)">1 pessoa por 6 ovelhas</button>
                    <p class="feedback"></p>
                </div>

                <div class="section">
                    <h2>Parte 2: Resposta livre</h2>
                    <hr>
                    <h3>Em que país é ilegal ter apenas uma cobaia, pois uma cobaia solitária pode ficar sozinha?</h3>
                    <input type="text"></input>
                    <button onclick="checkFreeResponse(event)">Verificar Resposta</button>
                    <p class="feedback"></p>
                </div>
            </div>
        </body>
    </html>

