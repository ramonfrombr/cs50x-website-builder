# Comércio

<div class="alert alert-warning" data-alert="warning" role="alert"><p>O CS50W não possui uma correspondência um para um entre aulas e projetos. Se você está tentando este projeto sem ter assistido pelo menos à Aula 4, está tentando cedo demais!</p></div>

Crie um site de leilões de comércio eletrônico semelhante ao eBay que permitirá aos usuários postar listagens de leilões, fazer lances em listagens, comentar essas listagens e adicionar listagens a uma "lista de observação".

![Página de listagens ativas](https://cs50.harvard.edu/web/2020/projects/2/images/listings.png)

![Página de listagem](https://cs50.harvard.edu/web/2020/projects/2/images/listing.png)

## Primeiros Passos

1.  Faça o download do código de distribuição em [https://cdn.cs50.net/web/2020/spring/projects/2/commerce.zip](https://cdn.cs50.net/web/2020/spring/projects/2/commerce.zip) e extraia-o.
2.  No seu terminal, acesse o diretório `commerce`.
3.  Execute `python manage.py makemigrations auctions` para fazer as migrações para o aplicativo `auctions`.
4.  Execute `python manage.py migrate` para aplicar as migrações ao seu banco de dados.

## Compreender

No código de distribuição, há um projeto Django chamado `commerce` que contém um único aplicativo chamado `auctions`.

Primeiramente, abra `auctions/urls.py`, onde a configuração da URL para este aplicativo está definida. Observe que já escrevemos algumas URLs para você, incluindo uma rota de índice padrão, uma rota `/login`, uma rota `/logout` e uma rota `/register`.

Dê uma olhada em `auctions/views.py` para ver as visualizações associadas a cada uma dessas rotas. A visualização do índice por enquanto retorna um modelo `index.html` principalmente vazio. A visualização `login_view` renderiza um formulário de login quando um usuário tenta acessar a página. Quando um usuário envia o formulário usando o método de solicitação POST, o usuário é autenticado, logado e redirecionado para a página de índice. A visualização `logout_view` faz logout do usuário e o redireciona para a página de índice. Por fim, a rota `register` exibe um formulário de registro para o usuário e cria um novo usuário quando o formulário é enviado. Tudo isso já está feito para você no código de distribuição, então você deve poder executar a aplicação agora para criar alguns usuários.

Execute `python manage.py runserver` para iniciar o servidor web Django e acesse o site em seu navegador. Clique em "Register" e registre uma conta. Você deverá ver que agora está "Conectado como" sua conta de usuário e os links no topo da página mudaram. Como o HTML mudou? Dê uma olhada em `auctions/templates/auctions/layout.html` para o layout HTML desta aplicação. Observe que várias partes do modelo são envolvidas em uma verificação se `user.is_authenticated`, para que diferentes conteúdos possam ser renderizados dependendo se o usuário está conectado ou não. Você pode modificar este arquivo se desejar adicionar ou modificar algo no layout!

Por fim, dê uma olhada em `auctions/models.py`. É aqui que você definirá quaisquer modelos para sua aplicação web, onde cada modelo representa um tipo de dado que deseja armazenar no seu banco de dados. Iniciamos com um modelo `User` que representa cada usuário da aplicação. Como ele herda de `AbstractUser`, já terá campos para um nome de usuário, email, senha, etc., mas você pode adicionar novos campos à classe `User` se houver informações adicionais sobre um usuário que deseja representar. Você também precisará adicionar modelos adicionais a este arquivo para representar detalhes sobre listagens de leilões, lances, comentários e categorias de leilão. Lembre-se de que cada vez que você alterar algo em `auctions/models.py`, precisará executar primeiro `python manage.py makemigrations` e então `python manage.py migrate` para migrar essas alterações para o seu banco de dados.

## Especificação

Complete a implementação do seu site de leilões. Você deve cumprir os seguintes requisitos:

-   **Modelos**: Sua aplicação deve ter pelo menos três modelos além do modelo `User`: um para listagens de leilões, um para lances e um para comentários feitos em listagens de leilões. Cabe a você decidir quais campos cada modelo deve ter e quais devem ser os tipos desses campos. Você pode ter modelos adicionais se desejar.
-   **Criar Listagem**: Os usuários devem poder visitar uma página para criar uma nova listagem. Eles devem ser capazes de especificar um título para a listagem, uma descrição em texto e qual deve ser o lance inicial. Os usuários também devem poder fornecer opcionalmente uma URL para uma imagem da listagem e/ou uma categoria (por exemplo, Moda, Brinquedos, Eletrônicos, Casa, etc.).
-   **Página de Listagens Ativas**: A rota padrão de sua aplicação web deve permitir aos usuários visualizar todas as listagens de leilão ativas no momento. Para cada listagem ativa, esta página deve exibir (no mínimo) o título, a descrição, o preço atual e a foto (se houver) da listagem.
-   **Página de Listagem**: Clicar em uma listagem deve levar os usuários a uma página específica para essa listagem. Nessa página, os usuários devem poder visualizar todos os detalhes sobre a listagem, incluindo o preço atual da listagem.
    -   Se o usuário estiver conectado, ele deve poder adicionar o item à sua "Lista de Observação". Se o item já estiver na lista de observação, o usuário deve poder removê-lo.
    -   Se o usuário estiver conectado, ele deve poder dar lances no item. O lance deve ser pelo menos tão grande quanto o lance inicial e maior do que quaisquer outros lances já feitos (se houver). Se o lance não atender a esses critérios, o usuário deve receber um erro.
    -   Se o usuário estiver conectado e for o responsável por criar a listagem, ele deve ter a capacidade de "fechar" o leilão nesta página, tornando o maior licitante o vencedor do leilão e tornando a lista não mais ativa.
    -   Se um usuário estiver conectado em uma página de listagem fechada e o usuário tiver ganhado o leilão, a página deve informar isso.
    -   Usuários conectados devem poder adicionar comentários à página da listagem. A página da listagem deve exibir todos os comentários que foram feitos na listagem.
-   **Lista de Observação**: Usuários que estiverem conectados devem poder visitar uma página de Lista de Observação, que deve exibir todas as listagens que um usuário adicionou à sua lista de observação. Clicar em qualquer uma dessas listagens deve levar o usuário à página dessa listagem.
-   **Categorias**: Os usuários devem poder visitar uma página que exibe uma lista de todas as categorias de listagens. Clicar no nome de qualquer categoria deve levar o usuário a uma página que exibe todas as listagens ativas nessa categoria.
-   **Interface do Django Admin**: Por meio da interface do Django Admin, um administrador do site deve poder visualizar, adicionar, editar e excluir quaisquer listagens, comentários e lances feitos no site.

## Dicas

-   Para criar uma conta de superusuário que pode acessar a interface de administração do Django, execute `python manage.py createsuperuser`.
-   Consulte a [referência de campos de modelo do Django](https://docs.djangoproject.com/pt-br/4.0/ref/models/fields/) para possíveis tipos de campos para o modelo Django.
-   Provavelmente você precisará criar alguns [formulários do Django](https://docs.djangoproject.com/pt-br/4.0/topics/forms/) para várias partes desta aplicação web.
-   Adicionar o decorador [`@login_required`](https://docs.djangoproject.com/pt-br/4.0/topics/auth/default/#the-login-required-decorator) acima de qualquer visualização garantirá que apenas um usuário logado possa acessar aquela visualização.
-   Você pode modificar o CSS quanto quiser para tornar o site único! Algumas capturas de tela de exemplo são mostradas no início desta página. Elas são apenas exemplos: sua aplicação não precisa ser esteticamente igual às capturas de tela aqui (é encorajado ser criativo!).

## Como Enviar

1.  Visite [este link](https://submit.cs50.io/invites/89679428401548238ceb022f141b9947), faça login com sua conta do GitHub e clique em **Authorize cs50**. Em seguida, marque a caixa indicando que deseja conceder acesso à equipe do curso às suas inscrições e clique em **Join course**.
2.  [Instale o Git](https://git-scm.com/downloads) e, opcionalmente, [instale o `submit50`](https://cs50.readthedocs.io/submit50/).

<div class="alert alert-success" data-alert="success" role="alert"><p>Quando enviar seu projeto, o conteúdo do seu ramo <code class="language-plaintext highlighter-rouge">web50/projects/2020/x/commerce</code> deve corresponder à estrutura de arquivos do código de distribuição descompactado originalmente recebido. Ou seja, seus arquivos não devem estar aninhados dentro de quaisquer outros diretórios criados por você. Seu ramo também não deve conter código de outros projetos, apenas deste. O não cumprimento dessa estrutura de arquivos provavelmente resultará na rejeição da sua submissão.</p>

<p>A título de exemplo, para este projeto, isso significa que se a equipe de avaliação visitar <code class="language-plaintext highlighter-rouge">https://github.com/me50/USERNAME/tree/web50/projects/2020/x/commerce</code> (onde <code class="language-plaintext highlighter-rouge">USERNAME</code> é seu nome de usuário do GitHub fornecido no formulário abaixo), deveríamos ver os dois subdiretórios (<code class="language-plaintext highlighter-rouge">auctions</code>, <code class="language-plaintext highlighter-rouge">commerce</code>) e o arquivo <code class="language-plaintext highlighter-rouge">manage.py</code>. Se sua organização do código não estiver como mencionado, reorganize seu repositório conforme necessário para corresponder a esse paradigma.</p></div>

3.  Se você instalou o `submit50`, execute

        submit50 web50/projects/2020/x/commerce

    Caso contrário, usando o Git, envie seu trabalho para `https://github.com/me50/USERNAME.git`, onde `USERNAME` é seu nome de usuário do GitHub, em um ramo chamado `web50/projects/2020/x/commerce`.

4.  [Faça uma gravação de tela](https://www.howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen/) que não exceda 5 minutos de duração (e não tenha sido enviada mais de um mês antes da sua submissão deste projeto), na qual você demonstra a funcionalidade do seu projeto. Certifique-se de que todos os elementos da especificação acima sejam demonstrados em seu vídeo. Não é necessário mostrar seu código neste vídeo, apenas sua aplicação em ação; revisaremos seu código no GitHub. [Faça o upload desse vídeo no YouTube](https://www.youtube.com/upload) (como não listado ou público, mas não privado) ou em outro lugar. Na descrição do seu vídeo, você deve marcar o tempo em que seu vídeo demonstra cada um dos sete (7) elementos da especificação. **Isso não é opcional**, vídeos sem tempos marcados em suas descrições serão rejeitados automaticamente.
5.  Envie [este formulário](https://forms.cs50.io/5659f5b5-7354-4a35-9cc1-d8933840302c).

Então, você pode acessar [https://cs50.me/cs50w](https://cs50.me/cs50w) para visualizar seu progresso atual!
