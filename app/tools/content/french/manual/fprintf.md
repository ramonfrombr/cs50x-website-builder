# [NOM](#name)

fprintf - imprime dans un fichier

# [SYNOPSIS](#synopsis)

## Fichier d'en-tête

    #include <stdio.h>

## Prototype

    int fprintf(FILE *stream, const char *format, ...);

Notez que `...` représente zéro ou plusieurs arguments supplémentaires.

# [DESCRIPTION](#description)

Cette fonction imprime une "chaîne formatée" dans un fichier. Elle attend en entrée le pointeur d'un `FILE` renvoyé par [fopen](fopen), une "chaîne de format" qui spécifie ce qu'il faut imprimer, et zéro ou plusieurs arguments ultérieurs. La chaîne de format peut éventuellement contenir des "spécifications de conversion", des espaces réservés qui commencent par `%` et qui spécifient comment formater les arguments ultérieurs de la fonction, s'il y en a. Par exemple, si `file` est un pointeur vers un `FILE` et `c` est un `char`, cette fonction peut imprimer ce dernier dans le premier comme suit en utilisant `%c`:

    fprintf(file, "%c\n", c);

Alternativement, cette fonction pourrait également formater cette même valeur en tant qu'`int` en utilisant `%i`, comme dans un tableau ASCII:

    fprintf(file, "%c %i\n", c, c);

Et cette fonction peut également imprimer des chaînes sans spécifications de conversion:

    fprintf(file, "bonjour tout le monde\n");

Parmi les spécifications de conversion prises en charge par cette fonction, on trouve:

| Spécification de conversion | Type     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |
| `%s`                     | `char *` |

Pour imprimer le signe de pourcentage réel, utilisez `%%`.

Pour spécifier la "précision" d'un `float` ou d'un `double`, `%f` peut éventuellement contenir un `.` après le `%`, suivi d'un nombre de décimales. Par exemple, cette fonction pourrait formater la valeur d'un tiers avec une décimale en utilisant `%.1f`:

    fprintf(file, "%.1f\n", 1.0 / 3.0);

# [VALEUR DE RETOUR](#return-value)

Cette fonction renvoie le nombre de caractères imprimés.

# [EXEMPLES](#examples)

    #include <stdio.h>

    int main(void)
    {
        FILE *file = fopen("cs50.txt", "w");
        if (file == NULL)
        {
            return 0;
        }

        char *s = "Ceci est CS50";
        fprintf(file, "%s\n", s);

        int i = 50;
        fprintf(file, "Ceci est CS%i\n", i);

        float f = 50.0;
        fprintf(file, "Ceci est CS%.0f\n", f);

        fclose(file);
        return 0;
    }