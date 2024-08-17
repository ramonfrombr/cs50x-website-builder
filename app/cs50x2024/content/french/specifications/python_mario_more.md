# Mario

![capture d'écran de Mario sautant au dessus d'une pyramide](https://cs50.harvard.edu/x/2024/psets/6/mario/more/pyramids.png)

## Problème à résoudre

Dans un fichier appelé `mario.py` dans un dossier appelé `sentimental-mario-more`, écrivez un programme qui recrée une demi-pyramide en utilisant des dièses (`#`) pour les blocs, exactement comme vous l'avez fait dans [l'ensemble de problèmes 1](../../../1/). Cette fois, votre programme doit être écrit en Python !

## Démonstration

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-B0CE4bjPGR19PoRKUe5ZF9VoM" src="https://asciinema.org/a/B0CE4bjPGR19PoRKUe5ZF9VoM.js"></script>

## Spécification

- Pour rendre les choses plus intéressantes, demandez d'abord à l'utilisateur avec `get_int` la hauteur de la demi-pyramide, un entier positif compris entre `1` et `8` inclus. (La hauteur des demi-pyramides représentées ci-dessus est `4`, la largeur de chaque demi-pyramide est `4`, avec un écart de taille `2` les séparant).
- Si l'utilisateur ne fournit pas un entier positif inférieur ou égal à `8`, vous devez lui redemander le même numéro.
- Ensuite, générez (avec l'aide de `print` et d'une ou plusieurs boucles) les demi-pyramides souhaitées.
- Prenez soin d'aligner le coin inférieur gauche de votre pyramide avec le bord gauche de la fenêtre de votre terminal, et assurez-vous qu'il y a deux espaces entre les deux pyramides, et qu'il n'y a pas d'espaces supplémentaires après le dernier ensemble de dièses sur chaque ligne.

## Comment tester

Bien que `check50` soit disponible pour ce problème, nous vous encourageons à tester d'abord votre code vous-même pour chacun des éléments suivants :

- Exécutez votre programme en tant que `python mario.py` et attendez une invite de saisie. Tapez `-1` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme invalide, en demandant à l'utilisateur de saisir un autre nombre.
- Exécutez votre programme en tant que `python mario.py` et attendez une invite de saisie. Tapez `0` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme invalide, en demandant à l'utilisateur de saisir un autre nombre.
- Exécutez votre programme en tant que `python mario.py` et attendez une invite de saisie. Tapez `1` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée sur le coin inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

        #  #

- Exécutez votre programme en tant que `python mario.py` et attendez une invite de saisie. Tapez `2` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée sur le coin inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

         #  #
        ##  ##

- Exécutez votre programme en tant que `python mario.py` et attendez une invite de saisie. Tapez `8` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée sur le coin inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

               #  #
              ##  ##
             ###  ###
            ####  ####
           #####  #####
          ######  ######
         #######  #######
        ########  ########

- Exécutez votre programme en tant que `python mario.py` et attendez une invite de saisie. Tapez `9` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme invalide, en demandant à l'utilisateur de saisir un autre nombre. Ensuite, tapez `2` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée sur le coin inférieur gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

         #  #
        ##  ##

- Exécutez votre programme en tant que `python mario.py` et attendez une invite de saisie. Tapez `foo` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme invalide, en demandant à l'utilisateur de saisir un autre nombre.
- Exécutez votre programme en tant que `python mario.py` et attendez une invite de saisie. Ne tapez rien et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme invalide, en demandant à l'utilisateur de saisir un autre nombre.

### Justesse

    check50 cs50/problems/2024/x/sentimental/mario/more

### Style

    style50 mario.py

## Comment soumettre

    submit50 cs50/problems/2024/x/sentimental/mario/more