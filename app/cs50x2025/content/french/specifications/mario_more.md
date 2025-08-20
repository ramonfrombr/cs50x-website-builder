# Mario

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cWOkHQXw0JQ?modestbranding=0&amp;rel=0&amp;showinfo=0&amp;start=11"></iframe></div>

## Problème à résoudre

Vers le début du monde 1-1 dans Super Mario Bros de Nintendo, Mario doit sauter par-dessus des pyramides de blocs adjacentes, comme indiqué ci-dessous.

![capture d'écran de Mario sautant par-dessus des pyramides adjacentes](https://cs50.harvard.edu/x/2024/psets/1/mario/more/pyramids.png)

Dans un fichier nommé `mario.c` dans un dossier nommé `mario-more`, implémentez un programme en C qui recrée cette pyramide, en utilisant des dièses (`#`) pour les briques, comme ci-dessous :

       #  #
      ##  ##
     ###  ###
    ####  ####

Et permet à l'utilisateur de décider la hauteur des pyramides en lui demandant d'abord un `int` positif compris entre 1 et 8, inclus.

#### Exemples

Voici comment le programme pourrait fonctionner si l'utilisateur saisit ``8` lorsqu'on lui demande :

    $ ./mario
    Height: 8
           #  #
          ##  ##
         ###  ###
        ####  ####
       #####  #####
      ######  ######
     #######  #######
    ########  ########

Voici comment le programme pourrait fonctionner si l'utilisateur saisit `4` lorsqu'on lui demande :

    $ ./mario
    Height: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Voici comment le programme pourrait fonctionner si l'utilisateur saisit `2` lorsqu'on lui demande :

    $ ./mario
    Height: 2
     #  #
    ##  ##

Et voici comment le programme pourrait fonctionner si l'utilisateur saisit `1` lorsqu'on lui demande :

    $ ./mario
    Height: 1
    #  #

Si l'utilisateur ne saisit pas en fait un nombre entier positif compris entre 1 et 8, inclus, lorsqu'on lui demande, le programme doit lui redemander jusqu'à ce qu'il coopère :

    $ ./mario
    Height: -1
    Height: 0
    Height: 42
    Height: 50
    Height: 4
       #  #
      ##  ##
     ###  ###
    ####  ####

Notez que la largeur de « l'écart » entre les pyramides adjacentes est égale à la largeur de deux dièses, quelle que soit la hauteur des pyramides.

### Procédure

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/FzN9RAjYG_Q?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Comment tester votre code

Votre code fonctionne-t-il comme prescrit lorsque vous saisissez :

- `-1` (ou autres nombres négatifs) ?
- `0` ?
- `1` à `8` ?
- `9` ou autres nombres positifs ?
- des lettres ou des mots ?
- aucune entrée du tout, lorsque vous appuyez uniquement sur Entrée ?

Vous pouvez également exécuter ce qui suit pour évaluer l'exactitude de votre code à l'aide de `check50`. Toutefois, veillez à le compiler et à le tester vous-même !

### Correction

Dans votre terminal, exécutez ce qui suit pour vérifier l'exactitude de votre travail.

    check50 cs50/problems/2024/x/mario/more

### Style

Exécutez ce qui suit pour évaluer le style de votre code à l'aide de `style50`.

    style50 mario.c

## Comment soumettre

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail.

    submit50 cs50/problems/2024/x/mario/more