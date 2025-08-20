# Mario

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cWOkHQXw0JQ?modestbranding=0&amp;rel=0&amp;showinfo=0&amp;start=11"></iframe></div>

## Problème à résoudre

Vers la fin du monde 1-1 dans le jeu [Super Mario Bros.](https://fr.wikipedia.org/wiki/Super_Mario_Bros.) de Nintendo, Mario doit escalader une pyramide de briques alignées à droite, comme dans l'image ci-dessous :

![capture d'écran de Mario sautant sur une pyramide alignée à droite](https://cs50.harvard.edu/x/2024/psets/1/mario/less/pyramid.png)

Dans un fichier nommé `mario.c` dans un dossier appelé `mario-less`, implémentez un programme en C qui recrée cette pyramide en utilisant les dièses (`#`) pour les briques, comme dans l'image ci-dessous :

           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

Mais demandez à l'utilisateur de fournir un `int` pour la hauteur réelle de la pyramide, afin que le programme puisse également produire des pyramides plus courtes comme celle-ci :

      #
     ##
    ###

Redemandez à l'utilisateur, autant de fois que nécessaire, si sa saisie n'est pas supérieure à 0 ou n'est pas un `int`.

#### Astuces

- Rappelez-vous que vous pouvez obtenir un `int` d'un utilisateur avec `get_int`, qui est déclaré dans `cs50.h`.
- Rappelez-vous que vous pouvez imprimer une `string` avec `printf`, qui est déclaré dans `stdio.h`.

## Démo

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-WPrv7PFVLaLkJ2BU96uTEQKuA" src="https://asc
iinema.org/a/WPrv7PFVLaLkJ2BU96uTEQKuA.js"></script>

## Conseil

### Écrivez du code que vous savez compiler

Même si ce programme ne fait rien, il doit au moins se compiler avec `make` !

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {

    }

### Écrivez du pseudo-code avant d'écrire plus de code

Si vous ne savez pas comment résoudre le problème lui-même, décomposez-le en plus petits problèmes que vous pourrez probablement résoudre en premier. Par exemple, ce problème se résume en fait à deux problèmes :

1.  Demander à l'utilisateur la hauteur de la pyramide
2.  Imprimer une pyramide de cette hauteur

Écrivez donc du pseudo-code sous forme de commentaires qui vous rappelleront de faire cela :

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Demander à l'utilisateur la hauteur de la pyramide

        // Imprimer une pyramide de cette hauteur
    }

### Convertissez le pseudo-code en code

D'abord, réfléchissez à la façon dont vous pourriez demander à l'utilisateur la hauteur de la pyramide. Rappelez-vous qu'une boucle `do while` est utile lorsque vous souhaitez faire quelque chose au moins une fois, et éventuellement encore et encore, comme dans l'exemple ci-dessous :

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Demander à l'utilisateur la hauteur de la pyramide
        int n;
        do
        {
            n = get_int("Hauteur : ");
        }
        while (n < 1);

        // Imprimer une pyramide de cette hauteur
    }

Ensuite, réfléchissez à la façon dont vous pourriez imprimer une pyramide de cette hauteur, de haut en bas. Remarquez que la première ligne doit comporter une brique, la deuxième deux briques, et ainsi de suite. Il est probable que vous ayez besoin d'une boucle, comme dans l'exemple ci-dessous, même si vous ne savez pas encore (pour l'instant !) ce que vous allez mettre dans cette boucle. Ajoutez donc un peu plus de pseudo-code sous forme de commentaire pour le moment :

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Demander à l'utilisateur la hauteur de la pyramide
        int n;
        do
        {
            n = get_int("Hauteur : ");
        }
        while (n < 1);

        // Imprimer une pyramide de cette hauteur
        for (int i = 0; i < n; i++)
        {
            // Imprimer une ligne de briques
        }
    }

