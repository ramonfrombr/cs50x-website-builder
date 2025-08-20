# Mario

![capture d'écran de Mario sautant au-dessus d'une pyramide](https://cs50.harvard.edu/x/2024/psets/6/mario/less/pyramid.png)

## Problème à résoudre

Dans un fichier appelé `mario.py` dans un dossier appelé `sentimental-mario-less`, écrivez un programme qui recrée une demi-pyramide en utilisant des dièses (`#`) comme blocs, exactement comme vous l'avez fait dans [l'exercice 1](../../../1/). Cette fois-ci, votre programme doit être écrit en Python !

## Démonstration

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-sUSilCTveD7JTV2lOZ7eIqKbo" src="https://asciinema.org/a/sUSilCTveD7JTV2lOZ7eIqKbo.js"></script>

## Spécifications

- Pour rendre les choses plus intéressantes, demandez d’abord à l’utilisateur de saisir une hauteur de demi-pyramide positive comprise entre `1` et `8`, inclusivement, à l'aide de `get_int`.
- Si l’utilisateur ne fournit pas un nombre entier positif ou s'il est supérieur à `8`, vous devez demander à nouveau de saisir une autre valeur.
- Ensuite, générez (à l'aide de `print` et d'une ou plusieurs boucles) la demi-pyramide souhaitée.
- Prenez soin d'aligner le coin inférieur gauche de votre demi-pyramide avec le bord gauche de votre fenêtre de terminal.

## Comment tester

Bien que `check50` soit disponible pour ce problème, nous vous encourageons à tester d'abord votre code vous-même pour chacun des cas suivants.

- Exécutez votre programme avec `python mario.py` et attendez que l’utilisateur saisisse une valeur. Tapez `-1` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme non valide en demandant à l'utilisateur de saisir un autre nombre.
- Exécutez votre programme avec `python mario.py` et attendez que l’utilisateur saisisse une valeur. Tapez `0` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme non valide en demandant à l'utilisateur de saisir un autre nombre.
- Exécutez votre programme avec `python mario.py` et attendez que l’utilisateur saisisse une valeur. Tapez `1` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée en bas à gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

        #

- Exécutez votre programme avec `python mario.py` et attendez que l’utilisateur saisisse une valeur. Tapez `2` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée en bas à gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

         #
        ##

- Exécutez votre programme avec `python mario.py` et attendez que l’utilisateur saisisse une valeur. Tapez `8` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée en bas à gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

               #
              ##
             ###
            ####
           #####
          ######
         #######
        ########

- Exécutez votre programme avec `python mario.py` et attendez que l’utilisateur saisisse une valeur. Tapez `9` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme non valide en demandant à l'utilisateur de saisir un autre nombre. Ensuite, tapez `2` et appuyez sur Entrée. Votre programme doit générer la sortie ci-dessous. Assurez-vous que la pyramide est alignée en bas à gauche de votre terminal et qu'il n'y a pas d'espaces supplémentaires à la fin de chaque ligne.

         #
        ##

- Exécutez votre programme avec `python mario.py` et attendez que l’utilisateur saisisse une valeur. Tapez `foo` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme non valide en demandant à l'utilisateur de saisir un autre nombre.
- Exécutez votre programme avec `python mario.py` et attendez que l’utilisateur saisisse une valeur. N'entrez rien et appuyez sur Enter. Votre programme doit rejeter cette entrée comme non valide en demandant à l'utilisateur de saisir un autre nombre.

### Exactitude

    check50 cs50/problems/2024/x/sentimental/mario/less

### Style

    style50 mario.py

## Comment soumettre

    submit50 cs50/problems/2024/x/sentimental/mario/less