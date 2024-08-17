# Chansons

![Logo Spotify Wrapped '22](https://cs50.harvard.edu/x/2024/psets/7/songs/wrapped.png)

## Problème à résoudre

Rédiger des requêtes SQL pour répondre à des questions sur une base de données contenant les 100 chansons les plus écoutées sur [Spotify](https://en.wikipedia.org/wiki/Spotify) en 2018.

## Démonstration

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-DsiNSGFrMq2J6t9aDYhIQUQHy" src="https://asciinema.org/a/DsiNSGFrMq2J6t9aDYhIQUQHy.js"></script>

## Mise en place

Pour ce problème, vous utiliserez une base de données mise à votre disposition par l'équipe de CS50.

Ouvrir [VS Code](https://cs50.dev/).

Commencer par cliquer à l'intérieur de la fenêtre de votre terminal, puis exécuter `cd` seul. Vous devriez constater que son « prompt » ressemble à celui ci-dessous.

    $

Cliquer à l'intérieur de la fenêtre de terminal, puis exécuter

    wget https://cdn.cs50.net/2023/fall/psets/7/songs.zip

suivi d'Entrée pour télécharger un fichier ZIP nommé `songs.zip` dans votre espace de codage. Veillez à ne pas négliger l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs !

Exécuter maintenant

    unzip songs.zip

pour créer un dossier nommé `songs`. Vous n'avez plus besoin du fichier ZIP, donc vous pouvez exécuter

    rm songs.zip

et répondre par « y » suivi d'Entrée à l'invite pour supprimer le fichier ZIP que vous avez téléchargé.

Saisir ensuite

    cd songs

suivi d'Entrée pour vous déplacer dans (c.-à-d. ouvrir) ce répertoire. Votre message devrait maintenant ressembler à celui ci-dessous.

    songs/ $

Si tout s'est bien passé, vous devriez exécuter

    ls

et vous devriez voir 8 fichiers .sql, `songs.db` et `answers.txt`.

Si vous rencontrez des problèmes, suivez à nouveau les mêmes étapes et essayez de déterminer où vous vous êtes trompé !

## Compréhension

Nous vous fournissons un fichier nommé `songs.db`, une base de données SQLite qui stocke des données provenant de [Spotify](https://developer.spotify.com/documentation/web-api/) sur les chansons et leurs artistes. Cet ensemble de données contient les 100 chansons les plus écoutées sur Spotify en 2018. Dans une fenêtre de terminal, exécuter `sqlite3 songs.db` afin de pouvoir commencer à exécuter des requêtes sur la base de données.

Tout d'abord, lorsque `sqlite3` vous demande de fournir une requête, saisir `.schema` et appuyer sur Entrée. Cela affichera les instructions `CREATE TABLE` qui ont été utilisées pour générer chacune des tables dans la base de données. En examinant ces instructions, vous pouvez identifier les colonnes présentes dans chaque table.

Remarquer que chaque `artiste` a un `id` et un `name`. Noter également que chaque chanson a un `name`, un `artist_id` (correspondant à l'`id` de l'artiste de la chanson), ainsi que des valeurs pour la dansabilité, l'énergie, la tonalité, le volume sonore, la présence vocale (présence de paroles dans une piste), la valence, le tempo et la durée de la chanson (mesurée en millisecondes).

Le défi qui vous attend consiste à rédiger des requêtes SQL pour répondre à différentes questions en sélectionnant des données dans une ou plusieurs de ces tables. Après cela, vous réfléchirez à la manière dont Spotify pourrait utiliser ces mêmes données dans sa campagne annuelle [Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) pour caractériser les habitudes des auditeurs.

## Détails d’implémentation

Pour chacun des problèmes suivants, vous devez rédiger une requête SQL unique qui produit les résultats spécifiés par chaque problème. Votre réponse doit prendre la forme d'une requête SQL unique, bien que vous puissiez imbriquer d'autres requêtes à l'intérieur de votre requête. Vous ne **devez pas** faire d'hypothèses sur les `id` de chansons ou d'artistes particuliers : vos requêtes doivent être exactes même si l'`id` d'une chanson ou d'une personne en particulier était différent. Enfin, chaque requête ne doit renvoyer que les données nécessaires pour répondre à la question : si le problème vous demande uniquement de générer les noms de chansons, par exemple, votre requête ne doit pas également générer le tempo de chaque chanson.

1. Dans `1.sql`, rédiger une requête SQL pour lister les noms de toutes les chansons de la base de données.
    - Votre requête doit générer une table avec une seule colonne pour le nom de chaque chanson.
2. Dans `2.sql`, rédiger une requête SQL pour lister les noms de toutes les chansons par ordre croissant de tempo.
    - Votre requête doit générer une table avec une seule colonne pour le nom de chaque chanson.
3. Dans `3.sql`, rédiger une requête SQL pour lister les noms des 5 chansons les plus longues, par ordre décroissant de longueur.
    - Votre requête doit générer une table avec une seule colonne pour le nom de chaque chanson.
4. Dans `4.sql`, rédiger une requête SQL qui liste les noms de toutes les chansons dont la dansabilité, l'énergie et la valence sont supérieures à 0,75.
    - Votre requête doit générer une table avec une seule colonne pour le nom de chaque chanson.
5. Dans `5.sql`, rédiger une requête SQL qui renvoie l'énergie moyenne de toutes les chansons.
    - Votre requête doit générer une table avec une seule colonne et une seule ligne contenant l'énergie moyenne.
6. Dans `6.sql`, rédiger une requête SQL qui liste les noms des chansons interprétées par Post Malone.
    - Votre requête doit générer une table avec une seule colonne pour le nom de chaque chanson.
    - Vous ne devez faire aucune hypothèse sur l'`artist_id` de Post Malone.
7. Dans `7.sql`, rédiger une requête SQL qui renvoie l'énergie moyenne des chansons interprétées par Drake.
    - Votre requête doit générer une table avec une seule colonne et une seule ligne contenant l'énergie moyenne.
    - Vous ne devez faire aucune hypothèse sur l'`artist_id` de Drake.
8. Dans `8.sql`, rédiger une requête SQL qui liste les noms des chansons qui présentent d'autres artistes.
    - Les chansons qui présentent d'autres artistes incluront « feat. » dans le nom de la chanson.
    - Votre requête doit générer une table avec une seule colonne pour le nom de chaque chanson.

## Indices

Consultez [cette référence de mots-clés SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) pour découvrir une syntaxe SQL qui pourrait vous être utile !

Cliquer sur les bascules ci-dessous pour lire quelques conseils !

### Lister les noms de toutes les chansons de la base de données

Rappelons que, pour sélectionner toutes les valeurs dans une colonne d'une table, vous pouvez utiliser le mot-clé `SELECT` de SQL. `SELECT` est suivi de la ou des colonnes que vous souhaitez sélectionner, qui est à son tour suivi de `FROM table` où `table` est le nom de la table dans laquelle vous souhaitez sélectionner.

Dans `1.sql`, essayez ensuite d'écrire ce qui suit :

    -- Toutes les chansons dans la base de données.
    SELECT name
    FROM songs;

### Lister les noms de toutes les chansons par ordre croissant de tempo

Rappelons que SQL a un mot-clé `ORDER BY`, par lequel vous pouvez trier les résultats de votre requête par la valeur dans une certaine colonne. Par exemple, `ORDER BY tempo` triera les résultats par la colonne `tempo`.

Dans `2.sql`, essayez ensuite d'écrire ce qui suit :

    -- Toutes les chansons par ordre croissant de tempo.
    SELECT name
    FROM songs
    ORDER BY tempo;

### Lister les noms des 5 chansons les plus longues, par ordre décroissant de longueur

Rappelons que `ORDER BY` ne doit pas toujours trier par ordre croissant. Vous pouvez spécifier que vos résultats soient triés par ordre _décroissant_ en ajoutant `DESC`. Par exemple, `ORDER BY duration_ms DESC` listera les résultats par ordre décroissant, par durée.

Et rappelez-vous également que `LIMIT n` peut spécifier que vous ne voulez que les premières \\(n\\) lignes qui correspondent à une requête spécifique. Par exemple, `LIMIT 5` ne renverra que les cinq premiers résultats de la requête.

Dans `3.sql`, essayez ensuite d'écrire ce qui suit :

    -- Les noms des 5 chansons les plus longues, par ordre décroissant de longueur.
    SELECT name
    FROM songs
    ORDER BY duration_

### Énumérez les noms des morceaux dont la valeur de danceability, d'énergie et de valence est supérieure à 0,75

N'oubliez pas que vous pouvez filtrer les résultats en SQL avec les clauses `WHERE`, qui sont suivies d'une condition qui teste généralement les valeurs dans les colonnes d'une ligne.

N'oubliez pas non plus que les opérateurs SQL fonctionnent à peu près de la même manière que ceux de C. Par exemple, `>` prend la valeur « true » lorsque la valeur de gauche est supérieure à la valeur de droite. Vous pouvez chaîner ces expressions ensemble, en utilisant `AND` ou `OR`, pour former une condition plus grande.

Dans `4.sql`, essayez donc d'écrire ce qui suit :

    -- Les noms des morceaux dont la valeur de danceability, d'énergie et de valence est supérieure à 0,75.
    SELECT name
    FROM songs
    WHERE danceability > 0,75 AND energy > 0,75 AND valence > 0,75 ;

### Trouvez l'énergie moyenne de tous les morceaux

N'oubliez pas que SQL prend en charge des mots-clés non seulement pour sélectionner des lignes particulières, mais aussi pour _agréger_ les données dans ces lignes. En particulier, vous pourriez trouver le mot-clé `AVG` (pour calculer les moyennes) utile. Pour agréger les résultats d'une colonne, appliquez simplement la fonction d'agrégation à cette colonne. Par exemple, `SELECT AVG(energy)` trouvera la moyenne des valeurs dans la colonne energy pour la requête donnée.

Dans `5.sql`, essayez donc d'écrire ce qui suit :

    -- L'énergie moyenne de tous les morceaux.
    SELECT AVG(energy)
    FROM songs ;

### Énumérez les noms des morceaux de Post Malone

Remarquez que si vous exécutez `.schema songs` dans votre invite sqlite, la table `songs` contient les noms des morceaux mais pas les noms des artistes ! Au lieu de cela, `songs` possède une colonne `artist_id`. Pour lister les noms des morceaux de Post Malone, vous devez d'abord identifier l'ID d'artiste de Post Malone.

    -- Identifier l'ID d'artiste de Post Malone
    SELECT id
    FROM artists
    WHERE name = 'Post Malone' ;

Cette requête renvoie 54. Maintenant, vous pouvez interroger la table `songs` pour n'importe quel morceau avec l'ID de Post Malone.

    SELECT name
    FROM songs
    WHERE artist_id = 54 ;

Mais, selon les spécifications, vous devez veiller à ne pas présumer la connaissance des ID. Vous pouvez améliorer la conception de cette requête en _imbricant_ vos deux requêtes.

Dans `6.sql`, essayez donc d'écrire ce qui suit :

    -- Les noms des morceaux de Post Malone.
    SELECT name
    FROM songs
    WHERE artist_id =
    (
        SELECT id
        FROM artists
        WHERE name = 'Post Malone'
    ) ;

### Trouvez l'énergie moyenne des morceaux de Drake

Notez que, comme pour la requête précédente, vous devrez combiner plusieurs tables pour exécuter cette requête avec succès. Vous pouvez à nouveau utiliser des sous-requêtes imbriquées, mais envisagez également une autre approche !

N'oubliez pas que vous pouvez utiliser le mot-clé `JOIN` de SQL pour combiner plusieurs tables en une seule, à condition de spécifier quelles colonnes dans ces tables doivent correspondre en fin de compte. Par exemple, la requête suivante joint les tables `songs` et `artists`, indiquant que la colonne `artist_id` dans la table `songs` et la colonne `id` dans la table `artists` doivent correspondre :

    SELECT *
    FROM songs
    JOIN artists ON songs.artist_id = artists.id

Une fois ces deux tables combinées, il suffit de filtrer votre sélection pour trouver l'énergie moyenne des morceaux de Drake.

Dans `7.sql`, essayez donc d'écrire ce qui suit :

    -- L'énergie moyenne des morceaux de Drake
    SELECT AVG(energy)
    FROM songs
    JOIN artists ON songs.artist_id = artists.id
    WHERE artists.name = 'Drake' ;

### Énumérez les noms des morceaux qui présentent d'autres artistes

Pour cette requête, notez que les morceaux qui présentent d'autres artistes contiennent généralement une mention « feat. » dans leur titre. N'oubliez pas que le mot-clé `LIKE` de SQL peut être utilisé pour faire correspondre des chaînes avec certaines expressions (comme « feat. » !). Pour ce faire, vous pouvez utiliser `% `: un caractère générique qui correspond à n'importe quelle séquence de caractères.

Dans `8.sql`, essayez donc d'écrire ce qui suit :

    -- Les noms des morceaux qui présentent d'autres artistes.
    SELECT name
    FROM songs
    WHERE name LIKE '%feat.%' ;

## Déroulement

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/wgKPUd_95AA"></iframe>

<details><summary>Vous ne savez pas comment résoudre ?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/7hydPL9ZswE"></iframe></details>

## Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) est une fonctionnalité qui présente aux utilisateurs de Spotify leurs 100 chansons les plus écoutées de l'année écoulée. En 2021, Spotify Wrapped a calculé une [« Audio Aura »](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) pour chaque utilisateur, une « lecture de [leurs] deux humeurs les plus marquantes dictées par [leurs] meilleures chansons et artistes de l'année ». Supposons que Spotify détermine une aura audio en examinant l'énergie moyenne, la valence et la danceability des 100 meilleures chansons d'une personne au cours de l'année écoulée. Dans `answers.txt`, réfléchissez aux questions suivantes :

- Si `songs.db` contient les 100 meilleures chansons d'un auditeur de 2018, comment caractériseriez-vous son aura audio ?
- Donnez une hypothèse sur les raisons pour lesquelles la façon dont vous avez calculé cette aura pourrait _ne pas_ être très représentative de l'auditeur. Quelles meilleures façons de calculer cette aura proposeriez-vous ?

Assurez-vous de soumettre `answers.txt` avec chacun de vos fichiers `.sql !`

## Comment tester

### Correction

    check50 cs50/problems/2024/x/songs

## Comment soumettre

    submit50 cs50/problems/2024/x/songs

## Remerciements

Ensemble de données de [Kaggle](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018).

