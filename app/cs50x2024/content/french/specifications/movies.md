# Films

![Logo d'IMDb](https://cs50.harvard.edu/x/2024/psets/7/movies/imdb.png)

## Problème à résoudre

Un fichier appelé `movies.db` vous est fourni, une base de données SQLite qui stocke des données de [IMDb](https://www.imdb.com/) sur les films, les personnes qui les ont réalisés et joués, et leurs notes. Écrivez des requêtes SQL pour répondre à des questions sur cette base de données de films.

## Démo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-uPWDqSe0NjjqXLF3qxzpsMnfv" src="https://asciinema.org/a/uPWDqSe0NjjqXLF3qxzpsMnfv.js"></script>

## Prise en main

Pour ce problème, vous utiliserez une base de données fournie par le personnel de CS50.

Connectez-vous à [cs50.dev](https://cs50.dev/), cliquez sur votre fenêtre de terminal et exécutez `cd` seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ceci :

    $

Ensuite, exécutez :

    wget https://cdn.cs50.net/2023/fall/psets/7/movies.zip

afin de télécharger un ZIP appelé `movies.zip` dans votre espace de codage.

Puis, exécutez :

    unzip movies.zip

pour créer un dossier appelé `movies`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter :

    rm movies.zip

et répondre par « y » suivi de Entrée à l'invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez :

    cd movies

suivi de Entrée pour vous déplacer dans (c'est-à-dire pour ouvrir) ce répertoire. Votre invite doit maintenant ressembler à ceci :

    movies/ $

Exécutez `ls` seul, et vous devriez voir 13 fichiers .sql, ainsi que `movies.db`.

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous vous êtes trompé !

## Spécification

Pour chacun des problèmes suivants, vous devez écrire une seule requête SQL qui renvoie les résultats spécifiés par chaque problème. Votre réponse doit prendre la forme d'une seule requête SQL, bien que vous puissiez imbriquer d'autres requêtes dans votre requête. Vous **ne devez pas** faire de suppositions sur les `id` de films ou de personnes particuliers : vos requêtes doivent être exactes même si l'`id` d'un film ou d'une personne en particulier est différent. Enfin, chaque requête doit renvoyer uniquement les données nécessaires pour répondre à la question : si le problème vous demande uniquement d'indiquer les titres des films, par exemple, alors votre requête ne doit pas également indiquer l'année de sortie de chaque film.

Vous pouvez vérifier les résultats de vos requêtes par rapport à [IMDb](https://www.imdb.com/) lui-même, mais sachez que les notes sur le site Web peuvent différer de celles de `movies.db`, car davantage de votes ont pu être exprimés depuis que nous avons téléchargé les données !

1.  Dans `1.sql`, écrivez une requête SQL pour lister les titres de tous les films sortis en 2008.
    - Votre requête doit générer un tableau avec une seule colonne pour le titre de chaque film.
2.  Dans `2.sql`, écrivez une requête SQL pour déterminer l'année de naissance d'Emma Stone.
    - Votre requête doit générer un tableau avec une seule colonne et une seule ligne (sans compter l'en-tête) contenant l'année de naissance d'Emma Stone.
    - Vous pouvez supposer qu'il n'y a qu'une seule personne dans la base de données portant le nom d'Emma Stone.
3.  Dans `3.sql`, écrivez une requête SQL pour lister les titres de tous les films dont la date de sortie est égale ou supérieure à 2018, par ordre alphabétique.
    - Votre requête doit générer un tableau avec une seule colonne pour le titre de chaque film.
    - Les films sortis en 2018 doivent être inclus, ainsi que les films dont les dates de sortie sont futures.
4.  Dans `4.sql`, écrivez une requête SQL pour déterminer le nombre de films avec une note IMDb de 10,0.
    - Votre requête doit générer un tableau avec une seule colonne et une seule ligne (sans compter l'en-tête) contenant le nombre de films avec une note de 10,0.
5.  Dans `5.sql`, écrivez une requête SQL pour lister les titres et les années de sortie de tous les films Harry Potter, dans l'ordre chronologique.
    - Votre requête doit générer un tableau avec deux colonnes, une pour le titre de chaque film et une pour l'année de sortie de chaque film.
    - Vous pouvez supposer que le titre de tous les films Harry Potter commencera par les mots « Harry Potter », et que si le titre d'un film commence par les mots « Harry Potter », il s'agit d'un film Harry Potter.
6.  Dans `6.sql`, écrivez une requête SQL pour déterminer la note moyenne de tous les films sortis en 2012.
    - Votre requête doit générer un tableau avec une seule colonne et une seule ligne (sans compter l'en-tête) contenant la note moyenne.
7.  Dans `7.sql`, écrivez une requête SQL pour lister tous les films sortis en 2010 et leurs notes, par ordre décroissant de note. Pour les films ayant la même note, classez-les par ordre alphabétique selon leur titre.
    - Votre requête doit générer un tableau avec deux colonnes, une pour le titre de chaque film et une pour la note de chaque film.
    - Les films qui n'ont pas de notes ne doivent pas être inclus dans le résultat.
8.  Dans `8.sql`, écrivez une requête SQL pour lister les noms de toutes les personnes qui ont joué dans Toy Story.
    - Votre requête doit générer un tableau avec une seule colonne pour le nom de chaque personne.
    - Vous pouvez supposer qu'il n'y a qu'un seul film dans la base de données intitulé Toy Story.
9.  Dans `9.sql`, écrivez une requête SQL pour lister les noms de toutes les personnes qui ont joué dans un film sorti en 2004, classés par année de naissance.
    - Votre requête doit générer un tableau avec une seule colonne pour le nom de chaque personne.
    - Les personnes nées la même année peuvent être répertoriées dans n'importe quel ordre.
    - Vous n'avez pas à vous soucier des personnes dont l'année de naissance n'est pas indiquée, tant que celles qui ont une année de naissance sont répertoriées dans l'ordre.
    - Si une personne est apparue dans plusieurs films en 2004, elle ne doit apparaître dans vos résultats qu'une seule fois.
10. Dans `10.sql`, écrivez une requête SQL pour lister les noms de toutes les personnes ayant réalisé un film ayant reçu une note d'au moins 9,0.
    - Votre requête doit générer un tableau avec une seule colonne pour le nom de chaque personne.
    - Si une personne a réalisé plus d'un film ayant reçu une note d'au moins 9,0, elle ne doit apparaître dans vos résultats qu'une seule fois.
11. Dans `11.sql`, écrivez une requête SQL pour lister les titres des cinq films les mieux notés (par ordre) dans lesquels Chadwick Boseman a joué, en commençant par le mieux noté.
    - Votre requête doit générer un tableau avec une seule colonne pour le titre de chaque film.
    - Vous pouvez supposer qu'il n'y a qu'une seule personne dans la base de données portant le nom de Chadwick Boseman.
12. Dans `12.sql`, écrivez une requête SQL pour lister les titres de tous les films dans lesquels Bradley Cooper et Jennifer Lawrence ont joué.
    - Votre requête doit générer un tableau avec une seule colonne pour le titre de chaque film.
    - Vous pouvez supposer qu'il n'y a qu'une seule personne dans la base de données portant le nom de Bradley Cooper.
    - Vous pouvez supposer qu'il n'y a qu'une seule personne dans la base de données portant le nom de Jennifer Lawrence.
13. Dans `13.sql`, écrivez une requête SQL pour lister les noms de toutes les personnes qui ont joué dans un film dans lequel Kevin Bacon a également joué.
    - Votre requête doit générer un tableau avec une seule colonne pour le nom de chaque personne.
    - Il peut y avoir plusieurs personnes nommées Kevin Bacon dans la base de données. N'oubliez de sélectionner que le Kevin Bacon né en 1958.
    - Kevin Bacon lui-même ne doit pas

## Conseils

### Comprendre le schéma de `movies.db`

À chaque fois que vous utilisez une nouvelle base de données, il est préférable de commencer par comprendre son _schéma_. Dans une fenêtre de terminal, exécutez `sqlite3 movies.db` pour commencer à exécuter des requêtes sur la base de données.

Tout d'abord, lorsque `sqlite3` vous invite à fournir une requête, tapez `.schema` et appuyez sur entrée. Cela affichera les instructions `CREATE TABLE` qui ont été utilisées pour générer chacune des tables de la base de données. En examinant ces instructions, vous pouvez identifier les colonnes présentes dans chaque table.

Notez que la table `movies` a une colonne `id` qui identifie de manière unique chaque film, ainsi que des colonnes pour le `titre` d'un film et l'`année` de sortie du film. La table `people` a également une colonne `id`, ainsi que des colonnes pour chaque `nom` de personne et son année de `naissance`.

Les notes de film, quant à elles, sont stockées dans la table `ratings`. La première colonne de la table est `movie_id` : une clé étrangère qui référence l'`id` de la table `movies`. Le reste de la ligne contient des données sur la `note` de chaque film et le nombre de `votes` que le film a reçu sur IMDb.

Enfin, les tables `stars` et `directors` correspondent à des personnes aux films dans lesquels ils ont joué ou réalisé. (Seules les vedettes et les réalisateurs [principaux](https://www.imdb.com/interfaces/) sont inclus.) Chaque table ne comporte que deux colonnes : `movie_id` et `person_id`, qui font respectivement référence à un film et à une personne spécifiques.

Le défi qui vous attend est d'écrire des requêtes SQL pour répondre à différentes questions en sélectionnant des données dans une ou plusieurs de ces tables.

### Stylez vos requêtes de manière cohérente

Consultez [sqlstyle.guide](https://www.sqlstyle.guide/) pour obtenir des conseils sur le bon style en SQL, en particulier lorsque vos requêtes deviennent plus complexes !

### Répertorier les titres de tous les films sortis en 2008

Rappelez-vous que vous pouvez sélectionner une (ou plusieurs) colonnes d'une base de données à l'aide de `SELECT`, comme dans l'exemple ci-dessous,

    SELECT colonne0, colonne1 FROM table ;

où `colonne0` est le titre d'une colonne et `colonne1` le titre d'une autre.

Et rappelez-vous que vous pouvez filtrer les lignes renvoyées dans une requête avec le mot-clé `WHERE`, suivi d'une condition. Vous pouvez également utiliser `=`, `>`, `<` et [d'autres opérateurs](https://www.w3schools.com/sql/sql_operators.asp).

    SELECT colonne FROM table
    WHERE condition ;

Consultez [cette référence des mots-clés SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) pour une syntaxe SQL qui peut vous être utile !

### Déterminer l'année de naissance d'Emma Stone

Rappelez-vous qu'une clause `WHERE` peut évaluer des conditions non seulement avec des nombres, mais aussi avec des chaînes.

### Répertorier les titres de tous les films dont la date de sortie est postérieure ou égale à 2018, par ordre alphabétique

Essayez de diviser cette requête en deux étapes. D'abord, trouvez les films dont la date de sortie est en 2018 ou après. Ensuite, mettez les titres de ces films par ordre alphabétique.

Pour trouver les films dont la date de sortie est en 2018 ou après, rappelez-vous qu'une condition en SQL prend en charge l'utilisation de nombreux [opérateurs de comparaison](https://www.w3schools.com/sql/sql_operators.asp) courants, notamment `>=` pour « supérieur ou égal à ». Vérifiez si votre requête renvoie le nombre correct de films, conformément à [Comment tester](#comment-tester).

Enfin, triez les résultats de la requête par ordre alphabétique par titre. Rappelez-vous que `ORDER BY` peut trier les données par une colonne dans vos résultats, comme dans l'exemple ci-dessous.

    ...
    ORDER BY colonne ;

### Déterminer le nombre de films avec une note IMDb de 10,0

Notez que cette question ne vous demande pas les films _individuels_ ayant une note de 10,0, mais le _nombre_ de films ayant une telle note. En d'autres termes, vous devez collecter (« agréger ») les résultats de votre requête en un seul nombre (le nombre de lignes). Rappelez-vous que SQL prend en charge une « fonction d'agrégation » appelée `COUNT`, que vous pouvez utiliser sur une colonne comme dans l'exemple ci-dessous.

    SELECT COUNT(colonne)
    FROM table ;

### Répertorier les titres et les années de sortie de tous les films Harry Potter, par ordre chronologique

Pour cette requête, vous voudrez probablement utiliser le mot-clé `LIKE` de SQL. Rappelez-vous que `LIKE` peut utiliser des « caractères génériques », tels que `%`, qui correspondent à n'importe quel caractère (ou séquence de celui-ci).

    SELECT colonne0, colonne1
    FROM table
    WHERE colonne1 LIKE motif ;

### Déterminer la note moyenne de tous les films sortis en 2012

Voici un autre exemple de requête dans laquelle vous devez agréger des données. Considérez la fonction d'agrégation `AVG` de SQL, pour calculer une moyenne.

Tenez également compte du fait que cette requête utilise des données stockées dans deux tables distinctes : `ratings` et `movies`. Rappelez-vous que, tant qu'une table a une clé étrangère qui correspond à une colonne d'une autre table, vous pouvez combiner deux tables à l'aide du mot-clé `JOIN` de SQL. Pour utiliser le mot-clé `JOIN`, vous devez spécifier la table que vous souhaitez joindre et la colonne par laquelle le faire.

    SELECT colonne0
    FROM table0
    JOIN table1 ON table0.colonne1 = table1.colonne2

### Lister tous les films sortis en 2010 et leurs notes, par ordre décroissant de note

Rappelez-vous que `ORDER BY` ne doit pas toujours trier par ordre croissant. Vous pouvez spécifier que vos résultats soient triés par ordre _décroissant_ en ajoutant `DESC`.

    ...
    ORDER BY colonne DESC ;

### Énumérez les noms de toutes les personnes ayant joué dans Toy Story

Lorsque vous voyez une requête plus complexe comme celle-ci, il est préférable de la diviser en morceaux plus petits. En fin de compte, votre requête devrait aboutir à une liste de noms, comme indiqué ci-dessous.

 -- Sélectionner les noms
SELECT name
FROM people
WHERE ...

Mais quelle est la meilleure façon de trouver les noms de ceux qui ont joué dans Toy Story ? Observez que la table `people` n’a pas cette information (mais la table `stars` peut l’avoir !). En effet, la table `stars` combine deux colonnes, `person_id` et `movie_id` : toute personne avec un `person_id` associé à l’`id` du film Toy Story a joué dans Toy Story.

 -- Sélectionner les noms
SELECT name
FROM people
WHERE ...

 -- Sélectionner les ID de personne
SELECT person_id
FROM stars
WHERE movie_id = ...

Une étape naturelle suivante consiste donc à trouver l’ID du film Toy Story.

 -- Sélectionner les noms
SELECT name
FROM people
WHERE ...

 -- Sélectionner les ID de personne
SELECT person_id
FROM stars
WHERE movie_id = ...

 -- Trouver l’ID de Toy Story
SELECT id
FROM movies
WHERE title = 'Toy Story' ;

Bien sûr, vous avez actuellement écrit trois requêtes _distinctes_. Mais remarquez que certaines requêtes (les deux premières) seraient complètes en incluant les résultats de la requête directement en dessous d’elles. Le processus d’élaboration d’une requête qui dépend des résultats d’une « sous-requête » est appelé requêtes « imbriquées ». C’est un bon indice, mais voici une façon d’imbriquer les requêtes ci-dessus !

 -- Sélectionner les noms
SELECT name
FROM people
WHERE id IN
(
 -- Sélectionner les ID de personne
SELECT person_id
FROM stars
WHERE movie_id = (

 -- Trouver l’ID de Toy Story
SELECT id
FROM movies
WHERE title = 'Toy Story'
)
) ;

### Énumérez les noms de toutes les personnes ayant joué dans un film sorti en 2004, triés par année de naissance

Observez que cette requête, comme la précédente, vous oblige à utiliser des données de plusieurs tables. Rappelez-vous que vous pouvez « imbriquer » des requêtes en SQL, ce qui vous permet de décomposer une requête plus grande en plus petites. Vous pourriez peut-être écrire des requêtes pour ...

1. Trouver les ID des films sortis en 2004
2. Trouver les ID des personnes ayant joué dans ces films
3. Trouver les noms des personnes avec ces ID de personnes

Ensuite, essayez d’imbriquer ces requêtes pour arriver à une requête unique qui renvoie toutes les personnes ayant joué dans un film sorti en 2004. Réfléchissez à la façon dont vous pourriez ensuite classer les résultats de votre requête.

### Énumérez les noms de toutes les personnes ayant réalisé un film avec une note d’au moins 9,0

Observez que cette requête, comme la précédente, vous oblige à utiliser des données de plusieurs tables. Rappelez-vous que vous pouvez « imbriquer » des requêtes en SQL, ce qui vous permet de décomposer une requête plus grande en plus petites. Vous pourriez peut-être écrire des requêtes pour ...

1. Trouver les ID des films avec une note d’au moins 9,0
2. Trouver les ID des personnes qui ont réalisé ces films
3. Trouver les noms des personnes avec ces ID de personnes

Ensuite, essayez d’imbriquer ces requêtes pour arriver à une requête unique qui renvoie les noms de toutes les personnes ayant réalisé un film avec une note d’au moins 9,0.

### Énumérez les titres des cinq films les mieux notés (dans l’ordre) dans lesquels Chadwick Boseman a joué, en commençant par le mieux noté

Observez que cette requête, comme la précédente, vous oblige à utiliser des données de plusieurs tables. Rappelez-vous que vous pouvez « imbriquer » des requêtes en SQL, ce qui vous permet de décomposer une requête plus grande en plus petites. Vous pourriez peut-être écrire des requêtes pour ...

1. Trouver l’ID de Chadwick Boseman
2. Trouver les ID des films associés à l’ID de Chadwick Boseman
3. Trouver les titres des films avec ces ID de films

Ensuite, essayez d’imbriquer ces requêtes pour arriver à une requête unique qui renvoie les titres des films de Chadwick Boseman.

À partir de là, vous devrez déterminer les notes de ces titres et trier ces titres par note, dans l’ordre décroissant. Réfléchissez à la façon dont vous pourriez combiner une table pertinente (probablement `notes` !) et trier les résultats par une colonne pertinente.

Enfin, consultez le mot-clé de SQL [`LIMIT`](https://www.sqlitetutorial.net/sqlite-limit/) qui renverra les \\(n\\) premières lignes d’une requête.

### Listez les titres de tous les films dans lesquels à la fois Bradley Cooper et Jennifer Lawrence ont joué

Notez que cette requête, comme la précédente, vous demande d'utiliser des données depuis plusieurs tables. Rappelez-vous que vous pouvez "imbriquer" des requêtes en SQL, ce qui vous permet de diviser une longue requête en plus petites. Vous pouvez peut-être écrire des requêtes pour :

1. Trouver l'ID de Bradley Cooper
2. Trouver l'ID de Jennifer Lawrence
3. Trouver les ID des films associés à l'ID de Bradley Cooper
4. Trouver les ID des films associés à l'ID de Jennifer Lawrence
5. Trouver les titres de films à partir des ID de films associés à _à la fois_ Bradley Cooper et Jennifer Lawrence

Puis, essayez d'imbriquer ces requêtes pour parvenir à une seule requête qui renvoie les films dans lesquels ont joué à la fois Bradley Cooper et Jennifer Lawrence.

Rappelez-vous que vous pouvez construire des conditions complexes en SQL en utilisant `AND` ou `OR`.

### Listez les noms de toutes les personnes qui ont joué dans un film dans lequel Kevin Bacon a également joué

Notez que cette requête, comme la précédente, vous demande d'utiliser des données depuis plusieurs tables. Rappelez-vous que vous pouvez "imbriquer" des requêtes en SQL, ce qui vous permet de diviser une longue requête en plus petites. Vous pouvez peut-être écrire des requêtes pour :

1. Trouver l'ID de Kevin Bacon (celui né en 1958 !)
2. Trouver les ID des films associés à l'ID de Kevin Bacon
3. Trouver les ID des personnes associées à ces ID de films
4. Trouver les noms des personnes avec ces ID de personnes

Puis, essayez d'imbriquer ces requêtes pour parvenir à une seule requête qui renvoie les noms de toutes les personnes qui ont joué dans un film dans lequel a également joué Kevin Bacon. **Gardez à l'esprit que vous voudrez exclure Kevin Bacon lui-même des résultats !**

## Procédure détaillée

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/v5_A3giDlQs?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Utilisation

Pour tester vos requêtes dans VS Code, vous pouvez interroger la base de données en exécutant

    $ cat nom_fichier.sql | sqlite3 .movies.db

où `nom_fichier.sql` est le fichier contenant votre requête SQL.

Vous pouvez aussi exécuter

    $ cat nom_fichier.sql | sqlite3 .movies.db > sortie.txt

pour rediriger le résultat de la requête vers un fichier texte appelé `sortie.txt`. (Cela peut être utile pour vérifier le nombre de lignes renvoyées par votre requête !)

## Comment tester

Bien que `check50` soit disponible pour ce problème, nous vous encourageons à tester vous-même votre code pour chacun des éléments suivants. Vous pouvez exécuter `sqlite3 .movies.db` pour exécuter des requêtes supplémentaires sur la base de données pour vous assurer que votre résultat est correct.

Si vous utilisez la base de données `movies.db` fournie dans la distribution de cet ensemble de problèmes, vous devriez constater que

- L'exécution de `1.sql` renvoie une table avec 1 colonne et 10 276 lignes.
- L'exécution de `2.sql` renvoie une table avec 1 colonne et 1 ligne.
- L'exécution de `3.sql` renvoie une table avec 1 colonne et 110 014 lignes.
- L'exécution de `4.sql` renvoie une table avec 1 colonne et 1 ligne.
- L'exécution de `5.sql` renvoie une table avec 2 colonnes et 11 lignes.
- L'exécution de `6.sql` renvoie une table avec 1 colonne et 1 ligne.
- L'exécution de `7.sql` renvoie une table avec 2 colonnes et 7 192 lignes.
- L'exécution de `8.sql` renvoie une table avec 1 colonne et 4 lignes.
- L'exécution de `9.sql` renvoie une table avec 1 colonne et 19 325 lignes.
- L'exécution de `10.sql` renvoie une table avec 1 colonne et 3 854 lignes.
- L'exécution de `11.sql` renvoie une table avec 1 colonne et 5 lignes.
- L'exécution de `12.sql` renvoie une table avec 1 colonne et 4 lignes.
- L'exécution de `13.sql` renvoie une table avec 1 colonne et 182 lignes.

Notez que le nombre de lignes n'inclut pas les lignes d'en-tête qui affichent uniquement les noms de colonnes.

Si votre requête renvoie un nombre de lignes légèrement différent de la sortie attendue, assurez-vous que vous gérez correctement les doublons ! Pour les requêtes qui demandent une liste de noms, aucune personne ne doit être listée deux fois, mais deux personnes différentes portant le même nom doivent chacune être listées.

### Exactitude

    check50 cs50/problems/2024/x/movies

## Comment soumettre

    submit50 cs50/problems/2024/x/movies

## Remerciements

Informations fournies par IMDb ([imdb.com](https://www.imdb.com)). Utilisées avec autorisation.

