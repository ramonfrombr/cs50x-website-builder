## Bonjour tout le monde

## Problème à résoudre

Grâce au Professeur [David Malan](https://en.wikipedia.org/wiki/David_J._Malan) (qui enseignait CS50 lorsque Ramon le suivit !), "bonjour tout le monde" a été implémenté dans des centaines de langues. Ajoutons votre implémentation à la liste !

Dans un fichier appelé `hello.c`, dans un dossier appelé `world`, implémentez un programme en C qui imprime `bonjour tout le monde\n`, et c'est tout !

#### Astuce

Voici le code réel que vous devez écrire ! (Sacrée astuce, hein ?) Il est cependant préférable de le saisir vous-même plutôt que de le copier/coller, afin de commencer à développer votre "mémoire musculaire" dans l'écriture de code.

    #include <stdio.h>

    int main(void)
    {
        printf("hello, world\n");
    }

## Démonstration

Voici une démonstration de ce qui doit se produire lorsque vous compilez et exécutez votre programme.

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-C5rag3703OZpKxGJ6dSwHnUEF" src="https://asciinema.org/a/C5rag3703OZpKxGJ6dSwHnUEF.js"></script>

## Comment commencer

Ouvrez [VS Code](https://cs50.dev/).

Commencez par cliquer dans votre fenêtre de terminal, puis exécutez `cd` tout seul. Vous devriez constater que son "invite" ressemble à ce qui suit :

    $

Exécutez ensuite :

    mkdir world

pour créer un dossier appelé `world` dans votre espace de code.

Exécutez ensuite :

    cd world

pour changer de répertoire et entrer dans ce dossier. Vous devriez maintenant voir l'invite de votre terminal comme : `world/ $`. Vous pouvez désormais exécuter :

    code hello.c

pour créer un fichier appelé `hello.c` dans lequel vous pouvez écrire votre code.

## Comment tester

Rappelez-vous que vous pouvez compiler `hello.c` avec :

    make hello

Si vous ne voyez pas de message d'erreur, la compilation a réussi ! Vous pouvez confirmer cela avec :

    ls

qui devrait lister non seulement `hello.c` (qui est un code source), mais aussi `hello` (qui est un code machine).

Si vous voyez un message d'erreur, essayez de corriger votre code et de le recompiler. Toutefois, si vous ne comprenez pas le message d'erreur, essayez d'exécuter :

    help50 make hello

pour des conseils.

Une fois que votre code est correctement compilé, vous pouvez exécuter votre programme avec :

    ./hello

### Justesse

Exécutez ce qui suit pour évaluer la justesse de votre code à l'aide de `check50`, un programme en ligne de commande qui affichera des visages heureux chaque fois que votre code réussira les tests automatisés de CS50 et des visages tristes chaque fois qu'il échouera !

    check50 cs50/problems/2024/x/world

### Style

Exécutez ce qui suit pour évaluer le style de votre code à l'aide de `style50`, un programme en ligne de commande qui affichera des ajouts (en vert) et des suppressions (en rouge) que vous devez apporter à votre programme afin d'améliorer son style. Si vous avez du mal à voir ces couleurs, `style50` prend également en charge d'autres [modes](https://cs50.readthedocs.io/style50/) !

    style50 hello.c

## Comment soumettre

Inutile de soumettre celui-ci !