Comment imprimer cette ligne de briques ? Ne serait-il pas pratique d'avoir une fonction appelée `print_row` qui pourrait faire cela ? Supposons qu'il en existe une :

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int bricks);

    int main(void)
    {
        // Demander à l'utilisateur la hauteur de la pyramide
        int n;
        do
        {
            n = get_int("Hauteur : ");
        }
        while (n < 1);

        // Imprimer une pyramide de cette hauteur
        for (int i = 0; i < n; i++)
        {
            // Imprimer une ligne de briques
        }
    }

    void print_row(int bricks)
    {
        // Imprimer une ligne de briques
    }

Nous pourrions alors appeler cette fonction depuis `main`, comme dans l'exemple ci-dessous :

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int bricks);

    int main(void)
    {
        // Demander à l'utilisateur la hauteur de la pyramide
        int n;
        do
        {
            n = get_int("Hauteur : ");
        }
        while (n < 1);

        // Imprimer une pyramide de cette hauteur
        for (int i = 0; i < n; i++)
        {
            // Imprimer une ligne de briques
            print_row(i + 1);
        }
    }

    void print_row(int bricks)
    {
        // Imprimer une ligne de briques
    }

Mais pourquoi `i + 1` ?

Implémentons maintenant `print_row` :

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int bricks);

    int main(void)
    {
        // Demander à l'utilisateur la hauteur de la pyramide
        int n;
        do
        {
            n = get_int("Hauteur : ");
        }
        while (n < 1);

        // Imprimer une pyramide de cette hauteur
        for (int i = 0; i < n; i++)
        {
            // Imprimer une ligne de briques
            print_row(i + 1);
        }
    }

    void print_row(int bricks)
    {
        for (int i = 0; i < bricks; i++)
        {
            printf("#");
        }
        printf("\n");
    }

Mais pourquoi le `\n` à la fin ?

Malheureusement, ce code imprime une pyramide alignée à gauche, mais vous en avez besoin d'une alignée à droite ! Peut-être devrions-nous imprimer des espaces vides avant certaines des briques, pour les déplacer vers la droite ? Modifions `print_row` comme suit afin de pouvoir imprimer les deux :

    #include <cs50.h>
    #include <stdio.h>

    void print_row(int spaces, int bricks);

    int main(void)
    {
        // Demander à l'utilisateur la hauteur de la pyramide
        int n;
        do
        {
            n = get_int("Hauteur : ");
        }
        while (n < 1);

        // Imprimer une pyramide de cette hauteur
        for (int i = 0; i < n; i++)
        {
            // Imprimer une ligne de briques
        }
    }

    

## Procédure pas à pas

<div class="alert alert-info" data-alert="info" role="alert"><p>Remarque, cette procédure indique que votre programme doit inviter l’utilisateur à indiquer la hauteur d’une pyramide et doit <em>de nouveau</em> l’inviter si l’utilisateur saisit une valeur inférieure à 1 ou supérieure à 8. La spécification ne requiert que de redemander à l’utilisateur s’il saisit une valeur inférieure à 1.</p></div>

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/NAs4FIWkJ4s?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Procédure de test

Votre code fonctionne-t-il comme prévu lorsque vous saisissez&nbsp;:

- `-1` ou d’autres nombres négatifs&nbsp;?
- `0`&nbsp;?
- `1` ou d’autres nombres positifs&nbsp;?
- des lettres ou des mots&nbsp;?
- aucune entrée (en appuyant seulement sur Entrée)&nbsp;?

### Exactitude

Dans votre terminal, exécutez la commande suivante pour vérifier l’exactitude de votre travail.

    check50 cs50/problems/2024/x/mario/less

### Style

Exécutez la commande suivante pour évaluer le style de votre code à l’aide de `style50`.

    style50 mario.c

## Procédure d’envoi

Dans votre terminal, exécutez la commande suivante pour soumettre votre travail.

    submit50 cs50/problems/2024/x/mario/less

