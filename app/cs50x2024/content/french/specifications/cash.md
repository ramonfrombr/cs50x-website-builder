# Argent

![Pièces américaines](https://cs50.harvard.edu/x/2024/psets/1/cash/coins.jpg)

## Problème à résoudre

Imaginez que vous travailliez dans un commerce et qu'un client vous donne 1,00 $ (100 cents) pour des bonbons qui coûtent 0,50 $ (50 cents). Vous devrez lui rendre sa « monnaie », la somme restante après avoir payé le prix des bonbons. Vous voudrez probablement rendre le moins de pièces possible à chaque client afin de ne pas en manquer (ou de ne pas l'énerver !). Dans un fichier appelé `cash.c` dans un dossier appelé `cash`, implémentez un programme en C qui imprime le nombre minimal de pièces nécessaires pour rendre le montant de monnaie indiqué, en cents, comme dans les exemples ci-dessous :

    Monnaie due : 25
    1

Mais invitez l'utilisateur à saisir un nombre entier supérieur à 0, afin que le programme fonctionne pour n'importe quel montant de monnaie :

    Monnaie due : 70
    4

Réinvitez l'utilisateur à saisir un nombre, autant de fois que nécessaire, si son entrée n'est pas supérieure ou égale à 0 (ou s'il ne s'agit pas d'un nombre entier).

## Démonstration

<script async="" data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-p6PlFqQgSWNWn4ggpIIaBOvIq" src="https://asciinema.org/a/p6PlFqQgSWNWn4ggpIIaBOvIq.js"></script>

## Algorithmes gloutons

Heureusement, l'informatique a fourni aux caissiers du monde entier des moyens de minimiser le nombre de pièces dues : les algorithmes gloutons.

Selon l'Institut national des normes et de la technologie (NIST), un algorithme glouton est un algorithme « qui prend toujours la meilleure solution immédiate ou locale tout en trouvant une réponse. Les algorithmes gloutons trouvent la solution globale ou optimale pour certains problèmes d'optimisation, mais peuvent trouver des solutions moins qu'optimales pour certaines instances d'autres problèmes ».

Qu'est-ce que cela signifie ? Eh bien, supposons qu'un caissier doive rendre de la monnaie à un client et que dans le tiroir de ce caissier se trouvent des pièces de 25 cents (25 ¢), 10 cents (10 ¢), 5 cents (5 ¢) et 1 cent (1 ¢). Le problème à résoudre est de décider quelles pièces et combien de chaque pièce doivent être rendues au client. Imaginez un caissier « glouton » comme quelqu'un qui veut prendre la plus grosse bouchée possible de ce problème à chaque fois qu'il prend une pièce dans le tiroir. Par exemple, si un client doit recevoir 41 ¢, la première bouchée la plus importante (c'est-à-dire la meilleure solution immédiate ou locale) possible est de 25 ¢. (Cette bouchée est « meilleure » dans la mesure où elle nous rapproche de 0 ¢ plus rapidement que n'importe quelle autre pièce). Notez qu'une bouchée de cette taille réduirait le problème de 41 ¢ à un problème de 16 ¢, car 41 - 25 = 16. C'est-à-dire que le reste est un problème similaire mais plus petit. Inutile de dire qu'une autre bouchée de 25 ¢ serait trop importante (en supposant que le caissier préfère ne pas perdre d'argent), et notre caissier glouton passerait donc à une bouchée de 10 ¢, ce qui lui laisserait un problème de 6 ¢. À ce stade, la gloutonnerie appelle une bouchée de 5 ¢ suivie d'une bouchée de 1 ¢, auquel cas le problème est résolu. Le client reçoit une pièce de 25 cents, une pièce de 10 cents, une pièce de 5 cents et une pièce de 1 cent : quatre pièces au total.

