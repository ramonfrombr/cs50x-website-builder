# Correcteur orthographique

## Problème à résoudre

Dans ce problème, vous implémenterez un programme qui vérifie l'orthographe d'un fichier, comme ci-dessous, en utilisant une table de hachage.

## Démonstration

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-o01nuZNSBSH2khVokTs2GEPtP" src="https://asciinema.org/a/o01nuZNSBSH2khVokTs2GEPtP.js"></script>

## Code de distribution

Dans ce problème, vous allez étendre les fonctionnalités du code fourni par l’équipe de CS50.

Connectez-vous à [cs50.dev](https://cs50.dev/), cliquez sur votre fenêtre de terminal et exécutez `cd` par lui-même. L'invite de votre fenêtre de terminal devrait ressembler à ce qui suit :

    $

Exécutez ensuite :

    wget https://cdn.cs50.net/2023/fall/psets/5/speller.zip

pour télécharger un ZIP appelé `speller.zip` dans votre espace de code.

Ensuite, exécutez :

    unzip speller.zip

pour créer un dossier appelé `speller`. Vous n’avez plus besoin du fichier ZIP, vous pouvez donc exécuter :

    rm speller.zip

et répondre par « y » suivi de la touche Entrée à l’invite pour supprimer le fichier ZIP que vous avez téléchargé.

Tapez maintenant :

    cd speller

suivi de la touche Entrée pour vous déplacer dans (c’est-à-dire ouvrir) ce répertoire. Votre invite devrait désormais ressembler à ce qui suit :

    speller/ $

Exécutez `ls` par lui-même, et vous devriez voir quelques fichiers et dossiers :

    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  speller50  texts/

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et essayez de déterminer où vous vous êtes trompé !

## Contexte

<div class="alert alert-danger" data-alert="danger" role="alert"><p><strong>Étant donné les nombreux fichiers dans ce programme, il est important de lire cette section dans son intégralité avant de commencer. Vous saurez alors quoi faire et comment le faire !</strong></p></div>

Théoriquement, sur une entrée de taille _n_, un algorithme avec un temps d'exécution de _n_ est « asymptotiquement équivalent », en termes de _O_, à un algorithme avec un temps d'exécution de _2n_. En effet, lorsque l’on décrit le temps d’exécution d’un algorithme, on se concentre généralement sur le terme dominant (c’est-à-dire le plus impactant) (ici _n_, puisque _n_ pourrait être bien plus grand que 2). Dans le monde réel, cependant, le fait est que _2n_ semble deux fois plus lent que _n_.

Le défi qui vous attend est d’implémenter le correcteur orthographique le plus rapide possible ! Par « plus rapide », nous parlons toutefois du temps d’horloge réel, et non asymptotique.

Dans `speller.c`, nous avons mis au point un programme conçu pour vérifier l’orthographe d’un fichier après avoir chargé un dictionnaire de mots du disque vers la mémoire. Ce dictionnaire, quant à lui, est implémenté dans un fichier appelé `dictionary.c`. (Il pourrait simplement être implémenté dans `speller.c`, mais au fur et à mesure que les programmes deviennent plus complexes, il est souvent pratique de les diviser en plusieurs fichiers.) Les prototypes des fonctions qui s’y trouvent sont quant à eux définis non pas dans `dictionary.c` lui-même, mais dans `dictionary.h` à la place. De cette façon, `speller.c` et `dictionary.c` peuvent tous deux `#include` le fichier. Malheureusement, nous n’avons pas tout à fait réussi à implémenter la partie chargement. Ni la partie vérification. Les deux (et un peu plus) nous vous les laissons ! Mais d’abord, une visite guidée.

### Compréhension

#### `dictionary.h`

Ouvrez `dictionary.h`, et vous verrez une nouvelle syntaxe, y compris quelques lignes qui mentionnent `DICTIONARY_H`. Pas besoin de s’inquiéter à ce sujet, mais si vous êtes curieux, ces lignes garantissent simplement que, même si `dictionary.c` et `speller.c` (que vous verrez dans un instant) `#include` ce fichier, `clang` ne le compilera qu’une seule fois.

Remarquez ensuite que l’on utilise `#include` sur un fichier appelé `stdbool.h`. C’est le fichier dans lequel `bool` lui-même est défini. Vous n’en aviez pas eu besoin auparavant, car la bibliothèque CS50 avait l’habitude de l’inclure pour vous.

Remarquez également notre utilisation de `#define`, une « directive de préprocesseur » qui définit une « constante » appelée `LENGTH` qui a une valeur de `45`. C’est une constante dans le sens où vous ne pouvez pas (accidentellement) la modifier dans votre propre code. En fait, `clang` remplacera toute mention de `LENGTH` dans votre propre code par, littéralement, `45`. En d’autres termes, ce n’est pas une variable, juste une astuce de recherche et de remplacement.

Enfin, remarquez les prototypes de cinq fonctions : `check`, `hash`, `load`, `size` et `unload`. Notez que trois d'entre elles prennent un pointeur comme argument, selon le `* ` :

    bool check(const char *word);
    unsigned int hash(const char *word);
    bool load(const char *dictionary);

Rappelez-vous que `char *` est ce que nous appelions `string`. Ces trois prototypes sont donc essentiellement :

    bool check(const string word);
    unsigned int hash(const string word);
    bool load(const string dictionary);

Et `const`, en attendant, dit simplement que ces chaînes, lorsqu'elles sont transmises en tant qu'arguments, doivent rester constantes ; vous ne pourrez pas les modifier, accidentellement ou autrement !

#### `dictionary.c`

Ouvrez maintenant `dictionary.c`. Notez que, en haut du fichier, nous avons défini une `struct` appelée `node` qui représente un nœud dans une table de hachage. Et nous avons déclaré un tableau de pointeurs global, `table`, qui représentera (bientôt) la table de hachage que vous utiliserez pour suivre les mots dans le dictionnaire. Le tableau contient `N` pointeurs de nœuds, et nous avons défini `N` égal à `26` pour le moment, pour correspondre à la fonction `hash` par défaut comme décrit ci-dessous. Vous voudrez probablement l’augmenter en fonction de votre propre implémentation de `hash`.

Ensuite, notez que nous avons implémenté `load`, `check`, `size` et `unload`, mais à peine, juste assez pour que le code se compile. Notez également que nous avons implémenté `hash` avec un exemple d'algorithme basé sur la première lettre du mot. Votre travail, en fin de compte, est de réimplémenter ces fonctions aussi intelligemment que possible afin que ce correcteur orthographique fonctionne comme annoncé. Et vite !

#### `speller.c`

D'accord, ouvrez maintenant `speller.c` et prenez le temps d'examiner le code et les commentaires qui s'y trouvent. Vous n'aurez rien à changer dans ce fichier, et vous n'avez pas besoin d'en comprendre l'intégralité, mais essayez néanmoins d'avoir une idée de sa fonctionnalité. Notez que, grâce à une fonction appelée `getrusage`, nous allons "comparer" (c'est-à-dire chronométrer l'exécution de) vos implémentations de `check`, `load`, `size` et `unload`. Notez également comment nous transmettons à `check` mot par mot le contenu d'un fichier à vérifier. En fin de compte, nous rapportons chaque faute d'orthographe dans ce fichier ainsi qu'un certain nombre de statistiques.

Notez, accessoirement, que nous avons défini l'utilisation de `speller` comme suit :

```
Usage : speller [dictionnaire] texte
```

où `dictionnaire` est supposé être un fichier contenant une liste de mots en minuscules, un par ligne, et `texte` est un fichier à vérifier. Comme le suggèrent les crochets, la fourniture du `dictionnaire` est facultative ; si cet argument est omis, `speller` utilisera par défaut `dictionaries/large`. En d'autres termes, l'exécution de

```
./speller texte
```

équivaut à exécuter

```
./speller dictionaries/large texte
```

où `texte` est le fichier que vous souhaitez vérifier. Autant dire que le premier est plus facile à taper ! (Bien sûr, `speller` ne pourra charger aucun dictionnaire tant que vous n'aurez pas implémenté `load` dans `dictionary.c ! Jusque-là, vous verrez « Impossible de charger ».)

Dans le dictionnaire par défaut, notez bien, il y a 143 091 mots, qui doivent tous être chargés en mémoire ! En fait, jetez un coup d'œil à ce fichier pour avoir une idée de sa structure et de sa taille. Notez que chaque mot dans ce fichier apparaît en minuscules (même, pour simplifier, les noms propres et les acronymes). De haut en bas, le fichier est trié lexicographiquement, avec un seul mot par ligne (chacun se terminant par `\n`). Aucun mot ne dépasse 45 caractères et aucun mot n'apparaît plus d'une fois. Pendant le développement, vous pouvez trouver utile de fournir à `speller` un `dictionnaire` contenant beaucoup moins de mots, de peur d'avoir du mal à déboguer une structure autrement énorme en mémoire. Dans `dictionaries/small` se trouve un tel dictionnaire. Pour l'utiliser, exécutez

```
./speller dictionaries/small texte
```

où `texte` est le fichier que vous souhaitez vérifier. Ne passez pas à autre chose tant que vous n'êtes pas sûr de comprendre comment fonctionne `speller` en lui-même !

Il y a de fortes chances que vous n'ayez pas passé assez de temps à examiner `speller.c`. Revenez en arrière et relisez-le !

#### `texts/`

Afin que vous puissiez tester votre implémentation de `speller`, nous vous avons également fourni un grand nombre de textes, parmi lesquels le scénario de _La La Land_, le texte de l'Affordable Care Act, trois millions d'octets de Tolstoï, des extraits de _The Federalist Papers_ et de Shakespeare, et plus encore. Afin que vous sachiez à quoi vous attendre, ouvrez et parcourez chacun de ces fichiers, qui se trouvent tous dans un répertoire appelé `texts` dans votre répertoire `pset5`.

Maintenant, comme vous devez le savoir après avoir lu attentivement `speller.c`, la sortie de `speller`, si elle est exécutée avec, disons :

```
./speller texts/lalaland.txt
```

ressemblera éventuellement à ce qui suit.

Voici quelques exemples de la sortie que vous verrez. Pour information, nous avons extrait quelques exemples de « fautes ». Et pour ne pas gâcher le plaisir, nous avons omis nos propres statistiques pour l'instant.

```
FAUTES D'ORTHOGRAPHE :

[...]
AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
[...]
Shangri
[...]
fianc
[...]
Sebastian's
[...]
```

```
MOTS MAL ÉPELÉS :
MOTS DANS LE DICTIONNAIRE :
MOTS DANS LE TEXTE :
TEMPS EN chargement :
TEMPS EN vérification :
TEMPS EN taille :
TEMPS EN déchargement :
TEMPS EN TOTAL :
```

`TEMPS EN chargement` représente le nombre de secondes que `speller` passe à exécuter votre implémentation de `load`. `TEMPS EN vérification` représente le nombre de secondes que `speller` passe, au total, à exécuter votre implémentation de `check`. `TEMPS EN taille` représente le nombre de secondes que `speller` passe à exécuter votre implémentation de `size`. `TEMPS EN déchargement` représente le nombre de secondes que `speller` passe à exécuter votre implémentation de `unload`. `TEMPS EN TOTAL` est la somme de ces quatre mesures.

**Notez que ces durées peuvent varier quelque peu entre les exécutions de `speller`, en fonction de ce que fait d'autre votre espace de code, même si vous ne modifiez pas votre code.**

Incidemment, pour être clair, par « mal orthographié », nous entendons simplement qu'un mot n'est pas dans le `dictionnaire` fourni.

#### `Makefile`

Enfin, rappelez-vous que `make` automatise la compilation de votre code afin que vous n'ayez pas à exécuter `clang` manuellement avec un tas de commutateurs. Cependant, à mesure que vos programmes grandissent, `make` ne pourra plus déduire du contexte comment compiler votre code ; vous devrez commencer à indiquer à `make` comment compiler votre programme, en particulier lorsqu'il s'agit de fichiers source multiples (c'est-à-dire `.c`), comme c'est le cas pour ce problème. Nous utiliserons donc un `Makefile`, un fichier de configuration qui indique à `make` exactement ce qu'il doit faire. Ouvrez `Makefile` et vous devriez voir quatre lignes :

1. La première ligne indique à `make` d'exécuter les lignes suivantes chaque fois que vous exécutez vous-même `make speller` (ou simplement `make`).
2. La deuxième ligne indique à `make` comment compiler `speller.c` en code machine (c'est-à-dire `speller.o`).
3. La troisième ligne indique à `make` comment compiler `dictionary.c` en code machine (c'est-à-dire `dictionary.o`).
4. La quatrième ligne indique à `make` de lier `speller.o` et `dictionary.o` dans un fichier appelé `speller`.

**Assurez-vous de compiler `speller` en exécutant `make speller` (ou simplement `make`). L'exécution de `make dictionary` ne fonctionnera pas !**

## Spécifications

Bon, le défi qui vous est désormais proposé est d'implémenter, dans l'ordre, `load`, `hash`, `size`, `check` et `unload` aussi efficacement que possible en utilisant une table de hachage, de telle sorte que `TIME IN load`, `TIME IN check`, `TIME IN size` et `TIME IN unload` soient tous minimisés. À vrai dire, la notion même de minimisation n'est pas évidente, dans la mesure où ces indicateurs varieront sans doute en fonction des valeurs de `dictionary` et `text` fournies à `speller`. Mais c'est là que réside le défi, voire le plaisir, de ce problème. Ce problème est votre chance de concevoir. Bien que nous vous invitions à minimiser l'espace, votre pire ennemi reste le temps. Mais avant de vous lancer, voici quelques spécifications de notre part.

- Vous n'êtes pas autorisé à modifier `speller.c` ou `Makefile`.
- Vous êtes autorisé à modifier `dictionary.c` (et devez d'ailleurs le faire pour compléter les implémentations de `load`, `hash`, `size`, `check` et `unload`), mais vous n'êtes pas autorisé à modifier les déclarations (c'est-à-dire les prototypes) de `load`, `hash`, `size`, `check` ou `unload`. Vous pouvez cependant ajouter de nouvelles fonctions et variables (locales ou globales) à `dictionary.c`.
- Vous pouvez modifier la valeur de `N` dans `dictionary.c` pour que votre table de hachage puisse avoir plus de compartiments.
- Vous pouvez modifier `dictionary.h`, mais vous n'êtes pas autorisé à modifier les déclarations de `load`, `hash`, `size`, `check` ou `unload`.
- Votre implémentation de `check` doit être insensible à la casse. En d'autres termes, si `foo` se trouve dans le dictionnaire, alors `check` doit renvoyer « vrai » pour n'importe quelle capitalisation de ce terme ; aucun des termes `foo`, `foO`, `fOo`, `fOO`, `fOO`, `Foo`, `FoO`, `FOo` et `FOO` ne doit être considéré comme mal orthographié.
- La capitalisation mise à part, votre implémentation de `check` ne doit renvoyer « vrai » que pour les mots réellement présents dans `dictionary`. Méfiez-vous du hard-coding de mots courants (par exemple, « the »), de peur que nous transmettions à votre implémentation un `dictionary` dépourvu de ces mêmes mots. De plus, les seuls possessifs autorisés sont ceux qui se trouvent réellement dans `dictionary`. En d'autres termes, même si `foo` se trouve dans `dictionary`, `check` doit renvoyer « faux » pour `foo's` si `foo's` ne se trouve pas également dans `dictionary`.
- Vous pouvez supposer que tout `dictionary` transmis à votre programme sera structuré exactement comme le nôtre, trié alphabétiquement de haut en bas avec un mot par ligne, chacun se terminant par `\n`. Vous pouvez également supposer que `dictionary` contiendra au moins un mot, qu'aucun mot ne dépassera `LENGTH` (une constante définie dans `dictionary.h`) caractères, qu'aucun mot n'apparaîtra plus d'une fois, que chaque mot ne contiendra que des caractères alphabétiques minuscules et éventuellement des apostrophes, et qu'aucun mot ne commencera par une apostrophe.
- Vous pouvez supposer que `check` ne recevra que des mots qui contiennent des caractères alphabétiques (minuscules ou majuscules) et éventuellement des apostrophes.
- Votre correcteur orthographique ne peut prendre que `text` et, éventuellement, `dictionary` comme entrée. Bien que vous puissiez être tenté (en particulier si vous êtes parmi les plus à l'aise) de « prétraiter » notre dictionnaire par défaut afin d'en déduire une « fonction de hachage idéale », vous ne pouvez pas enregistrer la sortie d'un tel prétraitement sur le disque afin de la recharger en mémoire lors des exécutions ultérieures de votre correcteur orthographique dans le but d'obtenir un avantage.
- Votre correcteur orthographique ne doit pas laisser de fuite de mémoire. Assurez-vous de vérifier l'absence de fuite avec `valgrind`.
- **La fonction de hachage que vous écrivez doit être en fin de compte la vôtre, et non une fonction que vous recherchez en ligne.**

Prêt à vous lancer ?

- Implémentez `load`.
- Implémentez `hash`.
- Implémentez `size`.
- Implémentez `check`.
- Implémentez `unload`.

## Astuces

### Implémenter `load`

Complétez la fonction `load`. `load` doit charger le dictionnaire en mémoire (en particulier, dans une table de hachage !). `load` doit renvoyer « vrai » en cas de succès et « faux » dans le cas contraire.

Considérez que ce problème est simplement composé de problèmes plus petits :

1.  Ouvrir le fichier dictionnaire
2.  Lire chaque mot dans le fichier
    1.  Ajouter chaque mot à la table de hachage
3.  Fermer le fichier dictionnaire

Écrivez un peu de pseudo-code pour vous rappeler de faire exactement ça :

    bool load(const char *dictionary)
    {
        // Ouvrir le fichier dictionnaire

        // Lire chaque mot dans le fichier

            // Ajouter chaque mot à la table de hachage

        // Fermer le fichier dictionnaire
    }

Réfléchissez d'abord à la façon d'ouvrir le fichier dictionnaire. [`fopen`](https://manual.cs50.io/3/fopen) est un choix naturel. Vous pouvez utiliser le mode `r`, étant donné que vous n'avez besoin que de _lire_ des mots dans le fichier dictionnaire (pas de les _écrire_ ou de les _ajouter_).

    bool load(const char *dictionary)
    {
        // Ouvrir le fichier dictionnaire
        FILE *source = fopen(dictionary, "r");

        // Lire chaque mot dans le fichier

            // Ajouter chaque mot à la table de hachage

        // Fermer le fichier dictionnaire
    }

Avant de poursuivre, vous devez écrire du code pour vérifier si le fichier s'est ouvert correctement. C'est à vous de décider ! Il est également préférable de s'assurer de fermer tous les fichiers que vous ouvrez, c'est donc le bon moment pour écrire le code pour fermer le fichier dictionnaire :

    bool load(const char *dictionary)
    {
        // Ouvrir le fichier dictionnaire
        FILE *source = fopen(dictionary, "r");

        // Lire chaque mot dans le fichier

            // Ajouter chaque mot à la table de hachage

        // Fermer le fichier dictionnaire
        fclose(source);
    }

Il reste à lire chaque mot dans le fichier et à ajouter chaque mot à la table de hachage. Renvoyez « vrai » lorsque l'opération entière est réussie et « faux » si elle échoue un jour. Envisagez de suivre la procédure pas à pas de ce problème et continuez à décomposer les sous-problèmes en problèmes encore plus petits. Par exemple, ajouter chaque mot à la table de hachage peut simplement consister à implémenter quelques étapes encore plus petites :

1.  Créer un espace pour un nouveau nœud de table de hachage
2.  Copier le mot dans le nouveau nœud
3.  Hacher le mot pour obtenir sa valeur de hachage
4.  Insérer le nouveau nœud dans la table de hachage (en utilisant l'index spécifié par sa valeur de hachage)

Bien entendu, il existe plusieurs façons d'aborder ce problème, chacune présentant ses propres compromis de conception. Pour cette raison, le reste du code dépend de vous !

### Implémenter `hash`

Complétez la fonction `hash`. `hash` doit prendre une chaîne de caractères, `word`, en entrée et renvoyer un `int` « non signé » positif.

La fonction de hachage qui vous est fournie renvoie un `int` compris entre 0 et 25, inclus, basé sur le premier caractère de `word`. Cependant, il existe de nombreuses façons d'implémenter une fonction de hachage au-delà de l'utilisation du premier caractère (ou des _caractères_) d'un mot. Envisagez une fonction de hachage qui utilise une somme de valeurs ASCII ou la longueur d'un mot. Une bonne fonction de hachage réduit les « collisions » et a une distribution (principalement !) uniforme dans les « compartiments » de la table de hachage.

### Implémenter `size`

Complétez la fonction `size`. `size` doit retourner le nombre de mots chargés dans le dictionnaire. Envisagez deux approches pour résoudre ce problème :

- Comptez chaque mot lorsque vous le chargez dans le dictionnaire. Renvoyez ce décompte lorsque `size` est appelée.
- Chaque fois que `size` est appelée, parcourez les mots de la table de hachage pour les compter. Renvoyez ce décompte.

Laquelle vous semble la plus efficace ? Quelle que soit votre préférence, nous vous laissons choisir le code.

### Implémenter `check`

Complétez la fonction `check`. `check` doit renvoyer `true` si un mot se trouve dans le dictionnaire, et `false` dans le cas contraire.

Considérez que ce problème est également composé de problèmes plus petits. Si vous avez implémenté une table de hachage, trouver un mot ne nécessite que quelques étapes :

1.  Hachez le mot pour obtenir sa valeur de hachage
2.  Recherchez le mot dans la table de hachage à l’emplacement spécifié par sa valeur de hachage
    1.  Renvoyez `true` si le mot est trouvé
3.  Renvoyez `false` si aucun mot n’est trouvé

Pour comparer des chaînes de caractères de façon insensible à la casse, vous trouverez peut-être [`strcasecmp`](https://man.cs50.io/3/strcasecmp) (déclarée dans `strings.h`) utile ! Vous voudrez probablement aussi vous assurer que votre fonction de hachage est insensible à la casse, de sorte que `foo` et `FOO` aient la même valeur de hachage.

### Implémenter `unload`

Complétez la fonction `unload`. Assurez-vous de `free` dans `unload` toute mémoire que vous avez allouée dans `load` !

N'oubliez pas que `valgrind` est votre nouvel ami. Sachez que `valgrind` surveille les fuites pendant l’exécution de votre programme, alors assurez-vous de fournir des arguments de ligne de commande si vous souhaitez que `valgrind` analyse `speller` lorsque vous utilisez un `dictionnaire` et/ou un texte en particulier, comme dans l’exemple ci-dessous. Il est préférable d’utiliser un petit texte, sinon l’exécution de `valgrind` pourrait prendre un certain temps.

    valgrind ./speller texts/cat.txt

Si vous exécutez `valgrind` sans spécifier de `texte` pour `speller`, les implémentations de `load` et `unload` ne seront pas appelées (et donc analysées).

Si vous n’êtes pas sûr de comment interpréter la sortie de `valgrind`, demandez simplement de l’aide à `help50` :

    help50 valgrind ./speller texts/cat.txt

## Procédure pas à pas

<div class="alert alert-danger" data-alert="danger" role="alert"><p><strong>Notez qu’il y a 6 vidéos dans cette playlist.</strong></p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/_z57x5PGF4w?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382T4b6jjwX_qbU23E_Unwcz"></iframe></div>

## Comment tester

Comment vérifier si votre programme affiche les bons mots mal orthographiés ? Eh bien, vous pouvez consulter les « clés de réponse » qui se trouvent dans le répertoire `keys` de votre répertoire `speller`. Par exemple, dans `keys/lalaland.txt` se trouvent tous les mots que votre programme _devrait_ penser mal orthographiés.

Vous pouvez donc exécuter votre programme sur un texte dans une fenêtre, comme ci-dessous.

    ./speller texts/lalaland.txt

Et vous pouvez ensuite exécuter la solution de l’équipe dans une autre fenêtre, comme ci-dessous.

    ./speller50 texts/lalaland.txt

Et vous pouvez ensuite comparer visuellement les fenêtres côte à côte. Cela peut cependant vite devenir fastidieux. Vous pouvez donc plutôt « rediriger » la sortie de votre programme vers un fichier, comme ci-dessous.

    ./speller texts/lalaland.txt > student.txt
    ./speller50 texts/lalaland.txt > staff.txt

Vous pouvez ensuite comparer les deux fichiers côte à côte dans la même fenêtre avec un programme comme `diff`, comme ci-dessous.

    diff -y student.txt staff.txt

Vous pouvez également, pour gagner du temps, comparer la sortie de votre programme (en supposant que vous l’ayez redirigée vers, par exemple, `student.txt`) avec l’une des clés de réponse sans exécuter la solution de l’équipe, comme ci-dessous.

    diff -y student.txt keys/lalaland.txt

Si la sortie de votre programme correspond à celle de l’équipe, `diff` affichera deux colonnes qui devraient être identiques, à l’exception peut-être des temps d’exécution en bas. Si les colonnes diffèrent, vous verrez un `>` ou `|` à l’endroit de la différence. Par exemple, si vous voyez

    MISSPELLED WORDS                                                MISSPELLED WORDS

    TECHNO                                                          TECHNO
    L                                                               L
                                                                  > Thelonious
    Prius                                                           Prius
                                                                  > MIA
    L                                                               L

cela signifie que votre programme (dont la sortie est à gauche) ne pense pas que `Thelonious` ou `MIA` est mal orthographié, alors que la sortie de l’équipe (à droite) le pense, comme en témoigne l’absence de `Thelonious` dans la colonne de gauche et la présence de `Thelonious` dans la colonne de droite.

Enfin, assurez-vous de tester avec les grands et les petits dictionnaires par défaut. Faites attention à ne pas supposer que si votre solution fonctionne avec le grand dictionnaire, elle fonctionnera aussi avec le petit. Voici comment essayer le petit dictionnaire :

    ./speller dictionaries/small texts/cat.txt

### Exactitude

    check50 cs50/problems/2024/x/speller

### Style

    style50 dictionary.c

## Solution de l’équipe

Comment évaluer à quel point votre code est rapide (et correct) ? Eh bien, comme toujours, n’hésitez pas à utiliser la solution de l’équipe, comme ci-dessous, et comparez ses chiffres aux vôtres.

    ./speller50 texts/lalaland.txt

## Comment soumettre

    submit50 cs50/problems/2024/x/speller

