# Héritage

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/xfZhb6lmxjk?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Problème à résoudre

Le groupe sanguin d'une personne est déterminé par deux allèles (c'est-à-dire différentes formes d'un gène). Les trois allèles possibles sont A, B et O, dont chaque personne possède deux (éventuellement le même, éventuellement différent). Chaque parent d'un enfant transmet aléatoirement l'un de ses deux allèles de groupe sanguin à son enfant. Les combinaisons possibles de groupes sanguins sont donc : OO, OA, OB, AO, AA, AB, BO, BA et BB.

Par exemple, si un parent a le groupe sanguin AO et l'autre parent a le groupe sanguin BB, alors les groupes sanguins possibles de l'enfant seraient AB et OB, selon l'allèle reçu de chaque parent. De même, si un parent a le groupe sanguin AO et l'autre OB, alors les groupes sanguins possibles de l'enfant seraient AO, OB, AB et OO.

Dans un fichier appelé `inheritance.c` dans un dossier appelé `inheritance`, simulez l'héritage des groupes sanguins pour chaque membre d'une famille.

## Démo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-J9DnbdokgIAjWUbzC2CBqP22N" src="https://asciinema.org/a/J9DnbdokgIAjWUbzC2CBqP22N.js"></script>

## Code de distribution

Pour ce problème, vous étendez les fonctionnalités du code fourni par le personnel de CS50.

