# Le scrutin majoritaire à plusieurs tours

## Problème à résoudre

Vous connaissez déjà les élections à scrutin majoritaire uninominal qui suivent un algorithme très simple pour déterminer le vainqueur : chaque électeur dispose d'une voix et le candidat ayant obtenu le plus de voix gagne.

Mais le scrutin majoritaire présente quelques inconvénients. Que se passe-t-il, par exemple, lors d'une élection avec trois candidats et que les bulletins suivants sont déposés ?

![Cinq bulletins, égalité entre Alice et Bob](https://cs50.harvard.edu/x/2024/psets/3/fptp_ballot_1.png)

Un scrutin majoritaire déclarerait ici une égalité entre Alice et Bob, puisque chacun a obtenu deux voix. Mais est-ce le bon résultat ?

Il existe un autre type de système électoral connu sous le nom de vote préférentiel. Dans un système de vote préférentiel, les électeurs peuvent voter pour plusieurs candidats. Au lieu de voter uniquement pour leur premier choix, ils peuvent classer les candidats par ordre de préférence. Les bulletins résultants pourraient donc ressembler à ceux ci-dessous.

![Cinq bulletins, avec préférences classées](https://cs50.harvard.edu/x/2024/psets/3/ranked_ballot_1.png)

Ici, chaque électeur, en plus de préciser son candidat de première préférence, a également indiqué ses deuxième et troisième choix. Et maintenant, ce qui était auparavant une élection à égalité pourrait maintenant avoir un gagnant. La course était à l'origine une égalité entre Alice et Bob, donc Charlie était hors course. Mais l'électeur qui a choisi Charlie a préféré Alice à Bob, donc Alice pourrait ici être déclarée gagnante.

Le vote préférentiel peut également résoudre un autre inconvénient potentiel du scrutin majoritaire. Regardez les bulletins suivants.

![Neuf bulletins, avec préférences classées](https://cs50.harvard.edu/x/2024/psets/3/ranked_ballot_3.png)

Qui devrait gagner cette élection ? Lors d'un scrutin majoritaire où chaque électeur choisit uniquement sa première préférence, Charlie remporte cette élection avec quatre voix contre seulement trois pour Bob et deux pour Alice. Mais une majorité des électeurs (5 sur 9) seraient plus heureux avec Alice ou Bob qu'avec Charlie. En tenant compte des préférences classées, un système électoral peut être en mesure de choisir un gagnant qui reflète mieux les préférences des électeurs.

L'un de ces systèmes de vote préférentiel est le scrutin majoritaire à deux tours. Lors d'une élection à deux tours, les électeurs peuvent classer autant de candidats qu'ils le souhaitent. Si un candidat obtient la majorité (plus de 50 %) des voix de première préférence, ce candidat est déclaré vainqueur de l'élection.

Si aucun candidat n'a obtenu plus de 50 % des voix, un « deuxième tour » a lieu. Le candidat qui a reçu le moins de voix est éliminé de l'élection, et toute personne ayant initialement choisi ce candidat comme première préférence voit désormais sa seconde préférence prise en compte. Pourquoi s'y prendre ainsi ? En effet, cela simule ce qui se serait passé si le candidat le moins populaire n'avait pas été dans l'élection au départ.

Le processus se répète : si aucun candidat n'obtient la majorité des voix, le candidat de la dernière place est éliminé, et toute personne ayant voté pour lui votera à la place pour sa prochaine préférence (qui n'a pas elle-même déjà été éliminée). Une fois qu'un candidat a la majorité, ce candidat est déclaré vainqueur.

Ça a l'air un peu plus compliqué qu'un scrutin majoritaire, n'est-ce pas ? Mais il a sans doute l'avantage d'être un système électoral où le vainqueur de l'élection représente plus précisément les préférences des électeurs. Dans un fichier appelé `runoff.c` dans un dossier appelé `runoff`, créez un programme pour simuler une élection à deux tours.

## Démo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-4rhSKgaZQsY93RLj0xgu7nwKB" src="https://asciinema.org/a/4rhSKgaZQsY93RLj0xgu7nwKB.js"></script>

## Code de distribution

### Télécharger le code de distribution

Connectez-vous à [cs50.dev](https://cs50.dev/), cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ce qui suit :

    $

Ensuite, exécutez

    wget https://cdn.cs50.net/2023/fall/psets/3/runoff.zip

pour télécharger un fichier ZIP appelé `runoff.zip` dans votre codespace.

Puis exécutez

    unzip runoff.zip

pour créer un dossier appelé `runoff`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm runoff.zip

et répondre par « y » suivi d'Entrée à l'invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd runoff

suivi d'Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

    runoff/ $

Si tout s'est bien passé, vous devez exécuter

    ls

et voir un fichier nommé `runoff.c`. L'exécution de `code runoff.c` devrait ouvrir le fichier dans lequel vous taperez votre code pour ce problème. Sinon, revenez sur vos pas et voyez si vous pouvez déterminer où vous vous êtes trompé !

### Comprenez le code dans `runoff.c`

Chaque fois que vous étendez les fonctionnalités d'un code existant, il est préférable de d'abord s'assurer que vous le comprenez dans son état actuel.

Regardez d'abord le haut de `runoff.c`. Deux constantes sont définies : `MAX_CANDIDATES` pour le nombre maximum de candidats à l'élection et `MAX_VOTERS` pour le nombre maximum d'électeurs à l'élection.

    // Max électeurs et candidats
    #define MAX_VOTERS 100
    #define MAX_CANDIDATES 9

Notez que `MAX_CANDIDATES` est utilisé pour dimensionner un tableau, `candidates`.

    // Tableau de candidats
    candidate candidates[MAX_CANDIDATES];

`candidates` est un tableau de `candidate`s. Dans `runoff.c`, un `candidate` est une `struct`. Chaque `candidate` a un champ `string` pour son `name`, un `int` représentant le nombre de `votes` qu'il a actuellement et une valeur `bool` appelée `eliminated` qui indique si le candidat a été éliminé de l'élection. Le tableau `candidates` suivra tous les candidats à l'élection.

    // Les candidats ont un nom, un nombre de voix, un statut éliminé
    typedef struct
    {
        string name;
        int votes;
        bool eliminated;
    }
    candidate;

Vous pouvez maintenant mieux comprendre `preferences`, le tableau bidimensionnel. Le tableau `preferences[i]` représentera toutes les préférences de l'électeur numéro `i`. L'entier, `preferences[i][j]`, stockera l'index du candidat, du tableau `candidates`, qui est la `j`ème préférence de l'électeur `i`.

    // preferences[i][j] est la jème préférence pour l'électeur i
    int preferences[MAX_VOTERS][MAX_CANDIDATES];

Le programme a également deux variables globales : `voter_count` et `candidate_count`.

    // Nombre d'électeurs et de candidats
    int voter_count;
    int candidate_count;

Passons maintenant à `main`. Notez qu'après avoir déterminé le nombre de candidats et le nombre d'électeurs, la boucle de vote principale commence, donnant à chaque électeur une chance de voter. Lorsque l'électeur entre ses préférences, la fonction `vote` est appelée pour suivre toutes les préférences. Si, à un moment quelconque, le bulletin de vote est jugé invalide, le programme se termine.

Une fois que tous les votes sont rentrés, une autre boucle commence, celle-ci va continuer à boucler dans le processus de ruissellement de vérification d'un gagnant et d'élimination du candidat de la dernière place jusqu'à ce qu'il y ait un gagnant.

Le premier appel ici est à une fonction appelée `tabulate`, qui devrait examiner toutes les préférences des électeurs et calculer le nombre total de votes actuels, en regardant le candidat de premier choix de chaque électeur qui n'a pas encore été éliminé. Ensuite, la fonction `print_winner` doit imprimer le gagnant s'il y en a un ; s'il y en a un, le programme est terminé. Mais sinon, le programme doit déterminer le plus petit nombre de votes que toute personne toujours dans l'élection a reçu (via un appel à `find_min`). S'il s'avère que tout le monde dans l'élection est à égalité avec le même nombre de voix (comme déterminé par la fonction `is_tie`), l'élection est déclarée à égalité ; sinon, le candidat (ou les candidats) de la dernière place est éliminé de l'élection via un appel à la fonction `eliminate`.

Si vous regardez un peu plus loin dans le fichier, vous verrez que le reste des fonctions — `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie` et `eliminate` — sont toutes à vous de compléter ! **Vous ne devez rien modifier d'autre dans `runoff.c` (et l'inclusion de fichiers d'en-tête supplémentaires, si vous le souhaitez).**

## Astuces

### Complétez la fonction `vote`

- La fonction prend trois arguments : `voter`, `rank` et `name`.
- Si `name` correspond au nom d'un candidat valide, vous devez mettre à jour le tableau des préférences globales pour indiquer que l'électeur `voter` a ce candidat comme préférence `rank`. Gardez à l'esprit que `0` est la première préférence, `1` est la deuxième préférence, etc. Vous pouvez supposer qu'aucun candidat n'aura le même nom.
- Si la préférence est enregistrée avec succès, la fonction doit renvoyer `true`. Sinon, la fonction doit renvoyer `false`. Considérez, par exemple, lorsque `name` n'est pas le nom de l'un des candidats.

Au fur et à mesure que vous écrivez votre code, tenez compte de ces astuces :

- Rappelez-vous que `candidate_count` stocke le nombre de candidats à l'élection.
- Rappelez-vous que vous pouvez utiliser [`strcmp`](https://man.cs50.io/3/strcmp) pour comparer deux chaînes de caractères.
- Rappelez-vous que `preferences[i][j]` stocke l'index du candidat qui est la préférence classée `j` pour l'`i`ème électeur.

### Compléter la fonction `tabulate`

- La fonction doit mettre à jour le nombre de `votes` que chaque candidat possède à ce stade du second tour.
- Rappelons qu'à chaque étape du second tour, chaque électeur vote effectivement pour son candidat préféré qui n'a pas encore été éliminé.

Pendant que vous écrivez votre code, tenez compte de ces conseils :

- Rappelez-vous que `voter_count` stocke le nombre d'électeurs dans l'élection et que, pour chaque électeur dans notre élection, nous voulons compter un bulletin.
- Rappelez-vous que pour un électeur `i`, son candidat de premier choix est représenté par `preferences[i][0]`, son candidat de deuxième choix par `preferences[i][1]`, etc.
- Rappelez-vous que la `structure` `candidate` a un champ appelé `eliminated`, qui sera `true` si le candidat a été éliminé de l'élection.
- Rappelez-vous que la `structure` `candidate` a un champ appelé `votes`, que vous voudrez probablement mettre à jour pour le candidat préféré de chaque électeur.
- Rappelez-vous qu'une fois que vous avez exprimé un vote pour le premier candidat non éliminé d'un électeur, vous voudrez vous arrêter, et non pas continuer dans son bulletin de vote. Vous pouvez sortir d'une boucle précocement en utilisant `break` à l'intérieur d'une condition.

### Compléter la fonction `print_winner`

- Si un candidat obtient plus de la moitié des voix, son nom doit être imprimé et la fonction doit renvoyer `true`.
- Si personne n'a encore remporté l'élection, la fonction doit renvoyer `false`.

Pendant que vous écrivez votre code, tenez compte de cet indice :

- Rappelez-vous que `voter_count` stocke le nombre d'électeurs dans l'élection. Compte tenu de cela, comment exprimeriez-vous le nombre de votes nécessaires pour remporter l'élection ?

### Compléter la fonction `find_min`

- La fonction doit renvoyer le nombre minimum de voix pour tout candidat participant encore à l'élection.

Pendant que vous écrivez votre code, tenez compte de cet indice :

- Vous voudrez probablement parcourir les candidats pour trouver celui qui est toujours dans l'élection et qui possède le plus petit nombre de voix. Quelles informations devez-vous suivre pendant que vous parcourez les candidats ?

### Compléter la fonction `is_tie`

- La fonction prend un argument `min`, qui sera le nombre minimum de voix que n'importe qui dans l'élection possède actuellement.
- La fonction doit renvoyer `true` si tous les candidats restants dans l'élection ont le même nombre de voix, et doit renvoyer `false` sinon.

Pendant que vous écrivez votre code, tenez compte de cet indice :

- Rappelez-vous qu'une égalité se produit si tous les candidats restant dans l'élection ont le même nombre de voix. Notez également que la fonction `is_tie` prend un argument `min`, qui est le plus petit nombre de voix que n'importe quel candidat possède actuellement. Comment pourriez-vous utiliser `min` pour déterminer si l'élection est à égalité (ou, inversement, pas une égalité )?

### Compléter la fonction `eliminate`

- La fonction prend un argument `min`, qui sera le nombre minimum de voix que n'importe qui dans l'élection possède actuellement.
- La fonction doit éliminer le ou les candidats qui ont `min` nombre de voix.

## Instructions pas à pas

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-Vc5aGywKxo?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Comment tester

Assurez-vous de tester votre code pour vous assurer qu'il gère...

- Une élection avec n'importe quel nombre de candidats (jusqu'au `MAX` de `9`)
- Voter pour un candidat par son nom
- Votes non valables pour les candidats qui ne figurent pas sur le bulletin de vote
- Impression du vainqueur de l'élection s'il n'y en a qu'un
- Ne pas éliminer quelqu'un dans le cas d'une égalité entre tous les candidats restants.

### Exactitude

    check50 cs50/problems/2024/x/runoff

### Style

    style50 runoff.c

## Comment soumettre

    submit50 cs50/problems/2024/x/runoff

