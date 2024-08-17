# Finance C$50

Implementa un sitio web a través del cual los usuarios pueden "comprar" y "vender" acciones, à la siguiente imagen.

![Finance C$50](https://cs50.harvard.edu/x/2024/psets/9/finance/finance_2024.png)

## Trasfondo

Si no estás seguro de lo que significa comprar y vender acciones (por ejemplo, acciones de una empresa), consulta [aquí](https://www.investopedia.com/articles/basics/06/invest1000.asp) para obtener un tutorial.

Estás a punto de implementar Finance C$50, una aplicación web a través de la cual puedes administrar carteras de acciones. Esta herramienta no solo te permitirá verificar los precios reales de las acciones y los valores de las carteras, sino que también te permitirá comprar (bueno, "comprar") y vender (bueno, "vender") acciones consultando los precios de las acciones.

De hecho, existen herramientas (una se conoce como IEX) que te permiten descargar cotizaciones de acciones a través de su API (interfaz de programación de aplicaciones) utilizando URL como `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Observa cómo el símbolo de Netflix (NFLX) está incrustado en esta URL; así es como IEX sabe de quién devolver los datos. Ese enlace en realidad no devolverá ningún dato porque IEX requiere que uses una clave API, pero si lo hiciera, verías una respuesta en formato JSON (JavaScript Object Notation) como esta:

    {
      "avgTotalVolume":6787785,
      "calculationPrice":"tops",
      "change":1.46,
      "changePercent":0.00336,
      "close":null,
      "closeSource":"official",
      "closeTime":null,
      "companyName":"Netflix Inc.",
      "currency":"USD",
      "delayedPrice":null,
      "delayedPriceTime":null,
      "extendedChange":null,
      "extendedChangePercent":null,
      "extendedPrice":null,
      "extendedPriceTime":null,
      "high":null,
      "highSource":"IEX real time price",
      "highTime":1699626600947,
      "iexAskPrice":460.87,
      "iexAskSize":123,
      "iexBidPrice":435,
      "iexBidSize":100,
      "iexClose":436.61,
      "iexCloseTime":1699626704609,
      "iexLastUpdated":1699626704609,
      "iexMarketPercent":0.00864679844447232,
      "iexOpen":437.37,
      "iexOpenTime":1699626600859,
      "iexRealtimePrice":436.61,
      "iexRealtimeSize":5,
      "iexVolume":965,
      "lastTradeTime":1699626704609,
      "latestPrice":436.61,
      "latestSource":"IEX real time price",
      "latestTime":"9:31:44 AM",
      "latestUpdate":1699626704609,
      "latestVolume":null,
      "low":null,
      "lowSource":"IEX real time price",
      "lowTime":1699626634509,
      "marketCap":192892118443,
      "oddLotDelayedPrice":null,
      "oddLotDelayedPriceTime":null,
      "open":null,
      "openTime":null,
      "openSource":"official",
      "peRatio":43.57,
      "previousClose":435.15,
      "previousVolume":2735507,
      "primaryExchange":"NASDAQ",
      "symbol":"NFLX",
      "volume":null,
      "week52High":485,
      "week52Low":271.56,
      "ytdChange":0.4790450244167119,
      "isUSMarketOpen":true
    }

Observa cómo, entre las llaves, hay una lista separada por comas de pares clave-valor, con un dos puntos que separa cada clave de su valor. Haremos algo muy similar con Yahoo Finance.

¡Pasemos nuestra atención ahora a obtener el código de distribución de este problema!

## Primeros pasos

Inicia sesión en [cs50.dev](https://cs50.dev/), haz clic en tu ventana de terminal y ejecuta `cd` por sí mismo. Deberías encontrar que el mensaje de la ventana de tu terminal se asemeja al siguiente:

    $

Luego ejecuta

    wget https://cdn.cs50.net/2024/x/psets/9/finance.zip

para descargar un ZIP llamado `finance.zip` en tu espacio de código.

Luego ejecuta

    unzip finance.zip

para crear una carpeta llamada `finance`. Ya no necesitas el archivo ZIP, por lo que puedes ejecutar

    rm finance.zip

y responde con "y" seguido de Enter en el mensaje para eliminar el archivo ZIP que descargaste.

Ahora escribe

    cd finance

seguido de Enter para moverte a ese directorio (es decir, abrirlo). Tu mensaje ahora debería parecerse al siguiente.

    finance/ $

Ejecuta `ls` por sí solo y deberías ver algunos archivos y carpetas:

    app.py  finance.db  helpers.py  requirements.txt  static/  templates/

Si te encuentras con algún problema, ¡sigue estos mismos pasos nuevamente y ve si puedes determinar dónde te equivocaste!

### Ejecución

Inicia el servidor web integrado de Flask (dentro de `finance/`):

    $ flask run

Visita la URL generada por `flask` para ver el código de distribución en acción. ¡Sin embargo, no podrás iniciar sesión ni registrarte todavía!

Dentro de `finance/`, ejecuta `sqlite3 finance.db` para abrir `finance.db` con `sqlite3`. Si ejecutas `.schema` en el mensaje de SQLite, observa cómo `finance.db` viene con una tabla llamada `users`. Echa un vistazo a su estructura (es decir, esquema). Observa cómo, de forma predeterminada, los nuevos usuarios recibirán $10,000 en efectivo. Pero si ejecutas `SELECT * FROM users;`, aún no hay usuarios (es decir, filas) para navegar.

Otra forma de ver `finance.db` es con un programa llamado phpLiteAdmin. Haz clic en `finance.db` en el explorador de archivos de tu espacio de códigos, luego haz clic en el enlace que se muestra debajo del texto "Visita el siguiente enlace para autorizar la vista previa de GitHub". Deberías ver información sobre la base de datos en sí, así como una tabla, `users`, tal como la viste en el mensaje `sqlite3` con `.schema`.

### Comprendre

#### `app.py`

Ouvrez `app.py`. En haut du fichier se trouvent plusieurs imports, parmi lesquels le module SQL de CS50 et quelques fonctions d'aide. Plus d'informations à leur sujet bientôt.

Après avoir configuré [Flask](https://flask.palletsprojects.com/), remarquez comment ce fichier désactive la mise en cache des réponses (à condition que vous soyez en mode débogage, ce qui est le cas par défaut dans votre espace de code code50), de peur que vous ne modifiiez un fichier sans que votre navigateur ne s'en aperçoive. Remarquez ensuite comment il configure [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) avec un « filtre » personnalisé, `usd`, une fonction (définie dans `helpers.py`) qui facilitera le formatage des valeurs en dollars américains (USD). Il configure ensuite Flask pour stocker les [sessions](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions) sur le système de fichiers local (c'est-à-dire le disque) au lieu de les stocker dans des cookies (signés numériquement), ce qui est la valeur par défaut de Flask. Le fichier configure ensuite le module SQL de CS50 pour utiliser `finance.db`.

Par la suite, il y a tout un tas d'itinéraires, dont seulement deux sont entièrement implémentés : `login` et `logout`. Lisez d'abord la mise en œuvre de `login`. Notez qu'il utilise `db.execute` (de la bibliothèque de CS50) pour interroger `finance.db`. Et remarquez comment il utilise `check_password_hash` pour comparer les hachages des mots de passe des utilisateurs. Notez également que `login` « se souvient » qu'un utilisateur est connecté en stockant son `user_id`, un entier, dans `session`. De cette façon, toutes les routes de ce fichier peuvent vérifier quel utilisateur, le cas échéant, est connecté. Enfin, notez qu'une fois que l'utilisateur s'est connecté avec succès, `login` redirigera vers « / », amenant l'utilisateur à sa page d'accueil. En revanche, remarquez que « logout » efface simplement la « session », déconnectant ainsi un utilisateur.

Notez que la plupart des itinéraires sont « décorés » avec `@login_required` (une fonction également définie dans `helpers.py`). Ce décorateur garantit que, si un utilisateur essaie de visiter l'un de ces itinéraires, il sera d'abord redirigé vers `login` pour se connecter.

Notez également que la plupart des itinéraires prennent en charge GET et POST. Malgré cela, la plupart d'entre eux (pour l'instant !) retournent simplement un « excuse », car ils ne sont pas encore implémentés.

#### `helpers.py`

Ensuite, jetez un œil à `helpers.py`. Ah, voici l'implémentation de `apology`. Notez qu'il finit par restituer un modèle, `apology.html`. Il arrive également à définir en lui-même une autre fonction, `escape`, qu'il utilise simplement pour remplacer les caractères spéciaux dans les excuses. En définissant `escape` à l'intérieur de `apology`, nous avons limité celui-ci à ce dernier ; aucune autre fonction ne pourra (ou n'aura besoin) de l'appeler.

Vient ensuite dans le fichier `login_required`. Ne vous inquiétez pas si celui-ci est un peu cryptique, mais si vous vous êtes déjà demandé comment une fonction peut renvoyer une autre fonction, voici un exemple !

Vient ensuite `lookup`, une fonction qui, étant donné un « symbole » (par exemple, NFLX), renvoie une cotation boursière pour une société sous la forme d'un `dict` avec deux clés : `price`, dont la valeur est un `float` ; et `symbol`, dont la valeur est un `str`, une version canonique (en majuscules) du symbole d'une action, quelle que soit la manière dont ce symbole a été capitalisé lorsqu'il a été transmis à `lookup`.

<div class="alert alert-warning" data-alert="warning" role="alert"><p>Veuillez noter. Si vous avez commencé ce problème en 2023, notez que <code class="language-plaintext highlighter-rouge">lookup</code> ne renvoie plus une clé de <code class="language-plaintext highlighter-rouge">name</code>, alors assurez-vous de la supprimer de toute requête qui l'attend. Aucun nom ne doit être affiché sur aucune page.</p></div>

Enfin, dans le fichier, se trouve `usd`, une courte fonction qui formate simplement un `float` en USD (par exemple, `1234.56` est formaté en `$1,234.56`).

#### `requirements.txt`

Jetez ensuite un coup d'œil à `requirements.txt`. Ce fichier prescrit simplement les packages dont cette application dépendra.

#### `static/`

Jetez également un coup d'œil à `static/`, à l'intérieur duquel se trouve `styles.css`. C'est là que vit un peu de CSS initial. Vous êtes libre de le modifier comme bon vous semble.

#### `templates/`

Maintenant, regardez dans `templates/`. Dans `login.html`, il s'agit essentiellement d'un simple formulaire HTML, stylisé avec [Bootstrap](https://getbootstrap.com/). Dans `apology.html`, en revanche, se trouve un modèle d'excuses. Rappelez-vous que `apology` dans `helpers.py` prenait deux arguments : `message`, qui était transmis à `render_template` comme valeur de `bottom`, et, éventuellement, `code`, qui était transmis à `render_template` comme valeur de `top`. Remarquez dans `apology.html` comment ces valeurs sont finalement utilisées ! Et [voici pourquoi](https://github.com/jacebrowning/memegen) 0:-)

Enfin, il y a `layout.html`. C'est un peu plus grand que d'habitude, mais c'est surtout parce qu'il est livré avec une « barre de navigation » (barre de navigation) sophistiquée et adaptée aux mobiles, également basée sur Bootstrap. Remarquez comment il définit un bloc, `main`, à l'intérieur duquel iront les modèles (y compris `apology.html` et `login.html`). Il inclut également la prise en charge du [message clignotant](https://flask.palletsprojects.com/en/1.1.x/quickstart/#message-flashing) de Flask afin que vous puissiez relayer les messages d'une route à une autre pour que l'utilisateur les voie.

## Spécification

### `register`

Complétez la mise en œuvre de `register` de telle sorte qu'elle permette à un utilisateur de s'inscrire pour un compte via un formulaire.

- Exiger qu'un utilisateur saisisse un nom d'utilisateur, implémenté comme un champ de texte dont le `name` est `username`. Affichez des excuses si l'entrée de l'utilisateur est vide ou si le nom d'utilisateur existe déjà.
  - Notez que [`cs50.SQL.execute`](https://cs50.readthedocs.io/libraries/cs50/python/#cs50.SQL) lèvera une exception `ValueError` si vous essayez d'`INSERT` un nom d'utilisateur en double parce que nous avons créé un `UNIQUE INDEX` sur `users.username`. Veillez donc à utiliser `try` et `except` pour déterminer si le nom d'utilisateur existe déjà.
- Exiger qu'un utilisateur saisisse un mot de passe, implémenté comme un champ de texte dont le `name` est `password`, puis le même mot de passe à nouveau, implémenté comme un champ de texte dont le `name` est `confirmation`. Affichez des excuses si l'une des entrées est vide ou si les mots de passe ne correspondent pas.
- Soumettez l'entrée de l'utilisateur via `POST` à `/register`.
- `INSERT` le nouvel utilisateur dans `users`, en stockant un hachage du mot de passe de l'utilisateur, et non le mot de passe lui-même. Hachez le mot de passe de l'utilisateur avec [`generate_password_hash`](https://werkzeug.palletsprojects.com/en/2.3.x/utils/#werkzeug.security.generate_password_hash) Il y a de fortes chances que vous souhaitiez créer un nouveau modèle (par exemple, `register.html`) assez similaire à `login.html`.

Une fois que vous avez correctement implémenté `register`, vous devriez pouvoir créer un compte et vous connecter (puisque `login` et `logout` fonctionnent déjà) ! Et vous devriez pouvoir voir vos lignes via phpLiteAdmin ou `sqlite3`.

### `quote`

Complétez la mise en œuvre de `quote` de telle sorte qu'elle permette à un utilisateur de rechercher le prix actuel d'une action.

- Exiger qu'un utilisateur saisisse le symbole d'une action, implémenté comme un champ de texte dont

### `buy`

Complétez l'implémentation de `buy` de telle sorte qu'elle permette à un utilisateur d'acheter des actions.

- Exigez qu'un utilisateur saisisse un symbole d'action, implémenté comme un champ texte dont le `name` est `symbol`. Affichez une excuse si l'entrée est vide ou si le symbole n'existe pas (selon la valeur renvoyée par `lookup`).
- Exigez qu'un utilisateur saisisse un nombre d'actions, implémenté comme un champ texte dont le `name` est `shares`. Affichez une excuse si l'entrée n'est pas un entier positif.
- Soumettez la saisie de l'utilisateur via `POST` à `/buy`.
- Une fois terminé, redirigez l'utilisateur vers la page d'accueil.
- Il y a de fortes chances que vous deviez appeler `lookup` pour rechercher le prix actuel d'une action.
- Il y a de fortes chances que vous deviez `SELECT` le montant d'argent liquide dont dispose actuellement l'utilisateur dans `users`.
- Ajoutez une ou plusieurs nouvelles tables à `finance.db` pour assurer le suivi de l'achat. Stockez suffisamment d'informations pour savoir qui a acheté quoi, à quel prix et quand.
  - Utilisez des types SQLite appropriés.
  - Définissez des index `UNIQUE` sur tous les champs qui doivent être uniques.
  - Définissez des index (non `UNIQUE`) sur tous les champs par lesquels vous effectuerez une recherche (comme via `SELECT` avec `WHERE`).
- Affichez une excuse, sans terminer l'achat, si l'utilisateur n'a pas les moyens d'acquérir le nombre d'actions au prix actuel.
- Vous n'avez pas à vous soucier des conditions de course (ou utiliser des transactions).

Une fois que vous avez implémenté `buy` correctement, vous devriez pouvoir voir les achats des utilisateurs dans vos nouvelles tables via phpLiteAdmin ou `sqlite3`.

### `index`

Complétez l'implémentation de `index` de telle sorte qu'elle affiche un tableau HTML résumant, pour l'utilisateur actuellement connecté, les actions que l'utilisateur possède, le nombre d'actions possédées, le prix actuel de chaque action et la valeur totale de chaque avoir (c'est-à-dire les actions fois le prix). Affichez également le solde de trésorerie actuel de l'utilisateur ainsi qu'un total général (c'est-à-dire la valeur totale des actions plus la trésorerie).

- Il y a de fortes chances que vous deviez exécuter plusieurs `SELECT`s. Selon la façon dont vous implémentez vos tables, vous pourriez trouver [GROUP BY](https://www.google.com/search?q=SQLite+GROUP+BY,) [HAVING](https://www.google.com/search?q=SQLite+HAVING,) [SUM](https://www.google.com/search?q=SQLite+SUM,) et/ou [WHERE](https://www.google.com/search?q=SQLite+WHERE) intéressant.
- Il y a de fortes chances que vous deviez appeler `lookup` pour chaque action.

### `sell`

Complétez l'implémentation de `sell` de telle sorte qu'elle permette à un utilisateur de vendre des actions d'une action (qu'il possède).

- Exigez qu'un utilisateur saisisse le symbole d'une action, implémenté comme un menu `select` dont le `name` est `symbol`. Affichez une excuse si l'utilisateur ne parvient pas à sélectionner une action ou si (d'une manière ou d'une autre, une fois soumis) l'utilisateur ne possède aucune action de cette action.
- Exigez qu'un utilisateur saisisse un nombre d'actions, implémenté comme un champ texte dont le `name` est `shares`. Affichez une excuse si l'entrée n'est pas un entier positif ou si l'utilisateur ne possède pas autant d'actions de l'action.
- Soumettez la saisie de l'utilisateur via `POST` à `/sell`.
- Une fois terminé, redirigez l'utilisateur vers la page d'accueil.
- Vous n'avez pas à vous soucier des conditions de course (ou utiliser des transactions).

### `history`

Complétez l'implémentation de `history` de telle sorte qu'elle affiche un tableau HTML résumant toutes les transactions d'un utilisateur, en listant ligne par ligne chaque achat et chaque vente.

- Pour chaque ligne, indiquez clairement si une action a été achetée ou vendue et incluez le symbole de l'action, le prix (d'achat ou de vente), le nombre d'actions achetées ou vendues, ainsi que la date et l'heure auxquelles la transaction a eu lieu.
- Vous devrez peut-être modifier la table que vous avez créée pour `buy` ou la compléter avec une table supplémentaire. Essayez de minimiser les redondances.

### Touche personnelle

Implémentez au moins une touche personnelle de votre choix :

- Permettre aux utilisateurs de modifier leurs mots de passe.
- Permettre aux utilisateurs d'ajouter de l'argent liquide supplémentaire à leur compte.
- Permettre aux utilisateurs d'acheter plus d'actions ou de vendre des actions qu'ils possèdent déjà via l'index lui-même, sans avoir à taper manuellement les symboles des actions.
- Implémentez une autre fonctionnalité de portée comparable.

## Procédure pas à pas

<div class="alert alert-info" data-alert="info" role="alert"><p>Notez que Brian mentionne que <code class="language-plaintext highlighter-rouge">lookup</code> renverra le nom de l'action. Selon ce qui précède, il ne renvoie plus que le prix et le symbole.</p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/7wPTAwT-6bA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Essais

Assurez-vous de tester manuellement votre application Web, comme suit :

- enregistrer un nouvel utilisateur et vérifier que sa page de portefeuille se charge avec les informations correctes,
- demander un devis en utilisant un symbole d'action valide,
- acheter une action plusieurs fois, en vérifiant que le portefeuille affiche les totaux corrects,
- vendre tout ou partie d'une action, en vérifiant à nouveau le portefeuille, et
- vérifier que votre page d'historique affiche toutes les transactions de votre utilisateur connecté.

Testez également des utilisations inattendues, comme suit :

- saisir des chaînes alphabétiques dans des formulaires lorsque seuls des chiffres sont attendus,
- saisir des nombres zéro ou négatifs dans des formulaires lorsque seuls des nombres positifs sont attendus,
- saisir des valeurs à virgule flottante dans des formulaires lorsque seuls des entiers sont attendus,
- essayer de dépenser plus d'argent liquide qu'un utilisateur n'en a,
- essayer de vendre plus d'actions qu'un utilisateur n'en possède,
- saisir un symbole d'action invalide, et
- inclure des caractères potentiellement dangereux comme `'` et `;` dans les requêtes SQL.

Vous pouvez également vérifier la validité de votre HTML en cliquant sur le bouton **I ♥ VALIDATOR** dans le pied de page de chacune de vos pages, qui publiera votre HTML sur [validator.w3.org](https://validator.w3.org/).

Une fois satisfait, pour tester votre code avec `check50`, exécutez ce qui suit.

    check50 cs50/problems/2024/x/finance

<div class="alert alert-warning" data-alert="warning" role="alert"><p>Sachez que <code class="language-plaintext highlighter-rouge">check50</code> testera l'ensemble de votre programme dans son ensemble. Si vous l'exécutez <strong>avant</strong> d'avoir terminé toutes les fonctions requises, il peut signaler des erreurs sur des fonctions qui sont en réalité correctes mais qui dépendent d'autres fonctions.</p></div>

## Style

    style50 app.py

## Solution du staff

Vous êtes libre de styliser votre propre application différemment, mais voici à quoi ressemble la solution du staff !

[https://finance.cs50.net/](https://finance.cs50.net/)

N’hésitez pas à créer un compte et à vous amuser. N’utilisez **pas** un mot de passe que vous utilisez sur d’autres sites.

Il est **raisonnable** de consulter le HTML et le CSS du staff.

## Astuces

- Pour formater une valeur comme une valeur de dollar américain (avec des cents indiqués à deux décimales), vous pouvez utiliser le filtre `usd` dans vos modèles Jinja (en imprimant les valeurs comme `{{ value | usd }}` au lieu de `{{ value }}`.
- Dans `cs50.SQL`, il existe une méthode `execute` dont le premier argument doit être une `str` de SQL. Si cette `str` contient des paramètres de points d’interrogation auxquels des valeurs doivent être liées, ces valeurs peuvent être fournies comme des paramètres nommés supplémentaires à `execute`. Voir l’implémentation de `login` pour un exemple de ce type. La valeur de retour de `execute` est la suivante :
  - Si `str` est un `SELECT`, alors `execute` renvoie une `list` d’au moins zéro objet `dict`, à l’intérieur desquels se trouvent des clés et des valeurs représentant respectivement les champs et les cellules d’une table.
  - Si `str` est un `INSERT` et que la table dans laquelle les données ont été insérées contient une `PRIMARY KEY` auto-incrémentante, alors `execute` renvoie la valeur de la clé primaire de la ligne nouvellement insérée.
  - Si `str` est un `DELETE` ou un `UPDATE`, alors `execute` renvoie le nombre de lignes supprimées ou mises à jour par `str`.
- Rappelez-vous que `cs50.SQL` enregistrera dans votre fenêtre de terminal toutes les requêtes que vous exécutez via `execute` (afin que vous puissiez vérifier qu’elles sont comme prévu).
- Veillez à utiliser des paramètres liés à un point d’interrogation (c’est-à-dire, un [style de paramètre](https://www.python.org/dev/peps/pep-0249/#paramstyle) de `named`) lorsque vous appelez la méthode `execute` de CS50, à la façon de `WHERE ?`. N’utilisez **pas** de f-strings, [`format`](https://docs.python.org/3.6/library/functions.html#format,) ou `+` (c’est-à-dire, la concaténation), de peur de risquer une attaque par injection SQL.
- Si (et seulement si) vous êtes déjà à l’aise avec SQL, vous pouvez utiliser [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/index.html) ou [Flask-SQLAlchemy](https://flask-sqlalchemy.pocoo.org/) (c’est-à-dire, [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/index.html)) au lieu de `cs50.SQL`.
- Vous pouvez ajouter des fichiers statiques supplémentaires à `static/`.
- Il y a de fortes chances que vous souhaitiez consulter la [documentation de Jinja](https://jinja.palletsprojects.com/en/3.1.x/) lors de l’implémentation de vos modèles.
- Il est **raisonnable** de demander à d’autres personnes d’essayer (et d’essayer de déclencher des erreurs) sur votre site.
- Vous êtes libre de modifier l’esthétique des sites, comme via
  - [bootswatch.com](https://bootswatch.com/),
  - [getbootstrap.com/docs/5.1/content](https://getbootstrap.com/docs/5.1/content/),
  - [getbootstrap.com/docs/5.1/components](https://getbootstrap.com/docs/5.1/components/), et/ou
  - [memegen.link](https://memegen.link/).
- Vous pouvez trouver la [documentation de Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) et la [documentation de Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/) utiles !

## FAQ

### ImportError : No module named ‘application’

Par défaut, `flask` recherche un fichier nommé `app.py` dans votre répertoire de travail actuel (car nous avons configuré la valeur de `FLASK_APP`, une variable d’environnement, à `app.py`). Si vous voyez cette erreur, il y a de fortes chances que vous ayez exécuté `flask` dans le mauvais répertoire !

### OSError : \[Errno 98\] Address already in use

Si, lors de l’exécution de `flask`, vous voyez cette erreur, il y a de fortes chances que (vous) ayez (encore) `flask` en cours d’exécution dans un autre onglet. Assurez-vous de terminer cet autre processus, comme avec Ctrl-C, avant de redémarrer `flask`. Si vous n’avez pas d’autre onglet de ce type, exécutez `fuser -k 8080/tcp` pour terminer tous les processus qui écoutent (encore) sur le port TCP 8080.

## Comment soumettre

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail.

    submit50 cs50/problems/2024/x/finance

<div class="alert alert-danger" data-alert="danger" role="alert"><h3 id="why-does-my-submission-pass-check50-but-shows-no-results-in-my-gradebook-after-running-submit50">Pourquoi ma soumission réussit-elle à check50, mais affiche-t-elle « Aucun résultat » dans mon Gradebook après l’exécution de submit50 ?</h3>

<p>Dans certains cas, <code class="language-plaintext highlighter-rouge">submit50</code> peut ne pas noter le devoir en raison de : (1) un formatage incohérent dans votre fichier <code class="language-plaintext highlighter-rouge">app.py</code>, et/ou (2) d’autres fichiers inutiles soumis avec le problème défini. Pour résoudre ces problèmes, exécutez <code class="language-plaintext highlighter-rouge">black app.py</code> dans le dossier <code class="language-plaintext highlighter-rouge">finance</code>. Résolvez les problèmes qui sont révélés. Ensuite, examinez le contenu de votre dossier <code class="language-plaintext highlighter-rouge">finance</code>. Supprimez les fichiers superflus, tels que les sessions Flask ou d’autres fichiers qui ne font pas partie de votre implémentation du problème défini. De plus, exécutez à nouveau <code class="language-plaintext highlighter-rouge">check50</code> pour vous assurer que votre soumission fonctionne toujours. Enfin, exécutez à nouveau la commande <code class="language-plaintext highlighter-rouge">submit50</code> ci-dessus. Votre résultat apparaîtra dans votre <a href="https://cs50.me/cs50x">Gradebook</a> dans quelques minutes.</p>

<p>Veuillez noter que s’il y a un score numérique à côté de votre soumission de finance dans la zone <code class="language-plaintext highlighter-rouge">submissions</code> de votre <a href="https://cs50.me/cs50x">Gradebook</a>, la procédure décrite ci-dessus ne s’applique pas à vous. Il est probable que vous n’ayez pas entièrement rempli les exigences du problème défini et que vous devriez vous fier à <code class="language-plaintext highlighter-rouge">check50</code> pour obtenir des indices sur ce qu’il reste à faire.</p></div>

