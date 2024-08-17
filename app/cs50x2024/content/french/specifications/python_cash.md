# Argent

## Problème à résoudre

Dans un fichier appelé `cash.py` dans un dossier appelé `sentimental-cash`, écrivez un programme qui demande à l'utilisateur combien d'argent il lui est dû, puis affiche le nombre minimal de pièces avec lesquelles cette monnaie peut être rendue. Vous pouvez le faire exactement comme vous l'avez fait dans [l'ensemble des problèmes 1](../../1/), sauf que votre programme doit cette fois être écrit en Python et que vous devez supposer que l'utilisateur saisira son argent en dollars (par exemple, 0,50 dollar au lieu de 50 cents).

## Démonstration

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-eoFGGVR2gwl2jvyj7sHchxUmW" src="https://asciinema.org/a/eoFGGVR2gwl2jvyj7sHchxUmW.js"></script>

## Spécification

- Utilisez `get_float` de la bibliothèque CS50 pour obtenir l'entrée de l'utilisateur et `print` pour afficher votre réponse. Supposez que les seules pièces disponibles sont les quarts (25&cent;), les dimes (10&cent;), les nickels (5&cent;) et les pennies (1&cent;).
  - Nous vous demandons d'utiliser `get_float` afin que vous puissiez gérer les dollars et les cents, même sans signe dollar. En d'autres termes, si un client a une dette de 9,75 $ (comme dans le cas où un journal coûte 25 &cent; mais que le client paie avec un billet de 10 $), supposons que l'entrée de votre programme sera `9,75` et non `9,75 $ ' ou `975`. Cependant, si un client a une dette de 9 $ exactement, supposons que l'entrée de votre programme sera `9,00` ou simplement `9` mais, encore une fois, pas `9 $` ou `900`. Bien sûr, de par la nature des valeurs à virgule flottante, votre programme fonctionnera probablement également avec des entrées comme `9,0` et `9,000`; vous n'avez pas à vous soucier de vérifier si l'entrée de l'utilisateur est « formatée » comme il se doit pour l'argent.
- Si l'utilisateur ne parvient pas à fournir une valeur non négative, votre programme doit redemander à l'utilisateur un montant valide, encore et encore, jusqu'à ce que l'utilisateur s'y conforme.
- Incidemment, afin que nous puissions automatiser certains tests de votre code, nous demandons que la dernière ligne de sortie de votre programme soit uniquement le nombre minimum de pièces possible : un entier suivi d'une nouvelle ligne.

## Comment tester

Bien que `check50` soit disponible pour ce problème, nous vous encourageons à d'abord tester votre code vous-même pour chacun des éléments suivants.

- Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour la saisie. Tapez `0,41` et appuyez sur Entrée. Votre programme devrait sortir `4`.
- Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour la saisie. Tapez `0,01` et appuyez sur Entrée. Votre programme devrait sortir `1`.
- Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour la saisie. Tapez `0,15` et appuyez sur Entrée. Votre programme devrait sortir `2`.
- Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour la saisie. Tapez `1,60` et appuyez sur Entrée. Votre programme devrait sortir `7`.
- Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour la saisie. Tapez `23` et appuyez sur Entrée. Votre programme devrait sortir `92`.
- Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour la saisie. Tapez `4,2` et appuyez sur Entrée. Votre programme devrait sortir `18`.
- Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour la saisie. Tapez `-1` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme non valide, en demandant à l'utilisateur de saisir un autre nombre.
- Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour la saisie. Tapez `foo` et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme non valide, en demandant à l'utilisateur de saisir un autre nombre.
- Exécutez votre programme en tant que `python cash.py`, et attendez une invite pour la saisie. N'écrivez rien et appuyez sur Entrée. Votre programme doit rejeter cette entrée comme non valide, en demandant à l'utilisateur de saisir un autre nombre.

### Exactitude

    check50 cs50/problems/2024/x/sentimental/cash

### Style

    style50 cash.py

## Comment soumettre

    submit50 cs50/problems/2024/x/sentimental/cash