# Crédit

![Personne tenant des cartes de crédit](https://cs50.harvard.edu/x/2024/psets/1/credit/credit_cards.jpeg)

## Problème à résoudre

Une carte de crédit (ou de débit) est bien entendu une carte en plastique qui vous permet de payer des biens et des services. Un numéro est imprimé sur cette carte. Il est également stocké dans une base de données quelque part, ainsi, lorsque votre carte est utilisée pour acheter quelque chose, le créancier sait à qui envoyer la facture. Il y a beaucoup de personnes qui ont des cartes de crédit dans ce monde, donc ces numéros sont assez longs : American Express utilise des numéros à 15 chiffres, MasterCard utilise des numéros à 16 chiffres et Visa utilise des numéros à 13 et 16 chiffres. Et ce sont des nombres décimaux (de 0 à 9), pas binaires, ce qui signifie, par exemple, qu’American Express pourrait imprimer jusqu’à 10^15 = 1 000 000 000 000 000 de cartes différentes ! (C’est, euh, un quadrillion.)

En réalité, c’est un peu une exagération, parce que les numéros de carte de crédit ont en réalité une certaine structure. Tous les numéros American Express commencent par 34 ou 37 ; la plupart des numéros MasterCard commencent par 51, 52, 53, 54 ou 55 (ils ont également d’autres nombres de départ potentiels dont nous ne nous occuperons pas pour ce problème) ; et tous les numéros Visa commencent par 4. Mais les numéros de carte de crédit ont également une « somme de contrôle » intégrée, une relation mathématique entre au moins un nombre et d’autres. Cette somme de contrôle permet aux ordinateurs (ou aux humains qui aiment les maths) de détecter les fautes de frappe (par exemple, les transpositions), voire les numéros frauduleux, sans avoir à interroger une base de données, ce qui peut être lent. Bien sûr, un mathématicien malhonnête pourrait certainement créer un faux numéro qui respecte néanmoins la contrainte mathématique, donc une recherche dans la base de données reste nécessaire pour des vérifications plus rigoureuses.

Dans un fichier appelé `credit.c` dans un dossier appelé `credit`, implémentez un programme en C qui vérifie la validité d’un numéro de carte de crédit donné.

## Algorithme de Luhn

Alors, quelle est la formule secrète ? Eh bien, la plupart des cartes utilisent un algorithme inventé par Hans Peter Luhn d'IBM. Selon l’algorithme de Luhn, vous pouvez déterminer si un numéro de carte de crédit est (syntaxiquement) valide comme suit :

1.  Multipliez tous les deux chiffres par 2, en commençant par l’avant-dernier chiffre du numéro, puis additionnez les chiffres de ces produits.
2.  Ajoutez la somme à la somme des chiffres qui n’ont pas été multipliés par 2.
3.  Si le dernier chiffre du total est 0 (ou, plus formellement, si le total modulo 10 est congru à 0), le numéro est valide !

C’est un peu déroutant, alors essayons un exemple avec la carte Visa de David : 4003600000000014.

1.  Pour la discussion, soulignons d'abord tous les deux chiffres, en commençant par l'avant-dernier chiffre du numéro :

4003600000000014

D'accord, multiplions chacun des chiffres soulignés par 2 :

1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

Cela nous donne :

2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

Additionnons maintenant les chiffres de ces produits (c'est-à-dire, pas les produits eux-mêmes) :

2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

2.  Ajoutons maintenant cette somme (13) à la somme des chiffres qui n'ont pas été multipliés par 2 (en partant de la fin) :

13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

3.  Ouais, le dernier chiffre de cette somme (20) est un 0, donc la carte de David est légitime !

Donc, valider les numéros de carte de crédit n’est pas difficile, mais cela devient un peu fastidieux à la main. Écrivons un programme.

## Détails de l’implémentation

Dans le fichier appelé `credit.c` dans le répertoire `credit`, écrivez un programme qui invite l’utilisateur à saisir un numéro de carte de crédit, puis indique (via `printf`) s’il s’agit d’un numéro de carte American Express, MasterCard ou Visa valide, selon les définitions de chaque format. Afin que nous puissions automatiser certains tests de votre code, nous vous demandons que la dernière ligne de sortie de votre programme soit `AMEX\n` ou `MASTERCARD\n` ou `VISA\n` ou `INVALID\n`, rien de plus, rien de moins. Pour plus de simplicité, vous pouvez supposer que l'entrée de l'utilisateur sera entièrement numérique (c'est-à-dire, dépourvue de tirets, comme cela pourrait être imprimé sur une carte réelle) et qu'elle n'aura pas de zéros non significatifs. Mais ne supposez pas que l'entrée de l'utilisateur tiendra dans un `int` ! Il est préférable d'utiliser `get_long` de la bibliothèque de CS50 pour obtenir l'entrée des utilisateurs. (Pourquoi ?)

Considérez l'exemple ci-dessous de la façon dont votre propre programme devrait se comporter lorsqu'un numéro de carte de crédit valide (sans tirets) lui est passé.

    $ ./credit
    Numéro : 4003600000000014
    VISA

Maintenant, `get_long` lui-même rejettera les tirets (et plus) de toute façon :

    $ ./credit
    Numéro : 4003-6000-0000-0014
    Numéro : foo
    Numéro : 4003600000000014
    VISA

Mais c'est à vous de saisir les entrées qui ne sont pas des numéros de carte de crédit (par exemple, un numéro de téléphone), même si elles sont numériques :

    $ ./credit
    Numéro : 6176292929
    INVALID

Testez votre programme avec de nombreuses entrées valides et non valides. (Nous le ferons certainement !) Voici quelques [numéros de carte](https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/test-transactions/#standard-test-cards) recommandés par PayPal pour les tests.

Si votre programme ne se comporte pas correctement sur certaines entrées (ou ne se compile pas du tout), il est temps de déboguer !

### Procédure pas à pas

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/dF7wNjsRBjI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

### Comment tester votre code

Vous pouvez également exécuter ce qui suit pour évaluer l'exactitude de votre code à l'aide de `check50`. Mais assurez-vous de le compiler et de le tester vous-même !

### Exactitude

Dans votre terminal, exécutez ce qui suit pour vérifier l'exactitude de votre travail.

    check50 cs50/problems/2024/x/credit

### Style

Exécutez ce qui suit pour évaluer le style de votre code à l’aide de `style50`.

    style50 credit.c

## Comment soumettre

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail.

    submit50 cs50/problems/2024/x/credit