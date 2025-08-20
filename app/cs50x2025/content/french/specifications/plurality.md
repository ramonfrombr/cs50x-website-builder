## Pluralité

## Problème à résoudre

Les élections se présentent sous toutes les formes et toutes les tailles. Au Royaume-Uni, le [Premier ministre](https://www.parliament.uk/education/about-your-parliament/general-elections/) est officiellement nommé par le monarque, qui choisit généralement le chef du parti politique qui remporte le plus de sièges à la Chambre des communes. Les États-Unis utilisent un processus électoral à plusieurs étapes [Electoral College](https://www.archives.gov/federal-register/electoral-college/about.html) via lequel les citoyens votent pour déterminer comment chaque État doit allouer les électeurs qui élisent ensuite le président.

Cependant, le moyen le plus simple d'organiser une élection reste probablement une méthode communément appelée « vote majoritaire » (également connu sous le nom de « premier passé le poteau » ou « le gagnant prend tout »). Lors d'un vote majoritaire, chaque électeur peut voter pour un candidat. À la fin de l'élection, le candidat ayant obtenu le plus grand nombre de voix est déclaré vainqueur de l'élection.

Pour ce problème, vous allez implémenter un programme qui organise une élection majoritaire, comme indiqué ci-dessous.

## Démonstration

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-o2EXEqiz7iqfDB31wYxBOWjs8" src="https://asciinema.org/a/o2EXEqiz7iqfDB31wYxBOWjs8.js"></script>

## Code de distribution

Pour ce problème, vous allez étendre la fonctionnalité du « code de distribution » qui vous a été fourni par l'équipe de CS50.

### Télécharger le code de distribution

Connectez-vous à [cs50.dev](https://cs50.dev/), cliquez sur votre fenêtre de terminal et exécutez `cd` seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ce qui suit :

    $

Ensuite, exécutez :

    wget https://cdn.cs50.net/2023/fall/psets/3/plurality.zip

afin de télécharger un fichier ZIP appelé `plurality.zip` dans votre espace de codes.

Ensuite, exécutez :

    unzip plurality.zip

pour créer un dossier appelé `plurality`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter :

    rm plurality.zip

et répondre par « y » suivi d'Entrée à l'invite pour supprimer le fichier ZIP que vous avez téléchargé.

Saisissez maintenant :

    cd plurality

suivi d'Entrée pour accéder à (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit :

    plurality/ $

Si tout s'est bien passé, vous devez exécuter :

    ls

et voir un fichier nommé `plurality.c`. Si vous exécutez `code plurality.c`, le fichier dans lequel vous taperez votre code pour cet ensemble de problèmes devrait s'ouvrir. Si ce n'est pas le cas, revenez sur vos pas et voyez si vous pouvez déterminer où vous vous êtes trompé !

### Comprendre le code dans `plurality.c`

Chaque fois que vous étendez la fonctionnalité d'un code existant, il est préférable d'être sûr de le comprendre d'abord dans son état actuel.

Regardez d'abord en haut du fichier. La ligne `#define MAX 9` est une syntaxe utilisée ici pour signifier que `MAX` est une constante (égale à `9`) qui peut être utilisée dans tout le programme. Ici, elle représente le nombre maximal de candidats possibles lors d'une élection.

    // Nombre maximal de candidats
    #define MAX 9

Notez que `plurality.c` utilise ensuite cette constante pour définir un tableau global, c'est-à-dire un tableau auquel n'importe quelle fonction peut accéder.

    // Tableau de candidats
    candidate candidates[MAX];

Mais qu'est-ce qu'un `candidate` dans ce cas ? Dans `plurality.c`, un `candidate` est une `struct`. Chaque `candidate` possède deux champs : une `string` appelée `name` qui représente le nom du candidat et un `int` appelé `votes` qui représente le nombre de voix obtenu par le candidat.

    // Les candidats ont un nom et un nombre de voix
    typedef struct
    {
        string name;
        int votes;
    }
    candidate;

Examinez maintenant la fonction `main`. Voyez si vous pouvez trouver où le programme définit une variable globale `candidate_count` représentant le nombre de candidats à l'élection.

    // Nombre de candidats
    int candidate_count;

Qu'en est-il de l'endroit où il copie les arguments de ligne de commande dans le tableau `candidates` ?

    // Remplir le tableau de candidats
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Le nombre maximal de candidats est %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

Et où il demande à l'utilisateur de saisir le nombre d'électeurs ?

    int voter_count = get_int("Nombre d'électeurs : ");

Ensuite, le programme permet à chaque électeur de voter, en appelant la fonction `vote` sur chaque candidat pour lequel il a voté. Enfin, `main` appelle la fonction `print_winner` pour imprimer le (ou les) vainqueur(s) de l'élection. Nous vous laissons identifier le code qui implémente cette fonctionnalité.

Si vous regardez plus loin dans le fichier, cependant, vous remarquerez que les fonctions `vote` et `print_winner` ont été laissées vides.

    // Mettre à jour les totaux des votes compte tenu d'un nouveau vote
    bool vote(string name)
    {
        // TODO
        return false;
    }

    // Imprimer le (ou les) vainqueur(s) de l'élection
    void print_winner(void)
    {
        // TODO
        return;
    }

Vous devez compléter cette partie ! **Vous ne devez rien modifier d'autre dans `plurality.c` que les implémentations des fonctions `vote` et `print_winner` (et l'inclusion de fichiers d'en-tête supplémentaires, si vous le souhaitez).**

## Astuces

### Complétez la fonction `vote`

Ensuite, complétez la fonction `vote`.

- Considérez que la signature de `vote`, `bool vote(string name)`, montre qu'elle prend un seul argument, une `string` appelée `name`, représentant le nom du candidat pour lequel il a été voté.
- `vote` doit renvoyer un `bool`, où `true` indique qu'un vote a été correctement exprimé et `false` indique que ce n'est pas le cas.

Une façon d'aborder ce problème est de procéder comme suit :

1.  Itérer sur chaque candidat
    1.  Vérifier si le nom du candidat correspond à l'entrée `name`
        1.  Si oui, incrémenter les votes de ce candidat et renvoyer `true`
        2.  Sinon, continuer la vérification
2.  S'il n'y a pas de correspondance après avoir vérifié chaque candidat, renvoyer `false`

Écrivons un faux-code pour vous rappeler de faire exactement cela :

    // Mettre à jour les totaux de votes donné un nouveau vote
    bool vote(string name)
    {
        // Itérer sur chaque candidat
            // Vérifier si le nom du candidat correspond au nom donné
                // Si oui, incrémenter les votes du candidat et renvoyer true

        // S'il n'y a pas de correspondance, renvoyer false
    }

Cependant, nous vous laisserons la mise en œuvre en code !

### Complétez la fonction `print_winner`

Enfin, complétez la fonction `print_winner`.

- La fonction doit imprimer le nom du candidat qui a reçu le plus de votes lors de l'élection, puis imprimer une nouvelle ligne.
- L'élection pourrait aboutir à une égalité si plusieurs candidats obtiennent chacun le nombre maximum de voix. Dans ce cas, vous devez indiquer les noms de chacun des candidats gagnants, chacun sur une ligne séparée.

Vous pourriez penser qu'un algorithme de tri résoudrait au mieux ce problème : imaginez trier les candidats en fonction de leur total de votes et d'imprimer le meilleur candidat (ou les meilleurs candidats). Rappelez-vous, cependant, que le tri peut être coûteux : même Merge Sort, l'un des algorithmes de tri les plus rapides, s'exécute en \\(O(N \\space log(N))\\).

Considérez que vous n'avez besoin que de deux informations pour résoudre ce problème :

1.  Le nombre maximum de votes
2.  Le candidat (ou les candidats) avec ce nombre de votes

En tant que tel, une bonne solution pourrait ne nécessiter que deux recherches. Écrivez un faux-code pour vous rappeler de faire exactement cela :

    // Imprimer le gagnant (ou les gagnants) de l'élection
    void print_winner(void)
    {
        // Trouver le nombre maximum de votes

        // Imprimer le candidat (ou les candidats) avec le maximum de votes

    }

Cependant, nous vous laisserons le code !

## Procédure

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ftOapzDjEb8?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Comment tester

Assurez-vous de tester votre code pour vous assurer qu'il gère…

- Une élection avec un nombre quelconque de candidats (jusqu'au `MAX` de `9`)
- Voter pour un candidat par son nom
- Votes invalides pour les candidats qui ne sont pas sur le bulletin de vote
- Imprimer le gagnant de l'élection s'il n'y en a qu'un
- Imprimer le gagnant de l'élection s'il y a plusieurs gagnants

### Justesse

    check50 cs50/problems/2024/x/plurality

### Style

    style50 plurality.c

## Comment soumettre

    submit50 cs50/problems/2024/x/plurality

