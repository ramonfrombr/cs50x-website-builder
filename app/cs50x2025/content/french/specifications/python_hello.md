# Bonjour, à nouveau

## Problème à résoudre

Dans un fichier nommé `hello.py` dans un dossier nommé `sentimental-hello`, implémentez un programme qui demande à un utilisateur son nom, puis affiche `hello, untel`, où `untel` est son nom, exactement comme vous l’avez fait dans [Problem Set 1](../../1/). Sauf que cette fois-ci, votre programme doit être écrit en Python !

### Astuces

- Rappelez-vous que vous pouvez obtenir une `str` d'un utilisateur avec `get_string`, qui est déclarée dans la bibliothèque `cs50`.
- Rappelez-vous que vous pouvez imprimer une `str` avec `print`.
- Rappelez-vous que vous pouvez créer des chaînes formatées en Python en ajoutant un `f` à une chaîne. Par exemple, `f"{name}"` substituera (``interpolera'') la valeur de la variable `name` à l'endroit où vous avez écrit `{name}`.

## Démonstration

<script data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-gqi2voQFzbKlna6WkQR0G2W93" src="https://asciinema.org/a/gqi2voQFzbKlna6WkQR0G2W93.js"></script>

## Comment tester

Bien que `check50` soit disponible pour ce problème, nous vous encourageons à d’abord tester votre code vous-même pour chacun des éléments suivants :

- Exécutez votre programme en tant que `python hello.py` et attendez l’invite pour saisir une entrée. Tapez `David` et appuyez sur Entrée. Votre programme doit générer `hello, David`.
- Exécutez votre programme en tant que `python hello.py` et attendez l’invite pour saisir une entrée. Tapez `Inno` et appuyez sur Entrée. Votre programme doit générer `hello, Inno`.
- Exécutez votre programme en tant que `python hello.py` et attendez l’invite pour saisir une entrée. Tapez `Kamryn` et appuyez sur Entrée. Votre programme doit générer `hello, Kamryn`.

### Exactitude

    check50 cs50/problems/2024/x/sentimental/hello

### Style

    style50 hello.py

## Comment soumettre

    submit50 cs50/problems/2024/x/sentimental/hello