# Fiftyville

## Problème à résoudre

Le canard de CS50 a été volé ! La ville de Fiftyville fait appel à vous pour résoudre le mystère du vol du canard. Les autorités pensent que le voleur a volé le canard, puis, peu après, s'est envolé de la ville avec l'aide d'un complice. Votre but est d'identifier :

- Qui est le voleur ?
- Vers quelle ville le voleur s'est-il échappé ?
- Qui est le complice du voleur qui l'a aidé à s'échapper

Tout ce que vous savez, c'est que le vol a eu lieu le 28 juillet 2023 et qu'il a eu lieu sur Humphrey Street.

Comment allez-vous résoudre ce mystère ? Les autorités de Fiftyville ont pris certains des documents de la ville concernant l'époque du vol et ont préparé une base de données SQLite pour vous, `fiftyville.db`, qui contient des tableaux de données de la ville. Vous pouvez interroger cette table à l'aide de requêtes SQL `SELECT` pour accéder aux données qui vous intéressent. En utilisant uniquement les informations de la base de données, votre tâche consiste à résoudre le mystère.

## Démo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-YgI5fyTP939jINCZm7l3o7WCY" src="https://asciinema.org/a/YgI5fyTP939jINCZm7l3o7WCY.js"></script>

## Pour commencer

Pour ce problème, vous utiliserez une base de données fournie par le personnel de CS50.

Connectez-vous à [cs50.dev](https://cs50.dev/), cliquez sur votre fenêtre de terminal et exécutez `cd` seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ce qui suit :

    $

Puis, exécutez

    wget https://cdn.cs50.net/2023/fall/psets/7/fiftyville.zip

afin de télécharger un fichier ZIP appelé `fiftyville.zip` dans votre espace de code.

Puis, exécutez

    unzip fiftyville.zip

pour créer un dossier appelé `fiftyville`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm fiftyville.zip

et répondre par « y » suivi de la touche Entrée à l'invite pour supprimer le fichier ZIP téléchargé.

Maintenant, tapez

    cd fiftyville

suivi de la touche Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit :

    fiftyville/ $

Exécutez `ls` seul et vous devriez voir quelques fichiers :

    answers.txt  fiftyville.db  log.sql

Si vous rencontrez des problèmes, suivez à nouveau les mêmes étapes et voyez si vous pouvez déterminer où vous vous êtes trompé !

## Spécification

Pour ce problème, ce qui importe autant que la résolution du mystère en lui-même, c'est le processus que vous utilisez pour résoudre le mystère. Dans `log.sql`, conservez un journal de toutes les requêtes SQL que vous exécutez sur la base de données. Au-dessus de chaque requête, étiquetez-la avec un commentaire (en SQL, les commentaires sont toutes les lignes qui commencent par `--`) décrivant pourquoi vous exécutez la requête et/ou quelles informations vous espérez obtenir de cette requête particulière. Vous pouvez utiliser des commentaires dans le fichier journal pour ajouter des notes supplémentaires sur votre processus de réflexion pendant que vous résolvez le mystère : en fin de compte, ce fichier doit servir de preuve du processus que vous avez utilisé pour identifier le voleur !

Lorsque vous écrirez vos requêtes, vous remarquerez peut-être que certaines d'entre elles peuvent devenir assez complexes. Pour aider à garder vos requêtes lisibles, consultez les principes d'un bon style sur [sqlstyle.guide](https://www.sqlstyle.guide). La section [indentation](https://www.sqlstyle.guide/#indentation) peut être particulièrement utile !

Une fois que vous avez résolu le mystère, remplissez chacune des lignes dans `answers.txt` en indiquant le nom du voleur, la ville vers laquelle le voleur s'est échappé et le nom du complice du voleur qui l'a aidé à s'échapper de la ville. (Assurez-vous de ne modifier aucun texte existant dans le fichier ou d'y ajouter d'autres lignes !)

En fin de compte, vous devez soumettre vos fichiers `log.sql` et `answers.txt`.

## Procédure

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/YHhgEoJMDnU?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Conseils

- Exécutez `sqlite3 fiftyville.db` pour commencer à exécuter des requêtes sur la base de données.
  - Lors de l'exécution de `sqlite3`, l'exécution de `.tables` listera tous les tableaux de la base de données.
  - Lors de l'exécution de `sqlite3`, l'exécution de `.schema NOM_TABLE`, où `NOM_TABLE` est le nom d'une table dans la base de données, vous montrera la commande `CREATE TABLE` utilisée pour créer la table. Cela peut être utile pour connaître les colonnes à interroger !
- Vous trouverez peut-être utile de commencer par le tableau `crime_scene_reports`. Commencez par rechercher un rapport de scène de crime qui correspond à la date et au lieu du crime.
- Consultez [cette référence de mots-clés SQL](https://www.w3schools.com/sql/sql_ref_keywords.asp) pour une syntaxe SQL qui peut être utile !

## Comment tester

### Correctness

    check50 cs50/problems/2024/x/fiftyville

## Comment soumettre

    submit50 cs50/problems/2024/x/fiftyville

## Remerciements

Inspiré d'une autre affaire chez [SQL City](https://mystery.knightlab.com/).