Connectez-vous sur [cs50.dev](https://cs50.dev/), cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à celle-ci :

    $

Exécutez ensuite

    wget https://cdn.cs50.net/2023/fall/psets/5/inheritance.zip

afin de télécharger un ZIP appelé `inheritance.zip` dans votre espace de codes.

Ensuite, exécutez

    unzip inheritance.zip

pour créer un dossier appelé `inheritance`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm inheritance.zip

et répondez par « y » suivi de Entrée à l'invite pour supprimer le fichier ZIP que vous avez téléchargé.

Tapez maintenant

    cd inheritance

suivi de Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à celle-ci.

    inheritance/ $

Exécutez `ls` tout seul, et vous devriez voir et voir un fichier nommé `inheritance.c`.

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et essayez de déterminer où vous vous êtes trompé !

## Détails de mise en œuvre

Terminez l'implémentation de `inheritance.c`, de sorte qu'il crée une famille d'une taille de génération spécifiée et attribue des allèles de groupe sanguin à chaque membre de la famille. L'allèle le plus ancien se voit attribuer des allèles de manière aléatoire.

- La fonction `create_family` prend un entier (`generations`) en entrée et doit allouer (comme via `malloc`) une `person` pour chaque membre de la famille de ce nombre de générations, renvoyant un pointeur vers la `person` dans la plus jeune génération.
  - Par exemple, `create_family(3)` doit renvoyer un pointeur vers une personne ayant deux parents, chaque parent ayant également deux parents.
  - Chaque `person` doit se voir attribuer des `allèles`. La génération la plus ancienne doit avoir des allèles choisis au hasard (comme en appelant la fonction `random_allele`), et les générations plus jeunes doivent hériter d'un allèle (choisi au hasard) de chaque parent.
  - Chaque `person` doit se voir attribuer des `parents`. La génération la plus ancienne doit avoir les deux `parents` définis sur `NULL`, et les générations plus jeunes doivent avoir des `parents` comme tableau de deux pointeurs, chacun pointant vers une structure `person` différente.

## Conseils

### Comprendre le code dans `inheritance.c`

Jetez un œil au code de distribution dans `inheritance.c`.

Remarquez la définition d'un type appelé `person`. Chaque personne possède un tableau de deux `parents`, chacun étant un pointeur vers une autre structure `person`. Chaque personne possède également un tableau de deux `allèles`, chacun étant un `char` (soit `'A'`, `'B'`, soit `'O'`).

    // Chaque personne a deux parents et deux allèles
    typedef struct person
    {
        struct person *parents[2];
        char alleles[2];
    }
    person;

Maintenant, jetez un œil à la fonction `main`. La fonction commence par « amorcer » (c'est-à-dire fournir une entrée initiale à) un générateur de nombres aléatoires, que nous utiliserons plus tard pour générer des allèles aléatoires.

    // Initialiser le générateur de nombres aléatoires
    srand(time(0));

La fonction `main` appelle ensuite la fonction `create_family` pour simuler la création de structures `person` pour une famille de 3 générations (c'est-à-dire une personne, ses parents et ses grands-parents).

    // Créer une nouvelle famille avec trois générations
    person *p = create_family(GENERATIONS);

Nous appelons ensuite `print_family` pour imprimer chacun de ces membres de la famille et leurs groupes sanguins.

    // Imprimer l'arbre généalogique des groupes sanguins
    print_family(p, 0);

Enfin, la fonction appelle `free_family` pour `libérer` toute mémoire précédemment allouée avec `malloc`.

    // Libérer la mémoire
    free_family(p);

Les fonctions `create_family` et `free_family` sont à vous d'écrire!

### Compléter la fonction `create_family`

La fonction `create_family` doit renvoyer un pointeur vers une `personne` qui a hérité son groupe sanguin du nombre de `générations` donné en entrée.

- Notez d'abord que ce problème offre une bonne opportunité de récursivité.
  - Pour déterminer le groupe sanguin de la personne actuelle, vous devez d'abord déterminer les groupes sanguins de ses parents.
  - Pour déterminer les groupes sanguins de ces parents, vous devez d'abord déterminer les groupes sanguins de leurs parents. Et ainsi de suite jusqu'à ce que vous atteigniez la dernière génération que vous souhaitez simuler.

Pour résoudre ce problème, vous trouverez plusieurs TODO dans le code de distribution.

Tout d'abord, vous devez allouer de la mémoire pour une nouvelle personne. Rappelez-vous que vous pouvez utiliser `malloc` pour allouer de la mémoire et `sizeof(person)` pour obtenir le nombre d'octets à allouer.

    // Allouer de la mémoire pour une nouvelle personne
    person *new_person = malloc(sizeof(person));

Ensuite, vous devez vérifier s'il reste des générations à créer, c'est-à-dire si `générations > 1`.

Si `générations > 1`, alors il y a encore des générations qui doivent être allouées. Nous avons déjà créé deux nouveaux parents, `parent0` et `parent1`, en appelant récursivement `create_family`. Votre fonction `create_family` doit ensuite définir les pointeurs parents de la nouvelle personne que vous avez créée. Enfin, attribuez les deux `allèles` à la nouvelle personne en choisissant aléatoirement un allèle de chaque parent.

- N'oubliez pas que pour accéder à une variable via un pointeur, vous pouvez utiliser la notation fléchée. Par exemple, si `p` est un pointeur vers une personne, alors un pointeur vers le premier parent de cette personne peut être accédé par `p->parents[0]`.
- Vous pouvez trouver la fonction `rand()` utile pour attribuer aléatoirement des allèles. Cette fonction renvoie un entier compris entre `0` et `RAND_MAX`, ou `32767`. En particulier, pour générer un nombre pseudo-aléatoire qui vaut soit `0` soit `1`, vous pouvez utiliser l'expression `rand() % 2`.

  // Créer deux nouveaux parents pour la personne actuelle en appelant récursivement create_family
  person *parent0 = create_family(générations - 1);
  person *parent1 = create_family(générations - 1);

  // Définir des pointeurs parents pour la personne actuelle
  new_person->parents[0] = parent0;
  new_person->parents[1] = parent1;

  // Attribuer aléatoirement les allèles de la personne actuelle en fonction des allèles de ses parents
  new_person->allèles[0] = parent0->allèles[rand() % 2];
  new_person->allèles[1] = parent1->allèles[rand() % 2];

Supposons qu'il n'y ait plus de générations à simuler. C'est-à-dire que `générations == 1`. Si c'est le cas, il n'y aura pas de données parents pour cette personne. Les deux parents de votre nouvelle personne doivent être définis sur `NULL` et chaque `allèle` doit être généré aléatoirement.

    // Définir des pointeurs parents sur NULL
    new_person->parents[0] = NULL;
    new_person->parents[1] = NULL;

    // Attribuer aléatoirement des allèles
    new_person->allèles[0] = random_allele();
    new_person->allèles[1] = random_allele();

Enfin, votre fonction doit renvoyer un pointeur vers la `personne` qui a été allouée.

    // Retourner une personne nouvellement créée
    return new_person;

### Compléter la fonction `free_family`

La fonction `free_family` doit accepter en entrée un pointeur vers une `personne`, libérer de la mémoire pour cette personne, puis libérer récursivement de la mémoire pour tous ses ancêtres.

- Puisqu'il s'agit d'une fonction récursive, vous devez d'abord gérer le cas de base. Si l'entrée de la fonction est `NULL`, alors il n'y a rien à libérer, votre fonction peut donc renvoyer immédiatement.
- Sinon, vous devez `free` récursivement les deux parents de la personne avant de `free` l'enfant.

Ce qui suit est un indice, mais voici comment faire !

    // Libérer `p` et tous les ancêtres de `p`.
    void free_family(person *p)
    {
        // Gérer le cas de base
        if (p == NULL)
        {
            return;
        }

        // Libérer les parents récursivement
        free_family(p->parents[0]);
        free_family(p->parents[1]);

        // Libérer l'enfant
        free(p);
    }

### Procédure pas à pas

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/9p7ddI3ozTY?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

<details><summary>Vous ne savez pas comment résoudre ?</summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/H7LULatPwcQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

## Comment tester

Lors de l'exécution de `./inheritance`, votre programme doit respecter les règles décrites dans le contexte. L'enfant doit avoir deux allèles, un de chaque parent. Les parents doivent chacun avoir deux allèles, un de chacun de leurs parents.

Par exemple, dans l'exemple ci-dessous, l'enfant de génération 0 a reçu un allèle O des deux parents de génération 1. Le premier parent a reçu un A du premier grand-parent et un O du deuxième grand-parent. De même, le deuxième parent a reçu un O et un B de ses grands-parents.

    $ ./inheritance
    Enfant (génération 0) : groupe sanguin OO
        Parent (génération 1) : groupe sanguin AO
            Grand-parent (génération 2) : groupe sanguin OA
            Grand-parent (génération 2) : groupe sanguin BO
        Parent (génération 1) : groupe sanguin OB
            Grand-parent (génération 2) : groupe sanguin AO
            Grand-parent (génération 2) : groupe sanguin BO

### Justesse

    check50 cs50/problems/2024/x/inheritance

### Style

    style50 inheritance.c

## Comment soumettre

    submit50 cs50/problems/2024/x/inheritance

