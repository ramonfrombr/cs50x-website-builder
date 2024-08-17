# Substitution

## Problème à résoudre

Dans un chiffrement par substitution, nous « chiffrons » (c'est-à-dire que nous dissimulons de manière réversible) un message en remplaçant chaque lettre par une autre lettre. Pour ce faire, nous utilisons une _clé_ : dans ce cas, un mappage de chacune des lettres de l'alphabet à la lettre à laquelle elle doit correspondre lorsque nous la chiffrons. Pour « déchiffrer » le message, le destinataire du message doit connaître la clé afin de pouvoir inverser le processus : traduire le texte chiffré (généralement appelé _ciphertext_) en message d'origine (généralement appelé _plaintext_).

Une clé, par exemple, peut être la chaîne `NQXPOMAFTRHLZGECYJIUWSKDVB`. Cette clé de 26 caractères signifie que `A` (la première lettre de l'alphabet) doit être convertie en `N` (le premier caractère de la clé), `B` (la deuxième lettre de l'alphabet) doit être convertie en `Q` (le deuxième caractère de la clé), et ainsi de suite.

Un message comme `HELLO`, serait alors chiffré en `FOLLE`, en remplaçant chacune des lettres selon le mappage déterminé par la clé.

Dans un fichier appelé `substitution.c` dans un dossier appelé `substitution`, créez un programme qui vous permet de chiffrer des messages à l'aide d'un chiffrement par substitution. Au moment où l'utilisateur exécute le programme, il doit décider, en fournissant un argument de ligne de commande, quelle doit être la clé du message secret qu'il fournira à l'exécution.

## Démo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-HWzT4fngSv4KtdNFgfgpdLxZY" src="https://asciinema.org/a/HWzT4fngSv4KtdNFgfgpdLxZY.js"></script>

## Spécification

Concevez et implémentez un programme, `substitution`, qui chiffre des messages à l'aide d'un chiffrement par substitution.

- Implémentez votre programme dans un fichier appelé `substitution.c` dans un répertoire appelé `substitution`.
- Votre programme doit accepter un seul argument de ligne de commande, la clé à utiliser pour la substitution. La clé elle-même doit être insensible à la casse, donc le fait qu'un caractère dans la clé soit en majuscules ou en minuscules ne doit pas affecter le comportement de votre programme.
- Si votre programme est exécuté sans aucun argument de ligne de commande ou avec plus d'un argument de ligne de commande, votre programme doit imprimer un message d'erreur de votre choix (avec `printf`) et renvoyer immédiatement de `main` une valeur de `1` (qui a tendance à signifier une erreur).
- Si la clé est invalide (car elle ne contient pas 26 caractères, qu'elle contient un caractère qui n'est pas un caractère alphabétique ou qu'elle ne contient pas chaque lettre exactement une fois), votre programme doit imprimer un message d'erreur de votre choix (avec `printf`) et renvoyer immédiatement de `main` une valeur de `1`.
- Votre programme doit générer `plaintext:` (sans nouvelle ligne), puis demander à l'utilisateur une `string` de texte brut (en utilisant `get_string`).
- Votre programme doit générer `ciphertext:` (sans nouvelle ligne) suivi du texte chiffré correspondant au texte brut, chaque caractère alphabétique du texte brut étant remplacé par le caractère correspondant dans le texte chiffré ; les caractères non alphabétiques doivent être générés inchangés.
- Votre programme doit conserver la casse : les lettres majuscules doivent rester des lettres majuscules ; les lettres minuscules doivent rester des lettres minuscules.
- Après avoir généré le texte chiffré, vous devez imprimer une nouvelle ligne. Votre programme doit alors quitter en renvoyant `0` à partir de `main`.

Vous trouverez peut-être utile une ou plusieurs fonctions déclarées dans `ctype.h`, par [manual.cs50.io](https://manual.cs50.io/).

## Procédure pas à pas

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/cXAoZAsgxJ4?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Comment tester

### Justesse

Dans votre terminal, exécutez ce qui suit pour vérifier la justesse de votre travail.

    check50 cs50/problems/2024/x/substitution

#### Comment utiliser `debug50`

Vous cherchez à exécuter `debug50` ? Vous pouvez le faire comme suit, après avoir compilé votre code avec succès avec `make`,

    debug50 ./substitution KEY

où `KEY` est la clé que vous donnez comme argument de ligne de commande à votre programme. Notez que l'exécution

    debug50 ./substitution

va (idéalement !) mettre fin à votre programme en invitant l'utilisateur à saisir une clé.

### Style

Exécutez ce qui suit pour évaluer le style de votre code à l'aide de `style50`.

    style50 substitution.c

## Comment soumettre

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail.

    submit50 cs50/problems/2024/x/substitution