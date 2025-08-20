# Bonjour, c’est moi

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/YQHsXMglC9A?modestbranding=0&amp;rel=0&amp;showinfo=0&amp;start=74"></iframe></div>

## Problème à résoudre

Dans un fichier nommé `hello.c`, dans un dossier nommé `me`, implémentez un programme en C qui demande le nom de l’utilisateur, puis salue cet utilisateur. Par exemple, si le nom de l’utilisateur est Adele, votre programme doit afficher `bonjour, Adele\n` !

#### Conseils

- Rappelez-vous que vous pouvez obtenir une `chaîne` de la part d’un utilisateur avec `get_string`, qui est déclarée dans `cs50.h`.
- Rappelez-vous que vous pouvez afficher une `chaîne` avec `printf`, qui est déclarée dans `stdio.h`.
- Rappelez-vous que vous pouvez formater une `chaîne` avec `printf` avec `%s`.

## Démonstration

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-Jn4egWrG0Rvuzo9d2Rs0qpkcL" src="https://asc
iinema.org/a/Jn4egWrG0Rvuzo9d2Rs0qpkcL.js"></script>

## Comment commencer

Exécutez `cd` tout seul dans votre fenêtre de terminal. Vous devriez vous apercevoir que l’invite de votre fenêtre de terminal ressemble à ce qui suit :

    $

Ensuite, exécutez

    mkdir moi

pour créer un dossier nommé `moi` dans votre espace de code.

Puis exécutez

    cd moi

pour changer de répertoire et entrer dans ce dossier. Vous devriez maintenant voir votre invite de terminal comme `moi/ $`. Vous pouvez maintenant exécuter

    code hello.c

pour créer un fichier nommé `hello.c` dans lequel vous pouvez écrire votre code.

## Procédure

Voici une « procédure » (c’est-à-dire un aperçu) de ce problème, si vous souhaitez également avoir un aperçu verbal de ce qu’il faut faire !

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/wSk1KSDUEYA?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Comment tester

### Justesse

Dans votre terminal, exécutez ce qui suit pour vérifier la justesse de votre travail :

    check50 cs50/problems/2024/x/moi

### Style

    style50 hello.c

## Comment soumettre

    submit50 cs50/problems/2024/x/moi