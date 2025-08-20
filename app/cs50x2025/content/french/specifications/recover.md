# Récupérer

![Image récupérée](https://cs50.harvard.edu/x/2024/psets/4/recover/recovered_image.png)

## Problème à résoudre

En prévision de ce problème, nous avons passé ces derniers jours à prendre des photos sur le campus, qui ont toutes été sauvegardées sur un appareil photo numérique au format JPEG sur une carte mémoire. Malheureusement, nous les avons toutes supprimées par erreur ! Heureusement, dans le monde de l'informatique, « supprimé » tend à ne pas vraiment signifier « supprimé », mais plutôt « oublié ». Même si l'appareil photo insiste sur le fait que la carte est maintenant vide, nous sommes presque sûrs que ce n'est pas tout à fait vrai. En effet, nous espérons (ou plutôt, nous attendons !) que vous puissiez écrire un programme qui récupère les photos pour nous !

Dans un fichier appelé `recover.c` dans un dossier appelé `recover`, écrivez un programme pour récupérer les JPEG d'une carte mémoire.

## Code de distribution

Pour ce problème, vous étendrez la fonctionnalité du code qui vous a été fourni par le personnel de CS50.

Connectez-vous à [cs50.dev](https://cs50.dev/), cliquez sur votre fenêtre de terminal et exécutez `cd` par lui-même. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ceci :

    $

Exécutez ensuite

    wget https://cdn.cs50.net/2023/fall/psets/4/recover.zip

afin de télécharger un fichier ZIP appelé `recover.zip` dans votre espace de codes.

Puis exécutez

    unzip recover.zip

pour créer un dossier appelé `recover`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm recover.zip

et répondre par « y » suivi de Entrée à l'invite pour supprimer le fichier ZIP que vous avez téléchargé.

Tapez maintenant

    cd recover

suivi de Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ceci :

    recover/ $

Exécutez `ls` par lui-même, et vous devriez voir deux fichiers : `recover.c` et `card.raw`.

## Contexte

Même si les JPEG sont plus complexes que les BMP, ils ont des « signatures », des motifs d'octets qui peuvent les distinguer des autres formats de fichiers. Plus précisément, les trois premiers octets des JPEG sont

    0xff 0xd8 0xff

du premier octet au troisième octet, de gauche à droite. Le quatrième octet, quant à lui, est soit `0xe0`, `0xe1`, `0xe2`, `0xe3`, `0xe4`, `0xe5`, `0xe6`, `0xe7`, `0xe8`, `0xe9`, `0xea`, `0xeb`, `0xec`, `0xed`, `0xee`, ou `0xef`. En d'autres termes, les quatre premiers bits du quatrième octet sont `1110`.

Il est probable que si vous trouvez ce motif de quatre octets sur un support connu pour stocker des photos (par exemple, ma carte mémoire), ils délimitent le début d'un JPEG. Pour être juste, vous pouvez rencontrer ces motifs sur certains disques purement par hasard, donc la récupération de données n'est pas une science exacte.

Heureusement, les appareils photo numériques ont tendance à stocker les photos de manière contiguë sur les cartes mémoire, de sorte que chaque photo est stockée immédiatement après la photo prise précédemment. En conséquence, le début d'un JPEG délimite généralement la fin d'un autre. Cependant, les appareils photo numériques initialisent souvent les cartes avec un système de fichiers FAT dont la « taille de bloc » est de 512 octets (B). Cela implique que ces appareils photo n'écrivent sur ces cartes qu'en unités de 512 B. Une photo de 1 Mo (c'est-à-dire 1 048 576 B) occupe donc 1 048 576 ÷ 512 = 2 048 « blocs » sur une carte mémoire. Mais il en est de même pour une photo qui est, disons, un octet plus petite (c'est-à-dire 1 048 575 B) ! L'espace gaspillé sur le disque est appelé « espace libre ». Les enquêteurs en criminalistique examinent souvent l'espace libre pour y trouver des restes de données suspectes.

Ces détails impliquent que vous, l'enquêteur, pouvez probablement écrire un programme qui parcourt une copie de ma carte mémoire, à la recherche des signatures des JPEG. Chaque fois que vous trouvez une signature, vous pouvez ouvrir un nouveau fichier en écriture et commencer à le remplir avec des octets provenant de ma carte mémoire, en ne fermant ce fichier qu'une fois que vous avez rencontré une autre signature. De plus, plutôt que de lire les octets de ma carte mémoire un par un, vous pouvez en lire 512 à la fois dans une mémoire tampon, pour des raisons d'efficacité. Grâce à FAT, vous pouvez avoir confiance que les signatures des JPEG seront « alignées sur les blocs ». Autrement dit, vous n'avez besoin de rechercher ces signatures que dans les quatre premiers octets d'un bloc.

Bien sûr, il faut se rendre compte que les JPEG peuvent s'étendre sur des blocs contigus. Sinon, aucun JPEG ne pourrait être plus grand que 512 B. Mais le dernier octet d'un JPEG peut ne pas tomber à la toute fin d'un bloc. Rappelez-vous la possibilité d'espace libre. Mais ne vous inquiétez pas. Comme cette carte mémoire était toute neuve lorsque j'ai commencé à prendre des photos, il y a de fortes chances qu'elle ait été « remise à zéro » (c'est-à-dire remplie de 0) par le fabricant, dans ce cas, tout espace libre sera rempli de 0. Ce n'est pas grave si ces 0 de fin se retrouvent dans les JPEG que vous récupérez ; ils devraient toujours être visibles.

Maintenant, je n'ai qu'une seule carte mémoire, mais vous êtes nombreux ! C'est pourquoi je suis allé de l'avant et j'ai créé une « image légale » de la carte, en stockant son contenu, octet par octet, dans un fichier appelé `card.raw`. Pour que vous ne perdiez pas de temps à parcourir des millions de 0 inutilement, je n'ai imagé que les premiers mégaoctets de la carte mémoire. Mais vous devriez finalement constater que l'image contient 50 JPEG.

## Spécification

Implémentez un programme appelé `recover` qui récupère les JPEG à partir d'une image légale.

- Implémentez votre programme dans un fichier appelé `recover.c` dans un répertoire appelé `recover`.
- Votre programme doit accepter exactement un argument de ligne de commande, le nom d'une image légale à partir de laquelle récupérer les JPEG.
- Si votre programme n'est pas exécuté avec exactement un argument de ligne de commande, il doit rappeler à l'utilisateur l'utilisation correcte, et `main` doit renvoyer `1`.
- Si l'image légale ne peut pas être ouverte en lecture, votre programme doit en informer l'utilisateur et `main` doit renvoyer `1`.
- Les fichiers que vous générez doivent chacun être nommés `###.jpg`, où `###` est un nombre décimal à trois chiffres, commençant par `000` pour la première image et en augmentant ainsi.
- Votre programme, s'il utilise `malloc`, ne doit pas fuir de mémoire.

## Astuces

### Écrivez un peu de pseudo-code avant d'écrire plus de code

Si vous ne savez pas comment résoudre le problème général, décomposez-le en problèmes plus petits que vous pouvez probablement résoudre en premier. Par exemple, ce problème n'est en réalité qu'une poignée de problèmes :

1. Accepter un seul argument de ligne de commande : le nom d'une carte mémoire
2. Ouvrir la carte mémoire
3. Tant qu'il reste des données à lire sur la carte mémoire

    1. Créer des JPEG à partir des données

Écrivons un peu de pseudo-code comme commentaires pour vous rappeler de faire exactement cela :

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Accepter un seul argument de ligne de commande

        // Ouvrir la carte mémoire

        // Tant qu'il reste des données à lire sur la carte mémoire

            // Créer des JPEG à partir des données
    }

### Convertir le pseudo-code en code

Tout d’abord, réfléchissez à la manière d’accepter un seul argument de ligne de commande. Si l’utilisateur utilise le programme de façon incorrecte, vous devez lui indiquer la bonne façon de l’utiliser.

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Accepter un seul argument de ligne de commande
        if (argc != 2)
        {
            printf("Usage: ./recover FILE\n");
            return 1;
        }

        // Ouvrir la carte mémoire

        // Tant qu’il y a des données à lire sur la carte mémoire

            // Créer des fichiers JPEG à partir des données
    }

Maintenant que vous avez vérifié que l’utilisation est correcte, vous pouvez ouvrir la carte mémoire. N’oubliez pas que vous pouvez ouvrir `card.raw` par programmation avec `fopen`, comme ci-dessous.

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Accepter un seul argument de ligne de commande
        if (argc != 2)
        {
            printf("Usage: ./recover FILE\n");
            return 1;
        }

        // Ouvrir la carte mémoire
        FILE *card = fopen(argv[1], "r");

        // Tant qu’il y a des données à lire sur la carte mémoire

            // Créer des fichiers JPEG à partir des données
    }

