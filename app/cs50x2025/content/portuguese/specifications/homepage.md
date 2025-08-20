# Homepage

Crie uma página inicial simples usando HTML, CSS e JavaScript.

## Introdução

A internet possibilitou coisas incríveis: podemos usar um mecanismo de pesquisa para pesquisar qualquer coisa imaginável, nos comunicar com amigos e familiares ao redor do mundo, jogar, fazer cursos e muito mais. Mas acontece que quase todas as páginas que podemos visitar são construídas em três linguagens essenciais, cada uma das quais serve a um propósito ligeiramente diferente:

1.  HTML ou _HyperText Markup Language_, que é usada para descrever o conteúdo dos sites;
2.  CSS, _Cascading Style Sheets_, que é usada para descrever a estética dos sites; e
3.  JavaScript, que é usado para tornar os sites interativos e dinâmicos.

Crie uma página inicial simples que apresente você, seu hobby favorito ou atividade extracurricular ou qualquer outra coisa que seja do seu interesse.

## Começando

Faça login em [cs50.dev](https://cs50.dev/), clique na janela do terminal e execute apenas `cd`. Você deve descobrir que o prompt da janela do terminal se assemelha ao seguinte:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/8/homepage.zip

para baixar um ZIP chamado `homepage.zip` em seu codespace.

Em seguida, execute

    unzip homepage.zip

para criar uma pasta chamada `homepage`. Você não precisa mais do arquivo ZIP, então pode executar

    rm homepage.zip

e responda com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd homepage

seguido de Enter para entrar (ou seja, abrir) o diretório. Seu prompt agora deve se parecer com o abaixo.

    homepage/ $

Execute `ls` sozinho e você verá alguns arquivos:

    index.html  styles.css

Se você tiver algum problema, siga os mesmos passos novamente e veja se consegue determinar onde errou! Você pode iniciar imediatamente um servidor para visualizar seu site executando

    http-server

na janela do terminal. Em seguida, clique no comando (se estiver no Mac) ou clique com o botão direito (se estiver no PC) no primeiro link que aparecer:

    http-server running on LINK

Onde LINK é o endereço do seu servidor.

## Especificação

Implemente em seu diretório `homepage` um site que deve:

- Conter pelo menos quatro páginas `.html` diferentes, sendo que pelo menos uma delas é `index.html` (a página principal do seu site), e deve ser possível acessar qualquer página do seu site de qualquer outra página seguindo um ou mais hiperlinks.
- Usar pelo menos dez (10) tags HTML distintas além de `<html>`, `<head>`, `<body>` e `<title>`. Usar alguma tag (por exemplo, `<p>`) várias vezes ainda conta como apenas uma (1) dessas dez!
- Integrar um ou mais recursos do Bootstrap em seu site. O Bootstrap é uma biblioteca popular (que vem com muitas classes CSS e muito mais) por meio da qual você pode embelezar seu site. Consulte a [documentação do Bootstrap](https://getbootstrap.com/docs/5.2/) para começar. Em particular, você pode achar alguns dos [componentes do Bootstrap](https://getbootstrap.com/docs/5.2/components/) interessantes. Para adicionar o Bootstrap ao seu site, basta incluir
    
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
    
    no `<head>` das suas páginas, abaixo do qual você também pode incluir
    
        <link href="styles.css" rel="stylesheet">
    
    para vincular seu próprio CSS.
- Ter pelo menos um arquivo de folha de estilo de sua própria criação, `styles.css`, que use pelo menos cinco (5) seletores CSS diferentes (por exemplo, tag (`example`), classe (`.example`) ou ID (`#example`)) e dentro do qual você use um total de pelo menos cinco (5) propriedades CSS diferentes, como `font-size` ou `margin`; e
- Integrar um ou mais recursos do JavaScript em seu site para tornar seu site mais interativo. Por exemplo, você pode usar JavaScript para adicionar alertas, para ter um efeito em um intervalo recorrente ou para adicionar interatividade a botões, menus suspensos ou formulários. Sinta-se à vontade para ser criativo!
- Certifique-se de que seu site tenha uma boa aparência em navegadores em dispositivos móveis, bem como em laptops e desktops.

Você também deve criar um arquivo de texto, `specification.txt`, que liste as 10 tags HTML e 5 propriedades CSS que você usou, bem como uma breve descrição (de uma frase) de como você escolheu usar JavaScript e Bootstrap.

## Testando

Se quiser ver a aparência do seu site enquanto trabalha nele, você pode executar `http-server`. Clique com o botão direito do mouse ou o botão direito do mouse no primeiro link apresentado pelo http-server, que deve abrir sua página da web em uma nova guia. Você poderá então atualizar a guia que contém sua página da web para ver suas últimas alterações.

Lembre-se também que, abrindo o Developer Tools no Google Chrome, você pode _simular_ a visita à sua página em um dispositivo móvel clicando no ícone em forma de telefone à esquerda de **Elements** na janela do Developer Tools ou, depois de abrir o Developer Tools guia já foi aberta, digitando `Ctrl`+`Shift`+`M` em um PC ou `Cmd`+`Shift`+`M` em um Mac, em vez de precisar visitar seu site separadamente em um dispositivo móvel!

## Avaliação

Sem `check50` para esta tarefa! Em vez disso, a exatidão do seu site será avaliada com base se você atende aos requisitos da especificação conforme descrito acima e se o seu HTML está bem formado e válido. Para garantir que suas páginas estejam, você pode usar este [serviço de validação de marcação](https://validator.w3.org/#validate_by_input), copiando e colando seu HTML diretamente na caixa de texto fornecida. Tome cuidado para eliminar quaisquer avisos ou erros sugeridos pelo validador antes de enviar!

Considere também:

- se a estética do seu site é tal que é intuitiva e direta para um usuário navegar;
- se o seu CSS foi fatorado em um ou mais arquivos CSS separados; e
- se você evitou repetição e redundância ao "cascatear" as propriedades de estilo das tags pai.

O `style50` não suporta arquivos HTML, portanto, é sua responsabilidade indenizar e alinhar as tags HTML de forma organizada. Saiba também que você pode criar um comentário HTML com:

    <!-- Comment goes here -->

mas comentar seu código HTML não é tão imperativo quanto comentar código em, digamos, C ou Python. Você também pode comentar seu CSS, em arquivos CSS, com:

    /* Comment goes here */

## Dicas

Para guias bastante abrangentes sobre as linguagens apresentadas neste problema, confira estes tutoriais:

- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/)
- [JavaScript](https://www.w3schools.com/js/)

## Como Enviar

    submit50 cs50/problems/2024/x/homepage