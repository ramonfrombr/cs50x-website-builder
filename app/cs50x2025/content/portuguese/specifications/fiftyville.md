## Fiftyville

## Problema a resolver

O Pato CS50 foi roubado! A cidade de Fiftyville te convocou para resolver o mistério do pato roubado. As autoridades acreditam que o ladrão roubou o pato e em seguida, logo depois, fugiu da cidade com a ajuda de um cúmplice. Seu objetivo é identificar:

- Quem é o ladrão,
- Para qual cidade o ladrão escapou, e
- Quem é o cúmplice do ladrão que o ajudou a escapar

Tudo o que você sabe é que o roubo **aconteceu em 28 de julho de 2023** e que **aconteceu na Humphrey Street**.

Como você irá resolver este mistério? As autoridades de Fiftyville coletaram alguns registros da cidade do período ao redor do roubo e prepararam um banco de dados SQLite para você, fiftyville.db, que contém tabelas de dados da cidade. Você pode consultar essa tabela usando consultas SQL SELECT para acessar os dados de seu interesse. Usando apenas as informações no banco de dados, sua tarefa é resolver o mistério.

## Demonstração

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-YgI5fyTP939jINCZm7l3o7WCY" src="https://asciinema.org/a/YgI5fyTP939jINCZm7l3o7WCY.js"></script>

## Começando

Para este problema, você usará um banco de dados fornecido pela equipe do CS50.

Faça login no [cs50.dev](https://cs50.dev/), clique na janela do seu terminal e execute `cd` por si só. Você deve descobrir que o prompt da janela do seu terminal se assemelha ao abaixo:

    $

Em seguida, execute

    wget https://cdn.cs50.net/2023/fall/psets/7/fiftyville.zip
    
para baixar um ZIP chamado fiftyville.zip no seu espaço de código.

Em seguida, execute

    unzip fiftyville.zip
    
para criar uma pasta chamada fiftyville. Você não precisa mais do arquivo ZIP, então você pode executar

    rm fiftyville.zip

e responder com "y" seguido de Enter no prompt para remover o arquivo ZIP que você baixou.

Agora digite

    cd fiftyville
    
seguido por Enter para se mover para (ou seja, abrir) esse diretório. O seu prompt agora deve se assemelhar ao abaixo.

    fiftyville/ $
    
Execute `ls` sozinho e você verá alguns arquivos:

    answers.txt  fiftyville.db  log.sql

Se você tiver algum problema, siga os mesmos passos novamente e veja se consegue determinar onde errou!

## Especificação

Para este problema, igualmente importante quanto resolver o mistério em si é o processo que você usa para resolver o mistério. No log.sql, mantenha um registro de todas as consultas SQL que você executar no banco de dados. Acima de cada consulta, rotule cada uma com um comentário (em SQL, comentários são todas as linhas que começam com `--`) descrevendo por que você está executando a consulta e/ou quais informações você espera obter dessa consulta em particular. Você pode usar comentários no arquivo de log para adicionar notas adicionais sobre seu processo de pensamento ao resolver o mistério: em última análise, este arquivo deve servir como uma evidência do processo que você usou para identificar o ladrão!

Ao escrever suas consultas, você pode perceber que algumas delas podem se tornar bastante complexas. Para ajudar a manter suas consultas legíveis, veja os princípios de bom estilo em [sqlstyle.guide](https://www.sqlstyle.guide). A seção [indentação](https://www.sqlstyle.guide/#indentation) pode ser particularmente útil!

Depois de resolver o mistério, complete cada uma das linhas no answers.txt preenchendo o nome do ladrão, a cidade para a qual o ladrão escapou e o nome do cúmplice do ladrão que o ajudou a escapar da cidade. (Certifique-se de não alterar nenhum dos textos existentes no arquivo ou adicionar quaisquer outras linhas ao arquivo!)

Em última análise, você deve enviar seus arquivos log.sql e answers.txt.

## Passo a passo

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/YHhgEoJMDnU?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Dicas

- Execute sqlite3 fiftyville.db para começar a executar consultas no banco de dados.
  - Ao executar sqlite3, executar .tables listará todas as tabelas no banco de dados.
  - Ao executar sqlite3, executar .schema NOME_DA_TABELA, onde NOME_DA_TABELA é o nome da tabela no banco de dados, irá mostrar o comando CREATE TABLE usado para criar a tabela. Isso pode ser útil para saber quais colunas consultar!
- Você pode achar útil começar com a tabela crime_scene_reports. Comece procurando um relatório de cena de crime que corresponda à data e ao local do crime.
- Veja [esta referência de palavras-chave SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) para obter alguma sintaxe SQL que pode ser útil!

## Como testar

### Correção

    check50 cs50/problems/2024/x/fiftyville

## Como enviar

    submit50 cs50/problems/2024/x/fiftyville

## Agradecimentos

Inspirado por outro caso em [SQL City](https://mystery.knightlab.com/).