Il s'avère que cette approche gloutonne (c'est-à-dire l'algorithme) n'est pas seulement optimale localement mais aussi globalement pour la monnaie américaine (et aussi pour celle de l'Union européenne). Autrement dit, tant qu'un caissier a suffisamment de chaque pièce, cette approche du plus grand au plus petit donnera le moins de pièces possible. Combien de pièces ? Eh bien, c'est à vous de nous le dire !

## Conseils

### Écrivez du code dont vous savez qu'il va compiler

Même si ce programme ne fera rien, il doit au moins compiler avec `make` !

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {

    }

Remarquez que vous avez maintenant inclus `cs50.h` et `stdio.h`, deux « fichiers d'en-tête » qui vous donneront accès à des fonctions qui pourraient vous aider à résoudre ce problème.

### Écrivez du pseudo-code avant d'écrire plus de code

Si vous ne savez pas comment résoudre le problème lui-même, décomposez-le en plus petits problèmes que vous pouvez probablement résoudre en premier. Par exemple, ce problème n'est en réalité qu'une poignée de problèmes :

1.  Invitez l'utilisateur à saisir la monnaie due, en cents.
2.  Calculez le nombre de pièces de 25 cents que vous devez donner au client. Soustrayez la valeur de ces pièces de 25 cents aux cents.
3.  Calculez le nombre de pièces de 10 cents que vous devez donner au client. Soustrayez la valeur de ces pièces de 10 cents aux cents restants.
4.  Calculez le nombre de pièces de 5 cents que vous devez donner au client. Soustrayez la valeur de ces pièces de 5 cents aux cents restants.
5.  Calculez le nombre de pièces de 1 cent que vous devez donner au client. Soustrayez la valeur de ces pièces de 1 cent aux cents restants.
6.  Faites la somme du nombre de pièces de 25 cents, 10 cents, 5 cents et 1 cent utilisées.
7.  Imprimez cette somme.

Voici l'algorithme glouton que vous pouvez utiliser pour résoudre ce problème, alors écrivons du pseudo-code sous forme de commentaires pour vous rappeler de faire exactement cela :

    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Invitez l'utilisateur à saisir la monnaie due, en cents

        // Calculez le nombre de pièces de 25 cents que vous devez donner au client
        // Soustrayez la valeur de ces pièces de 25 cents aux cents

        // Calculez le nombre de pièces de 10 cents que vous devez donner au client
        // Soustrayez la valeur de ces pièces de 10 cents aux cents restants

        // Calculez le nombre de pièces de 5 cents que vous devez donner au client
        // Soustrayez la valeur de ces pièces de 5 cents aux cents restants

        // Calculez le nombre de pièces de 1 cent que vous devez donner au client
        // Soustrayez la valeur de ces pièces de 1 cent aux cents restants

        // Faites la somme du nombre de pièces de 25 cents, 10 cents, 5 cents et 1 cent utilisées
        // Imprimez cette somme
    }

### Convertir le pseudo-code en code

Premièrement, pensez à la manière dont vous pourriez demander à l'utilisateur les centimes qui lui sont dus. Rappelez-vous qu'une boucle `do while` est utile lorsque vous voulez faire quelque chose au moins une fois, et peut-être encore et encore, comme dans l'exemple ci-dessous :

```c
    #include <cs50.h>
    #include <stdio.h>

    int main(void)
    {
        // Demander à l'utilisateur le montant de la monnaie due, en centimes
        int cents;
        do
        {
            cents = get_int("Monnaie due : ");
        }
        while (cents < 0);
    }
```

Il est judicieux de vous arrêter ici et de `faire` votre programme. Testez pour être sûr que votre programme se compile et qu'il vous redemande si vous entrez moins de 0 centime (ou si vous entrez une valeur comme « chat »).

Ensuite, réfléchissez à la manière de calculer le nombre de quarts à donner au client. Puisque nous utilisons un algorithme glouton, cette question devient : « quel est le _plus grand_ nombre de quarts que vous pourriez lui donner ?». Vous _pourriez_ écrire une solution à ce problème dans votre fonction `main`. Mais cela pourrait éclaircir votre réflexion si vous écriviez une nouvelle fonction : une appelée `calculate_quarters`. De cette façon, vous pouvez mieux vous concentrer sur la logique de calcul des quarts. Plus tard, vous pouvez intégrer cette fonction dans votre solution plus large.

