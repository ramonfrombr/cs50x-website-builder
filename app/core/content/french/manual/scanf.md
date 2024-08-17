# [NOM](#nom)

scanf - obtenir une entrée d'un utilisateur

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdio.h>

## Prototype

    int scanf(const char * format, ...);

Notez que `...` représente zéro ou plusieurs arguments supplémentaires.

# [DESCRIPTION](#description)

Cette fonction "scanne" l'entrée du clavier d'un utilisateur pour des valeurs de types spécifiés. Il attend en entrée une "chaîne de format" qui spécifie ce à quoi s'attendre et zéro ou plusieurs arguments ultérieurs, chacun devant être un emplacement en mémoire. La chaîne de format doit généralement contenir des "spécifications de conversion", des espaces réservés qui commencent par `%` et qui spécifient quels types de valeurs sont attendus. Les arguments ultérieurs se verront attribuer ces valeurs. Par exemple, si `n` est un `int`, cette fonction peut obtenir un `int` d'un utilisateur en utilisant `%i`:

    scanf("%i", &n);

Parmi les spécifications de conversion prises en charge par cette fonction, on trouve:

| Spécification de conversion | Type     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |

Il n'est pas sûr d'utiliser cette fonction pour obtenir une chaîne de caractères d'un utilisateur en utilisant `%s`, car l'entrée de l'utilisateur pourrait dépasser la capacité de l'argument qui serait attribué à cette valeur.

# [VALEUR DE RETOUR](#valeur-de-retour)

Cette fonction renvoie le nombre d'arguments auxquels des valeurs ont été attribuées ou `EOF`, une constante définie dans `stdio.h`, en cas d'erreur.

# [EXEMPLES](#exemples)

    #include <stdio.h>

    int main(void)
    {
        int i;
        printf("Entrée: ");
        scanf("%i", &i);
        printf("Sortie: %i\n", i);
    }