Vous devez bien sûr vérifier que le fichier a été ouvert correctement ! Si ce n’est pas le cas, informez-en l’utilisateur et quittez le programme : nous vous laissons cette partie.

Ensuite, votre programme doit lire les données de la carte que vous avez ouverte, jusqu’à ce qu’il n’y ait plus de données à lire. En cours de route, votre programme doit récupérer chacun des fichiers JPEG de `card.raw`, en stockant chacun d’eux sous forme de fichier distinct dans votre répertoire de travail actuel.

Réfléchissez d’abord à la manière de lire `card.raw` en profondeur. Rappelez-vous que, pour lire des données à partir d’un fichier, vous devez stocker temporairement ces données dans un « tampon ». Et rappelez-vous également que `card.raw` stocke les données dans des blocs de 512 octets. Par conséquent, vous voudrez probablement créer un tampon de 512 octets pour stocker des blocs de données au fur et à mesure que vous les lisez de manière séquentielle. Une façon de procéder est d’utiliser le type `uint8_t` de `stdint.h`, qui stocke exactement 8 bits (1 octet). Le type est appelé `uint8_t` puisqu’il stocke un entier non signé/positif/non négatif qui nécessite 8 bits d’espace (c’est-à-dire un octet).

    #include <stdint.h>
    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Accepter un seul argument de ligne de commande
        if (argc != 2)
        {
            printf("Usage: ./recover FILE\n");
            return 1;
        }

        // Ouvrir la carte mémoire
        FILE *card = fopen(argv[1], "r");

        // Créer un tampon pour un bloc de données
        uint8_t buffer[512];

        // Tant qu’il y a des données à lire sur la carte mémoire

            // Créer des fichiers JPEG à partir des données
    }