```c
int calculate_quarters(int cents)
{
    // Calculer le nombre de quarts à donner au client
}
```

Notez que cette fonction est en effet nommée `calculate_quarters`. Par `int cents` entre parenthèses, elle prend un `int` appelé `cents` en entrée. Et, selon le `int` devant son nom, elle doit également « retourner » un `int`. Autrement dit, la sortie de cette fonction est un entier : le nombre de quarts qui entrent dans les centimes. Si cette idée vous intrigue, rappelez-vous qu'il existe plusieurs exemples de programmes dans le [Code source](https://github.com/cs50/lectures/tree/2023/fall/1/src1) de la semaine 1 qui illustrent comment les fonctions peuvent retourner une valeur.

Maintenant, considérez cette façon d'implémenter `calculate_quarters` en ajoutant au nombre de quarts jusqu'à ce que nous n'ayons plus de centimes à convertir en quarts :

```c
int calculate_quarters(int cents)
{
    // Calculer le nombre de quarts à donner au client
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}
```

Certes, il existe au moins une façon plus simple de résoudre ce problème `calculate_quarters`. Mais nous vous laissons le soin de la découvrir !

Avec `calculate_quarters` fonctionnant comme prévu, vous pouvez intégrer cette fonction dans votre programme. Prenez soin de « déclarer » la « signature » de la fonction (c'est-à-dire `int calculate_quarters(int cents)`) au-dessus de votre fonction `main`, afin que vous puissiez effectivement utiliser `calculate_quarters` là-bas tout en la définissant plus tard, en dessous de `main`.

```c
#include <cs50.h>
#include <stdio.h>

int calculate_quarters(int cents);

int main(void)
{
    // Demander à l'utilisateur le montant de la monnaie due, en centimes
    int cents;
    do
    {
        cents = get_int("Monnaie due : ");
    }
    while (cents < 0);

    // Calculer le nombre de quarts à donner au client
    int quarters = calculate_quarters(cents);

    // Soustraire la valeur de ces quarts des centimes
    cents = cents - (quarters * 25);
}

int calculate_quarters(int cents)
{
    // Calculer le nombre de quarts à donner au client
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}
```

Quelques problèmes résolus, et quelques autres à venir ! Vous remarquez un modèle que vous pourriez réutiliser ici ?

## Comment tester

Pour ce programme, essayez de tester votre code manuellement. C'est une bonne pratique :

- Si vous saisissez `-1`, votre programme vous le demande-t-il à nouveau ?
- Si vous saisissez `0`, votre programme affiche-t-il `0` ?
- Si vous saisissez `1`, votre programme affiche-t-il `1` (c'est-à-dire un sou )?
- Si vous saisissez `4`, votre programme affiche-t-il `4` (c'est-à-dire quatre sous )?
- Si vous saisissez `5`, votre programme affiche-t-il `1` (c'est-à-dire un nickel )?
- Si vous saisissez `24`, votre programme affiche-t-il `6` (c'est-à-dire deux pièces de dix cents et quatre sous )?
- Si vous saisissez `25`, votre programme affiche-t-il `1` (c'est-à-dire un quart )?
- Si vous saisissez `26`, votre programme affiche-t-il `2` (c'est-à-dire un quart et un sou )?
- Si vous saisissez `99`, votre programme affiche-t-il `9` (c'est-à-dire trois quarts, deux pièces de dix cents et quatre sous )?

### Justesse

Dans votre terminal, exécutez ce qui suit pour vérifier l'exactitude de votre travail :

```bash
check50 cs50/problems/2024/x/cash
```

### Style

Exécutez ce qui suit pour évaluer le style de votre code à l'aide de `style50` :

```bash
style50 cash.c
```

## Comment soumettre

Dans votre terminal, exécutez ce qui suit pour soumettre votre travail :

```bash
submit50 cs50/problems/2024/x/cash
```

