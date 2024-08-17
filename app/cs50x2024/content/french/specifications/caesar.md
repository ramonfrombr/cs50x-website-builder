# César

![Chiffrement de César](https://cs50.harvard.edu/x/2024/psets/2/caesar/cipher.jpg)

## Problème à résoudre

On suppose que César (oui, celui-là même) utilisait pour "crypter" (c'est-à-dire dissimuler de manière réversible) des messages confidentiels, en décalant chaque lettre d'un certain nombre de positions. Par exemple, il pouvait écrire A à la place de B, B à la place de C, C à la place de D, ..., et en faisant le tour de l'alphabet, Z à la place de A. C'est ainsi que pour dire BONJOUR à quelqu'un, César pouvait écrire CPOPGJ. À la réception de tels messages, les destinataires devaient les "décrypter" en décalant les lettres en sens inverse du même nombre de positions.

Le secret de ce "cryptosystème" reposait sur le fait que seuls César et les destinataires connaissaient un secret, le nombre de places dont César avait décalé ses lettres (par exemple, 1). Ce n'est pas particulièrement sûr selon les normes modernes, mais bon, si vous êtes peut-être le premier au monde à le faire, c'est assez sûr !

Un texte non crypté est généralement appelé _texte clair_. Un texte crypté est généralement appelé _texte chiffré_. Et le secret utilisé s'appelle une _clé_.

Pour être clair, voici comment le cryptage de "BONJOUR" avec une clé de \(1\) donne "CPOPGJ" :

| Texte clair    | `B`     | `O`     | `N`     | `J`     | `O`     | `U`     | `R`     |
| ------------ | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| \+ Clé       | \(1\\) | \(1\\) | \(1\\) | \(1\\) | \(1\\) | \(1\\) | \(1\\) |
| = Texte chiffré | `C`     | `P`     | `O`     | `P`     | `G`     | `J`     | `S`     |

Plus formellement, l'algorithme de César (c'est-à-dire le chiffrement) crypte les messages en "faisant pivoter" chaque lettre de \(k\) positions. Plus formellement, si \(p\) est un texte clair (c'est-à-dire un message non crypté), \(p_i\) est le \(i^{ième}\) caractère de \(p\), et \(k\) est une clé secrète (c'est-à-dire un entier non négatif), alors chaque lettre, \(c_i\), du texte chiffré, \(c\), est calculée comme suit :

\\\[c_i = (p_i + k)\\space\\%\\space26\\\]

où \\(\\%\\space26\\) signifie ici "reste de la division par 26". Cette formule donne peut-être l'impression que le chiffrement est plus compliqué qu'il ne l'est, mais ce n'est en fait qu'une manière concise d'exprimer l'algorithme avec précision. En effet, pour faciliter la discussion, pensez à A (ou a) comme \(0\), B (ou b) comme \(1\), …, H (ou h) comme \(7\), I (ou i) comme \(8\), …, et Z (ou z) comme \(25\). Supposons que César veuille dire "Salut" à quelqu'un en toute confidentialité en utilisant, cette fois, une clé, \(k\), de 3. Son texte clair, \(p\), est donc "Salut", dans lequel le premier caractère de son texte clair, \(p_0\), est "S" (c'est-à-dire 18), et le deuxième caractère de son texte clair, \(p_1\), est "a" (c'est-à-dire 0). Le premier caractère de son texte chiffré, \(c_0\), est donc "V", et le deuxième caractère de son texte chiffré, \(c_1\), est donc "d". C'est logique ?

Dans un fichier appelé `caesar.c` dans un dossier appelé `caesar`, écrivez un programme qui vous permet de crypter des messages en utilisant le chiffrement de César. Au moment où l'utilisateur exécute le programme, il doit décider, en fournissant un argument en ligne de commande, quelle doit être la clé du message secret qu'il fournira au moment de l'exécution. Nous ne devons pas nécessairement supposer que la clé de l'utilisateur va être un nombre ; bien que vous puissiez supposer que, si c'est un nombre, ce sera un entier positif.

## Démonstration

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-JnlhDTjc264WfGSoNxc0hsjEY" src="https://asciinema.org/a/JnlhDTjc264WfGSoNxc0hsjEY.js"></script>

## Spécifications

Concevez et implémentez un programme, `caesar`, qui crypte les messages en utilisant le chiffrement de César.

- Implémentez votre programme dans un fichier appelé `caesar.c` dans un répertoire appelé `caesar`.
- Votre programme doit accepter un seul argument de ligne de commande, un entier non négatif. Appelons-le \(k\) pour simplifier.
- Si votre programme est exécuté sans aucun argument de ligne de commande ou avec plus d'un argument de ligne de commande, votre programme doit imprimer un message d'erreur de votre choix (avec `printf`) et retourner de `main` une valeur de `1` (qui tend à signifier une erreur) immédiatement.
- Si l'un des caractères de l'argument de ligne de commande n'est pas un chiffre décimal, votre programme doit imprimer le message `Usage : ./caesar clé` et retourner de `main` une valeur de `1`.
- Ne supposez pas que \(k\) sera inférieur ou égal à 26. Votre programme doit fonctionner pour toutes les valeurs entières non négatives de \(k\) inférieures à \(2^{31} - 26\). En d'autres termes, vous n'avez pas à vous inquiéter si votre programme finit par planter si l'utilisateur choisit une valeur de \(k\) trop grande ou presque trop grande pour être contenue dans un `int`. (Rappel : un `int` peut déborder.) Mais, même si \(k\) est supérieur à \(26\), les caractères alphabétiques dans l'entrée de votre programme doivent rester des caractères alphabétiques dans la sortie de votre programme. Par exemple, si \(k\) est \(27\), `A` ne doit pas devenir `\` même si `\` est à \(27\) positions de `A` en ASCII, selon [asciitable.com](https://www.asciitable.com/) ; `A` doit devenir `B`, car `B` est à \(27\) positions de `A`, à condition de faire le tour de `Z` à `A`.
- Votre programme doit sortir `texte clair :` (avec deux espaces mais sans retour à la ligne) et ensuite demander à l'utilisateur une `chaîne` de texte clair (en utilisant `get_string`).
- Votre programme doit sortir `texte chiffré :` (avec un espace mais sans retour à la ligne) suivi du texte chiffré correspondant au texte clair, chaque caractère alphabétique du texte clair étant "décalé" de _k_ positions ; les caractères non alphabétiques doivent être sortis inchangés.
- Votre programme doit préserver la casse : les lettres majuscules, bien que décalées, doivent rester des lettres majuscules ; les lettres minuscules, bien que décalées, doivent rester des lettres minuscules.
- Après avoir sorti le texte chiffré, vous devez imprimer un retour à la ligne. Votre programme doit ensuite quitter en retournant `0` depuis `main`.

## Conseils

Comment commencer ? Abordons ce problème étape par étape.

### Pseudo-code

Tout d'abord, essayez d'écrire une fonction `main` dans `caesar.c` qui implémente le programme en utilisant uniquement du pseudo-code, même si vous n'êtes pas (encore !) sûr de savoir comment l'écrire en code réel.

Il y a plusieurs façons de le faire, voici donc une seule façon !

    int main(int argc, string argv[])
    {
        // Assurez-vous que le programme a été exécuté avec un seul argument de ligne de commande

        // Assurez-vous que chaque caractère de argv[1] est un chiffre

        // Convertissez argv[1] d'une `string` en un `int`

        // Demandez à l'utilisateur le texte clair

        // Pour chaque caractère du texte clair :

            // Faites pivoter le caractère s'il s'agit d'une lettre
    }

Vous pouvez modifier votre propre pseudo-code après avoir vu le nôtre ici, mais ne le copiez/collez pas simplement dans

### Comptage des arguments de la ligne de commande

Quel que soit votre pseudo-code, commençons par n'écrire que le code C qui vérifie si le programme a été exécuté avec un seul argument de ligne de commande avant d'ajouter des fonctionnalités supplémentaires.

Plus précisément, modifiez `main` dans `caesar.c` de telle manière que, si l'utilisateur ne fournit aucun argument de ligne de commande, ou deux ou plus, la fonction imprime `"Utilisation : ./caesar clé\n"` puis renvoie `1`, ce qui ferme le programme. Si l'utilisateur fournit exactement un argument de ligne de commande, le programme ne doit rien imprimer et simplement renvoyer `0`. Le programme doit donc se comporter comme indiqué ci-dessous :

    $ ./caesar
    Utilisation : ./caesar clé


    $ ./caesar 1 2 3
    Utilisation : ./caesar clé


    $ ./caesar 1

#### Astuces

- Rappelez-vous que vous pouvez imprimer à l'aide de `printf`.
- Rappelez-vous qu'une fonction peut renvoyer une valeur avec `return`.
- Rappelez-vous que `argc` contient le nombre d'arguments de ligne de commande passés à un programme, plus le nom du programme.

### Vérification de la clé

Maintenant que votre programme (espérons-le !) accepte l'entrée comme prescrit, passons à une autre étape.

Ajoutez à `caesar.c`, sous `main`, une fonction appelée, par exemple, `only_digits` qui prend une `chaîne` comme argument et renvoie `true` si cette `chaîne` ne contient que des chiffres, de `0` à `9`, sinon elle renvoie `false`. Veillez à ajouter également le prototype de la fonction au-dessus de `main`.

#### Astuces

- Vous voudrez probablement un prototype comme :
  bool only_digits(string s);

  Et n'oubliez pas d'inclure `cs50.h` en haut de votre fichier, afin que le compilateur reconnaisse `string` (et `bool`).

- Rappelez-vous qu'une chaîne de caractères n'est qu'un tableau de `char`.
- Rappelez-vous que `strlen`, déclarée dans `string.h`, calcule la longueur d'une `chaîne`.
- Vous pouvez trouver `isdigit`, déclarée dans `ctype.h`, utile, selon [manual.cs50.io](https://manual.cs50.io/). Mais notez qu'elle ne vérifie qu'un seul `char` à la fois !

Modifiez ensuite `main` de telle sorte qu'elle appelle `only_digits` sur `argv[1]`. Si cette fonction renvoie `false`, alors `main` doit imprimer `"Utilisation : ./caesar clé\n"` et renvoyer `1`. Sinon, `main` doit simplement renvoyer `0`. Le programme doit donc se comporter comme indiqué ci-dessous :

    $ ./caesar 42


    $ ./caesar banane
    Utilisation : ./caesar clé

### Utilisation de la clé

Modifiez maintenant `main` de telle manière qu'elle convertisse `argv[1]` en un `int`. Vous pouvez trouver `atoi`, déclarée dans `stdlib.h`, utile, selon [manual.cs50.io](https://manual.cs50.io/). Utilisez ensuite `get_string` pour demander à l'utilisateur du texte brut avec `"texte en clair : "`.

Implémentez ensuite une fonction appelée, par exemple, `rotate`, qui prend un `char` en entrée ainsi qu'un `int`, et qui fait pivoter ce `char` d'autant de positions s'il s'agit d'une lettre (c'est-à-dire alphabétique), en bouclant de `Z` à `A` (et de `z` à `a`) si nécessaire. Si le `char` n'est pas une lettre, la fonction doit renvoyer le même `char` inchangé.

#### Astuces

- Vous voudrez probablement un prototype comme :
  char rotate(char c, int n);

  Un appel de fonction comme
  rotate('A', 1)

  ou même
  rotate('A', 27)

  devrait donc renvoyer `'B'`. Et un appel de fonction comme
  rotate('!', 13)

  devrait renvoyer `'!'`.

- Rappelez-vous que vous pouvez explicitement « convertir » un `char` en un `int` avec `(int)`, et un `int` en un `char` avec `(char)`. Vous pouvez également le faire implicitement en traitant simplement l'un comme l'autre.
- Vous voudrez probablement soustraire la valeur ASCII de `'A'` à toutes les lettres majuscules, afin de traiter `'A'` comme `0`, `'B'` comme `1`, etc., tout en effectuant l'arithmétique. Puis ajoutez-le à nouveau lorsque vous en avez terminé avec le même.
- Vous voudrez probablement soustraire la valeur ASCII de `'a'` à toutes les lettres minuscules, afin de traiter `'a'` comme `0`, `'b'` comme `1`, etc., tout en effectuant l'arithmétique. Puis ajoutez-le à nouveau lorsque vous en avez terminé avec le même.
- Vous pouvez trouver d'autres fonctions déclarées dans `ctype.h` utiles, selon [manual.cs50.io](https://manual.cs50.io/).
- Vous trouverez probablement `%` utile pour « boucler » arithmétiquement d'une valeur comme `25` à `0`.

Modifiez ensuite `main` de telle sorte qu'elle imprime `"texte chiffré : "` puis itère sur chaque `char` dans le texte brut de l'utilisateur, en appelant `rotate` sur chacun, et en imprimant la valeur renvoyée.

#### Astuces

- Rappelez-vous que `printf` peut imprimer un `char` en utilisant `%c`.
- Si vous ne voyez aucune sortie lorsque vous appelez `printf`, c'est probablement parce que vous imprimez des caractères en dehors de la plage ASCII valide de 0 à 127. Essayez d'imprimer temporairement les caractères sous forme de nombres (en utilisant `%i` au lieu de `%c`) pour voir quelles valeurs vous imprimez !

## Procédure pas à pas

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/V2uusmv2wxI?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Comment tester

### Exactitude

Dans votre terminal, exécutez la commande ci-dessous pour vérifier l'exactitude de votre travail.

    check50 cs50/problems/2024/x/caesar

#### Comment utiliser `debug50`

Vous souhaitez exécuter `debug50` ? Vous pouvez le faire comme suit, après avoir compilé votre code avec succès avec `make`,

    debug50 ./caesar KEY

où `KEY` est la clé que vous donnez comme argument de ligne de commande à votre programme. Notez que l'exécution

    debug50 ./caesar

fera (idéalement !) s'arrêter votre programme en demandant une clé à l'utilisateur.

### Style

Exécutez la commande ci-dessous pour évaluer le style de votre code à l'aide de `style50`.

    style50 caesar.c

## Comment soumettre

Dans votre terminal, exécutez la commande ci-dessous pour soumettre votre travail :

    submit50 cs50/problems/2024/x/caesar