Cependant, ce n’est probablement pas la meilleure idée d’utiliser 512 comme un [« nombre magique »](../../../shorts/magic_numbers/) ici. Il y a des chances que vous puissiez encore améliorer cette conception !

Maintenant, réfléchissez à la manière de lire les données de la carte mémoire. Selon sa [page de manuel](https://man.cs50.io/3/fread), `fread` renvoie le nombre d’octets qu’il a lus, auquel cas il devrait renvoyer soit `512` soit `0`, étant donné que `card.raw` contient un certain nombre de blocs de 512 octets. Afin de lire chaque bloc de `card.raw`, après l’avoir ouvert avec `fopen`, il devrait suffire d’utiliser une boucle comme celle-ci.

    #include <stdint.h>
    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Accepter un seul argument de ligne de commande
        if (argc != 2)
        {
            printf("Usage: ./recover FILE\n");
            return 1;
        }

        // Ouvrir la carte mémoire
        FILE *card = fopen(argv[1], "r");

        // Créer un tampon pour un bloc de données
        uint8_t buffer[512];

        // Tant qu’il y a des données à lire sur la carte mémoire
        while (fread(buffer, 1, 512, card) == 512)
        {
            // Créer des fichiers JPEG à partir des données

        }
    }

De cette façon, dès que `fread` renvoie `0` (qui est en fait `false`), votre boucle se termine.

Enfin, c’est à vous de déterminer comment créer par programmation des fichiers JPEG au fur et à mesure que vous continuez à lire `card.raw`. Pour cela, vous trouverez peut-être utile la [procédure pas à pas](#procédure pas à pas) ci-dessous.

N’oubliez pas que votre programme doit numéroter les fichiers qu’il génère en les nommant chacun `###.jpg`, où `###` est un nombre décimal à trois chiffres à partir de `000`. Liez-vous d’amitié avec [`sprintf`](https://man.cs50.io/3/sprintf) et notez que `sprintf` stocke une chaîne formatée à un emplacement en mémoire. Étant donné le format `###.jpg` prescrit pour le nom de fichier d’un fichier JPEG, combien d’octets devez-vous allouer pour cette chaîne ? (N’oubliez pas le caractère NUL !)

Pour vérifier si les fichiers JPEG que votre programme renvoie sont corrects, double-cliquez simplement dessus et jetez un œil ! Si chaque photo apparaît intacte, votre opération a probablement réussi !

Et bien sûr, n’oubliez pas de `fclose` chaque fichier que vous avez ouvert avec `fopen` !

### Gardez votre répertoire de travail propre

Il y a de fortes chances que les fichiers JPEG que la première ébauche de votre code renvoie ne soient pas corrects. (Si vous les ouvrez et ne voyez rien, ils ne sont probablement pas corrects !) Exécutez la commande ci-dessous pour supprimer tous les fichiers JPEG dans votre répertoire de travail actuel.

    rm *.jpg

Si vous préférez ne pas être invité à confirmer chaque suppression, exécutez plutôt la commande ci-dessous.

    rm -f *.jpg

Soyez simplement prudent avec ce commutateur `-f`, car il « force » la suppression sans vous le demander.

## Procédure pas à pas

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ooL0r_8N9ms?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Comment tester

### Exécuter le programme

    ./recover card.raw

### Correctness

    check50 cs50/problems/2024/x/recover

### Style

    style50 recover.c

## Comment soumettre

    submit50 cs50/problems/2024/x/recover

