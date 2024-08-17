# Volume

![WAV file waveform](https://cs50.harvard.edu/x/2024/psets/4/volume/wav_file.png)

## Problème à résoudre

Les fichiers [WAV](https://docs.fileformat.com/audio/wav/) sont un format de fichier courant pour représenter l'audio. Les fichiers WAV stockent l'audio sous forme d'une séquence "d'échantillons" : des nombres qui représentent la valeur d'un signal audio à un moment donné. Les fichiers WAV commencent par un "en-tête" de 44 octets qui contient des informations sur le fichier lui-même, notamment la taille du fichier, le nombre d'échantillons par seconde et la taille de chaque échantillon. Après l'en-tête, le fichier WAV contient une séquence d'échantillons, chacun étant un seul entier de 2 octets (16 bits) représentant le signal audio à un moment donné.

Ajuster la valeur de chaque échantillon par un facteur donné a pour effet de modifier le volume de l'audio. Multiplier chaque valeur d'échantillon par 2,0, par exemple, aura pour effet de doubler le volume de l'audio d'origine. Multiplier chaque échantillon par 0,5, quant à lui, aura pour effet de réduire le volume de moitié.

Dans un fichier appelé `volume.c` dans un dossier appelé `volume`, écrivez un programme pour modifier le volume d'un fichier audio.

## Démo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-mc2hPhYDt1spoMjlqNMuqC4Uc" src="https://asciinema.org/a/mc2hPhYDt1spoMjlqNMuqC4Uc.js"></script>

## Code de distribution

Pour ce problème, vous étendrez les fonctionnalités du code fourni par l'équipe de CS50.

Connectez-vous à [cs50.dev](https://cs50.dev/), cliquez sur votre fenêtre de terminal et exécutez `cd` seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ce qui suit :

    $

Ensuite, exécutez

    wget https://cdn.cs50.net/2023/fall/psets/4/volume.zip

afin de télécharger un ZIP appelé `volume.zip` dans votre espace de code.

Puis exécutez

    unzip volume.zip

pour créer un dossier appelé `volume`. Vous n'avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm volume.zip

et répondre par « y », puis Entrée à l'invite de commande pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd volume

suivi de la touche Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

    volume/ $

Si tout s'est bien passé, vous devez exécuter

    ls

et voir un fichier nommé `volume.c`. L'exécution de `code volume.c` devrait ouvrir le fichier dans lequel vous taperez votre code pour cette série de problèmes. Sinon, revenez sur vos pas et essayez de déterminer où vous vous êtes trompé !

## Détails de l'implémentation

Terminez l'implémentation de `volume.c`, de sorte qu'il modifie le volume d'un fichier son par un facteur donné.

- Le programme doit accepter trois arguments en ligne de commande. Le premier est `input`, qui représente le nom du fichier audio original. Le deuxième est `output`, qui représente le nom du nouveau fichier audio qui doit être généré. Le troisième est `factor`, qui est le montant par lequel le volume du fichier audio d'origine doit être ajusté.
  - Par exemple, si `factor` est `2,0`, votre programme doit doubler le volume du fichier audio dans `input` et enregistrer le nouveau fichier audio généré dans `output`.
- Votre programme doit d'abord lire l'en-tête du fichier d'entrée et écrire l'en-tête dans le fichier de sortie.
- Votre programme doit ensuite lire le reste des données du fichier WAV, un échantillon de 16 bits (2 octets) à la fois. Votre programme doit multiplier chaque échantillon par le `factor` et écrire le nouvel échantillon dans le fichier de sortie.
  - Vous pouvez supposer que le fichier WAV utilisera des valeurs signées de 16 bits comme échantillons. En pratique, les fichiers WAV peuvent avoir un nombre variable de bits par échantillon, mais nous supposerons des échantillons de 16 bits pour ce problème.
- Votre programme, s'il utilise `malloc`, ne doit pas fuir de mémoire.

## Conseils

### Comprenez le code dans `volume.c`

Notez d'abord que `volume.c` est déjà configuré pour recevoir trois arguments en ligne de commande, `input`, `output` et `factor`.

- `main` prend à la fois un `int`, `argc`, et un tableau de `char *` (chaînes !), `argv`.
- Si `argc`, le nombre d'arguments en ligne de commande, y compris le programme lui-même, n'est pas égal à 4, le programme imprimera son utilisation appropriée et quittera avec le code de statut 1.

        int main(int argc, char \*argv[])
        {
            // Vérifier les arguments en ligne de commande
            if (argc != 4)
            {
                printf("Usage : ./volume input.wav output.wav factor\n");
                return 1;
            }

            // ...
        }

Ensuite, `volume.c` utilise [`fopen`](https://manual.cs50.io/3/fopen) pour ouvrir les deux fichiers fournis en arguments en ligne de commande.

- Il est recommandé de vérifier si le résultat de l'appel de `fopen` est `NULL`. Si c'est le cas, le fichier n'a pas été trouvé ou n'a pas pu être ouvert.

        // Ouvrir les fichiers et déterminer le facteur d'ajustement
        FILE *input = fopen(argv[1], "r");
        if (input == NULL)
        {
            printf("Impossible d'ouvrir le fichier.\n");
            return 1;
        }

        FILE *output = fopen(argv[2], "w");
        if (output == NULL)
        {
            printf("Impossible d'ouvrir le fichier.\n");
            return 1;
        }

Plus tard, ces fichiers sont fermés avec `fclose`. Chaque fois que vous appelez `fopen`, vous devez appeler `fclose` plus tard !

        // Fermer les fichiers
        fclose(input);
        fclose(output);

Cependant, avant de fermer les fichiers, notez que nous avons quelques TODO.

        // TODO : Copier l'en-tête du fichier d'entrée vers le fichier de sortie

        // TODO : Lire les échantillons du fichier d'entrée et écrire les données mises à jour dans le fichier de sortie

Il y a de fortes chances que vous ayez besoin de connaître le facteur par lequel ajuster le volume, d'où la raison pour laquelle `volume.c` convertit déjà le troisième argument en ligne de commande en `float` pour vous !

        float factor = atof(argv[3]);

### Copier l'en-tête WAV du fichier d'entrée vers le fichier de sortie

Votre première TODO est de copier l'en-tête du fichier WAV depuis `input` et de l'écrire dans `output`. Tout d'abord, vous devez en apprendre plus sur quelques types de données spéciaux.

Jusqu'ici, nous avons vu un certain nombre de types différents en C, dont `int`, `bool`, `char`, `double`, `float` et `long`. Cependant, à l'intérieur d'un fichier d'en-tête appelé `stdint.h`, figurent les déclarations d'un certain nombre d'autres types qui nous permettent de définir très précisément la taille (en bits) et le signe (positif ou négatif) d'un nombre entier. Deux types en particulier nous seront utiles lorsque nous travaillerons avec des fichiers WAV :

- `uint8_t` est un type qui stocke un nombre entier non signé de 8 bits (d'où `8` !) (c'est-à-dire non négatif) (d'où `uint` !). Nous pouvons traiter chaque octet de l'en-tête d'un fichier WAV comme une valeur `uint8_t`.
- `int16_t` est un type stockant un nombre entier de 16 bits signé (c'est-à-dire positif ou négatif). Nous pouvons traiter chaque échantillon audio d'un fichier WAV comme une valeur `int16_t`.

Vous souhaiterez probablement créer un tableau d'octets pour stocker les données de l'en-tête du fichier WAV que vous lirez depuis le fichier d'entrée. En utilisant le type `uint8_t` pour représenter un octet, vous pouvez créer un tableau de `n` octets pour votre en-tête avec une syntaxe comme :

    uint8_t header[n];

en remplaçant `n` par le nombre d'octets. Vous pouvez ensuite utiliser `header` comme argument pour [`fread`](https://manual.cs50.io/3/fread) ou [`fwrite`](https://manual.cs50.io/3/fwrite) pour lire depuis ou écrire dans l'en-tête.

Souvenez-vous que l'en-tête d'un fichier WAV fait toujours exactement 44 octets. Notez que `volume.c` définit déjà une variable pour vous, nommée `HEADER_SIZE`, qui est égale au nombre d'octets dans l'en-tête.

Ce qui suit est un assez gros indice, mais voici comment vous pourriez accomplir cette TODO !

    // Copier l'en-tête du fichier d'entrée vers le fichier de sortie
    uint8_t header[HEADER_SIZE];
    fread(header, HEADER_SIZE, 1, input);
    fwrite(header, HEADER_SIZE, 1, output);

### Écrire les données mises à jour dans le fichier de sortie

Votre TODO suivante est de lire les échantillons depuis `input`, mettre à jour ces échantillons et écrire les échantillons mis à jour dans `output`. Lors de la lecture de fichiers, il est courant de créer un « tampon » dans lequel stocker temporairement les données. Là, vous pouvez modifier les données et, une fois qu'elles sont prêtes, écrire les données du tampon dans un nouveau fichier.

Souvenez-vous que nous pouvons utiliser le type `int16_t` pour représenter un échantillon d'un fichier WAV. Pour stocker un échantillon audio, vous pouvez donc créer une variable tampon avec une syntaxe comme :

    // Créer un tampon pour un échantillon unique
    int16_t buffer;

Avec un tampon pour les échantillons en place, vous pouvez maintenant y lire des données, un échantillon à la fois. Essayez d'utiliser `fread` pour cette tâche ! Vous pouvez utiliser `&buffer`, l'adresse de `buffer`, comme argument pour `fread` ou `fwrite` afin de lire depuis ou écrire dans le tampon. (Souvenez-vous que l'opérateur `&` est utilisé pour obtenir l'adresse de la variable.)

    // Créer un tampon pour un échantillon unique
    int16_t buffer;

    // Lire un échantillon unique dans le tampon
    fread(&buffer, sizeof(int16_t), 1, input)

Maintenant, pour augmenter (ou diminuer) le volume d'un échantillon, il vous suffit de le multiplier par un certain facteur.

    // Créer un tampon pour un échantillon unique
    int16_t buffer;

    // Lire un échantillon unique dans le tampon
    fread(&buffer, sizeof(int16_t), 1, input)

    // Mettre à jour le volume de l'échantillon
    buffer *= factor;

Et enfin, vous pouvez écrire cet échantillon mis à jour dans `output` :

    // Créer un tampon pour un échantillon unique
    int16_t buffer;

    // Lire un échantillon unique depuis input dans le tampon
    fread(&buffer, sizeof(int16_t), 1, input)

    // Mettre à jour le volume de l'échantillon
    buffer *= factor;

    // Écrire l'échantillon mis à jour dans un nouveau fichier
    fwrite(&buffer, sizeof(int16_t), 1, output);

Il n'y a qu'un seul problème : vous devrez continuer à lire un échantillon dans votre tampon, mettre à jour son volume et écrire l'échantillon mis à jour dans le fichier de sortie tant qu'il reste des échantillons à lire.

- Heureusement, en fonction de sa documentation, `fread` renverra le nombre d'éléments de données correctement lus. Vous pourriez trouver utile de vérifier cela pour savoir quand vous avez atteint la fin du fichier !
- Gardez à l'esprit qu'il n'y a aucune raison pour laquelle vous ne puissiez pas appeler `fread` à l'intérieur d'une condition de boucle `while`. Par exemple, vous pourriez passer un appel à `fread` correspondant à ce qui suit :

        while (fread(...))
        {

        }

C'est presque une solution, mais regardez ce qui suit pour une manière efficace de résoudre ce problème :

    // Créer un tampon pour un échantillon unique
    int16_t buffer;

    // Lire un échantillon unique depuis input dans le tampon tant qu'il reste des échantillons à lire
    while (fread(&buffer, sizeof(int16_t), 1, input) != 0)
    {
        // Mettre à jour le volume de l'échantillon
        buffer *= factor;

        // Écrire l'échantillon mis à jour dans un nouveau fichier
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

Comme la version de C que vous utilisez traite les valeurs non nulles comme `true` et les valeurs nulles comme `false`, vous pouvez simplifier la syntaxe ci-dessus de la manière suivante :

    // Créer un tampon pour un échantillon unique
    int16_t buffer;

    // Lire un échantillon unique depuis input dans le tampon tant qu'il reste des échantillons à lire
    while (fread(&buffer, sizeof(int16_t), 1, input))
    {
        // Mettre à jour le volume de l'échantillon
        buffer *= factor;

        // Écrire l'échantillon mis à jour dans un nouveau fichier
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

## Description pas à pas

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/LiGhjz9ColQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

<details><summary>Vous ne savez pas comment résoudre ? </summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-rtZkTAK2gg?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

## Comment tester

Le programme doit se comporter selon les exemples suivants.

    $ ./volume input.wav output.wav 2.0

Lorsque vous écoutez `output.wav` (par exemple en faisant un Ctrl-clic sur `output.wav` dans l'explorateur de fichiers, en choisissant **Télécharger**, puis en ouvrant le fichier dans un lecteur audio sur votre ordinateur), il doit être deux fois plus fort que `input.wav` !

    $ ./volume input.wav output.wav 0.5

Lorsque vous écoutez `output.wav`, il doit être deux fois moins fort que `input.wav` !

### Exactitude

    check50 cs50/problems/2024/x/volume

### Style

    style50 volume.c

## Comment soumettre

    submit50 cs50/problems/2024/x/volume

