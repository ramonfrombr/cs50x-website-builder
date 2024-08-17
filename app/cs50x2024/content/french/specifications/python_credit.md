# Crédit

## Problème à résoudre

Dans un fichier nommé `credit.py` dans un dossier nommé `sentimental-credit`, écrivez un programme qui demande à l'utilisateur un numéro de carte de crédit et indique (via `print`) s'il s'agit d'un numéro de carte American Express, MasterCard ou Visa valide, exactement comme vous l'avez fait dans [Problem Set 1](../../1/). Cette fois, votre programme doit être écrit en Python !

## Démonstration

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-QYLr1R1RDLO9QkPF2XFODLkq4" src="https://asciinema.org/a/QYLr1R1RDLO9QkPF2XFODLkq4.js"></script>

## Spécification

- Afin que nous puissions automatiser certains tests de votre code, nous vous demandons que la dernière ligne de sortie de votre programme soit `AMEX\n` ou `MASTERCARD\n` ou `VISA\n` ou `INVALID\n`, rien de plus, rien de moins.
- Pour simplifier, vous pouvez supposer que l'entrée de l'utilisateur sera entièrement numérique (c'est-à-dire dépourvue de tirets, comme ils pourraient être imprimés sur une carte réelle).
- Il est préférable d'utiliser `get_int` ou `get_string` de la bibliothèque de CS50 pour obtenir l'entrée de l'utilisateur, en fonction de la façon dont vous décidez d'implémenter celui-ci.

## Astuces

- Il est possible d'utiliser des expressions régulières pour valider l'entrée de l'utilisateur. Vous pouvez utiliser le module [`re`](https://docs.python.org/3/library/re.html) de Python, par exemple, pour vérifier si l'entrée de l'utilisateur est bien une séquence de chiffres de la bonne longueur.

## Comment tester

Bien que `check50` soit disponible pour ce problème, nous vous encourageons à tester d'abord votre code par vous-même pour chacun des éléments suivants.

- Exécutez votre programme en tant que `python credit.py`, et attendez une invite pour l'entrée. Tapez `378282246310005` et appuyez sur Entrée. Votre programme doit sortir `AMEX`.
- Exécutez votre programme en tant que `python credit.py`, et attendez une invite pour l'entrée. Tapez `371449635398431` et appuyez sur Entrée. Votre programme doit sortir `AMEX`.
- Exécutez votre programme en tant que `python credit.py`, et attendez une invite pour l'entrée. Tapez `5555555555554444` et appuyez sur Entrée. Votre programme doit sortir `MASTERCARD`.
- Exécutez votre programme en tant que `python credit.py`, et attendez une invite pour l'entrée. Tapez `5105105105105100` et appuyez sur Entrée. Votre programme doit sortir `MASTERCARD`.
- Exécutez votre programme en tant que `python credit.py`, et attendez une invite pour l'entrée. Tapez `4111111111111111` et appuyez sur Entrée. Votre programme doit sortir `VISA`.
- Exécutez votre programme en tant que `python credit.py`, et attendez une invite pour l'entrée. Tapez `4012888888881881` et appuyez sur Entrée. Votre programme doit sortir `VISA`.
- Exécutez votre programme en tant que `python credit.py`, et attendez une invite pour l'entrée. Tapez `1234567890` et appuyez sur Entrée. Votre programme doit sortir `INVALID`.

### Correction

    check50 cs50/problems/2024/x/sentimental/credit

### Style

    style50 credit.py

## Comment soumettre

    submit50 cs50/problems/2024/x/sentimental/credit