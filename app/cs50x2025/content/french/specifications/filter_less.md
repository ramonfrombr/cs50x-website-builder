## Filtre

![Harvard Yard en niveaux de gris](https://cs50.harvard.edu/x/2024/psets/4/filter/less/yard-grayscale.bmp)

## Problème à résoudre

Le moyen peut-être le plus simple de représenter une image consiste à utiliser une grille de pixels (c'est-à-dire de points), chacun pouvant être d'une couleur différente. Pour les images en noir et blanc, nous avons donc besoin d'un bit par pixel, car 0 peut représenter le noir et 1 peut représenter le blanc, comme ci-dessous.

![un bitmap simple](https://cs50.harvard.edu/x/2024/psets/4/filter/less/bitmap.png)

En ce sens, une image n'est donc qu'un bitmap (c'est-à-dire une carte de bits). Pour les images plus colorées, il vous suffit de plus de bits par pixel. Un format de fichier (comme [BMP](https://en.wikipedia.org/wiki/BMP_file_format), [JPEG](https://en.wikipedia.org/wiki/JPEG), ou [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)) qui prend en charge la « couleur 24 bits » utilise 24 bits par pixel. (BMP prend en fait en charge les couleurs 1, 4, 8, 16, 24 et 32 bits.)

Un BMP 24 bits utilise 8 bits pour indiquer la quantité de rouge dans la couleur d'un pixel, 8 bits pour indiquer la quantité de vert dans la couleur d'un pixel et 8 bits pour indiquer la quantité de bleu dans la couleur d'un pixel. Si vous avez déjà entendu parler de la couleur RVB, eh bien, voilà : rouge, vert, bleu.

Si les valeurs R, V et B d'un pixel dans un BMP sont, par exemple, `0xff`, `0x00` et `0x00` en hexadécimal, ce pixel est purement rouge, car `0xff` (autrement dit `255` en décimal) implique « beaucoup de rouge », tandis que `0x00` et `0x00` impliquent « pas de vert » et « pas de bleu », respectivement. Dans ce problème, vous manipulerez ces valeurs R, V et B de pixels individuels, créant finalement vos propres filtres d'image.

Dans un fichier appelé `helpers.c` dans un dossier appelé `filter-less`, écrivez un programme pour appliquer des filtres aux BMP.

## Démonstration

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-QnLel70SPmbW9nswXTb9Yu9ZD" src="https://asciinema.org/a/QnLel70SPmbW9nswXTb9Yu9ZD.js"></script>

## Code de distribution

Pour ce problème, vous étendrez les fonctionnalités du code qui vous a été fourni par l'équipe de CS50.

Connectez-vous à [cs50.dev](https://cs50.dev/), cliquez sur votre fenêtre de terminal et exécutez `cd` seul. Vous devriez constater que l'invite de votre fenêtre de terminal ressemble à ce qui suit :

    $

Ensuite, exécutez

    wget https://cdn.cs50.net/2023/fall/psets/4/filter-less.zip

afin de télécharger un ZIP appelé `filter-less.zip` dans votre espace de code.

Ensuite, exécutez

    unzip filter-less.zip

afin de créer un dossier appelé `filter-less`. Vous n'avez plus besoin du fichier ZIP, vous pouvez exécuter

    rm filter-less.zip

et répondre par « y » suivi d'Entrée à l'invite de suppression du fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd filter-less

suivi d'Entrée pour vous déplacer (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit.

    filter-less/ $

Exécutez `ls` seul, et vous devriez voir quelques fichiers : `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` et `Makefile`. Vous devriez également voir un dossier, `images/`, avec quatre fichiers BMP. Si vous rencontrez un problème, suivez à nouveau ces étapes et essayez de déterminer où vous vous êtes trompé !

## Contexte

### Technique (carte bits)

Rappelons qu'un fichier est simplement une séquence de bits, agencés d'une certaine façon. Un fichier BMP 24 bits est donc essentiellement une séquence de bits, dont (presque) tous les 24 représentent la couleur d'un pixel. Cependant, un fichier BMP contient également des « métadonnées », des informations comme la hauteur et la largeur d'une image. Ces métadonnées sont stockées au début du fichier, sous la forme de deux structures de données généralement appelées « en-têtes », à ne pas confondre avec les fichiers d'en-tête de C. (D'ailleurs, ces en-têtes ont évolué au fil du temps. Ce problème utilise la dernière version du format BMP de Microsoft, la 4.0, qui a fait ses débuts avec Windows 95.)

Le premier de ces en-têtes, appelé `BITMAPFILEHEADER`, fait 14 octets de long. (Rappelons que 1 octet est égal à 8 bits.) Le second en-tête, appelé `BITMAPINFOHEADER`, fait 40 octets de long. Immédiatement après ces en-têtes se trouve la carte bits réelle : une chaîne d'octets, dont les triplets représentent la couleur d'un pixel. Cependant, BMP stocke ces triplets à l'envers (c.-à-d. en tant que BGR), avec 8 bits pour le bleu, suivis de 8 bits pour le vert, suivis de 8 bits pour le rouge. (Certains BMP stockent également la carte bits entière à l'envers, avec la ligne supérieure d'une image à la fin du fichier BMP. Cependant, nous avons stocké les fichiers BMP de cet ensemble de problèmes tels que décrits ici, avec la première ligne de chaque carte bits en premier et la dernière ligne en dernier.) En d'autres termes, si nous devions convertir le smiley 1 bit ci-dessus en un smiley 24 bits, en remplaçant le noir par du rouge, un BMP 24 bits stockerait cette carte bits comme suit, avec `0000ff` signifiant rouge et `ffffff` signifiant blanc ; nous avons mis en évidence au crayon rouge toutes les instances de `0000ff`.

![red smile](https://cs50.harvard.edu/x/2024/psets/4/filter/less/red_smile.png)

Comme nous avons présenté ces bits de gauche à droite, de haut en bas, en 8 colonnes, vous pouvez réellement voir la petite tête rouge si vous reculez.

Pour plus de clarté, rappelons qu'un chiffre hexadécimal représente 4 bits. Par conséquent, `ffffff` en hexadécimal signifie en réalité `111111111111111111111111` en binaire.

Notez que vous pouvez représenter une carte bits comme un tableau de pixels à deux dimensions : l'image est un tableau de lignes, chaque ligne étant un tableau de pixels. En effet, c'est ainsi que nous avons choisi de représenter les images bitmap dans ce problème.

### Filtre d'image

Que signifie même filtrer une image ? Filtrer une image consiste à prendre les pixels de l'image originale et à modifier chaque pixel de manière à ce qu'un effet particulier soit apparent sur l'image résultante.

## Compréhension

Examinons maintenant certains des fichiers qui vous ont été fournis comme code de distribution pour comprendre ce qu'ils contiennent.

### `bmp.h`

Ouvrez `bmp.h` (en double-cliquant dessus dans le navigateur de fichiers) et jetez un coup d'œil.

Vous verrez des définitions pour les en-têtes que nous avons mentionnés (`BITMAPINFOHEADER` et `BITMAPFILEHEADER`). De plus, ce fichier définit `BYTE`, `DWORD`, `LONG` et `WORD`, des types de données que l'on trouve normalement dans le monde de la programmation Windows. Remarquez qu'il s'agit simplement d'alias pour des primitives que vous connaissez (espérons-le) déjà. Il semble que `BITMAPFILEHEADER` et `BITMAPINFOHEADER` utilisent ces types.

Le plus important pour vous, peut-être, est que ce fichier définit également une structure appelée `RGBTRIPLE` qui, tout simplement, « encapsule » trois octets : un bleu, un vert et un rouge (l'ordre, rappelez-vous, dans lequel nous nous attendons à trouver les triplets RVB sur le disque).

Pourquoi ces structures sont-elles utiles ? Eh bien, rappelons qu'un fichier est simplement une séquence d'octets (ou, au final, de bits) sur le disque. Cependant, ces octets sont généralement ordonnés de telle manière que les premiers représentent quelque chose, les suivants représentent autre chose, et ainsi de suite. Les « formats de fichiers » existent parce que le monde a standardisé ce que les octets signifient. Maintenant, nous pourrions simplement lire un fichier sur un disque en RAM comme un grand tableau d'octets. Et nous pourrions simplement nous rappeler que l'octet `array[i]` représente une chose, tandis que l'octet `array[j]` en représente une autre. Mais pourquoi ne pas donner des noms à certains de ces octets afin de pouvoir les récupérer de la mémoire plus facilement ? C'est précisément ce que nous permettent de faire les structures de `bmp.h`. Au lieu de penser à certains fichiers comme une longue séquence d'octets, nous pouvons plutôt les considérer comme une séquence de structures.

### `filter.c`

Maintenant, ouvrons `filter.c`. Ce fichier a déjà été écrit pour vous, mais voici quelques points importants à noter.

Tout d'abord, remarquez la définition de `filters` à la ligne 10. Cette chaîne indique au programme quels sont les arguments de ligne de commande autorisés pour le programme : `b`, `g`, `r` et `s`. Chacun d'eux spécifient un filtre différent que nous pourrions appliquer à nos images : flou, échelle de gris, effet miroir et sépia.

Les lignes suivantes ouvrent un fichier image, s'assurent qu'il s'agit bien d'un fichier BMP et lisent toutes les informations sur les pixels dans un tableau 2D appelé `image`.

Faites défiler jusqu'à l'instruction `switch` qui commence à la ligne 101. Notez que, selon le filtre `filter` que nous avons choisi, une fonction différente est appelée : si l'utilisateur choisit le filtre `b`, le programme appelle la fonction `blur` ; si `g`, alors `grayscale` est appelé ; si `r`, alors `reflect` est appelé ; et si `s`, alors `sepia` est appelé. Notez également que chacune de ces fonctions prend en arguments la hauteur de l'image, la largeur de l'image et le tableau 2D des pixels.

Ce sont les fonctions que vous implémenterez (bientôt !). Comme vous pouvez l'imaginer, le but est que chacune de ces fonctions modifie le tableau 2D des pixels de manière à ce que le filtre souhaité soit appliqué à l'image.

Les lignes restantes du programme prennent l'image `image` résultante et l'écrivent dans un nouveau fichier image.

### `helpers.h`

Ensuite, jetez un œil à `helpers.h`. Ce fichier est assez court et ne fournit que les prototypes de fonction pour les fonctions que vous avez vues précédemment.

Notez ici que chaque fonction prend un tableau 2D appelé `image` comme argument, où `image` est un tableau de `height` lignes, et que chaque ligne est elle-même un autre tableau de `width` `RGBTRIPLE`. Donc, si `image` représente l'image entière, alors `image[0]` représente la première ligne, et `image[0][0]` représente le pixel dans le coin supérieur gauche de l'image.

### `helpers.c`

Maintenant, ouvrez `helpers.c`. C'est ici que l'implémentation des fonctions déclarées dans `helpers.h` a sa place. Mais veuillez noter que, pour le moment, les implémentations sont manquantes ! Cette partie vous revient.

### `Makefile`

Enfin, examinons `Makefile`. Ce fichier spécifie ce qui doit se produire lorsque nous exécutons une commande de terminal comme `make filter`. Alors que les programmes que vous avez pu écrire auparavant étaient confinés à un seul fichier, `filter` semble utiliser plusieurs fichiers : `filter.c` et `helpers.c`. Nous devrons donc indiquer à `make` comment compiler ce fichier.

Essayez de compiler `filter` vous-même en accédant à votre terminal et en exécutant :

    $ make filter

Ensuite, vous pouvez exécuter le programme en exécutant :

    $ ./filter -g images/yard.bmp out.bmp

Ce qui prend l'image `images/yard.bmp` et génère une nouvelle image appelée `out.bmp` après avoir passé les pixels par la fonction `grayscale`. Cependant, `grayscale` ne fait rien pour l'instant, donc l'image de sortie doit ressembler à la cour d'origine.

## Spécification

Implémentez les fonctions dans `helpers.c` de sorte qu'un utilisateur puisse appliquer des filtres en niveaux de gris, sépia, réflexion ou flou à leurs images.

- La fonction `grayscale` doit prendre une image et la transformer en une version en noir et blanc de la même image.
- La fonction `sepia` doit prendre une image et la transformer en une version sépia de la même image.
- La fonction `reflect` doit prendre une image et la refléter horizontalement.
- Enfin, la fonction `blur` doit prendre une image et la transformer en une version floue au carré de la même image.

Vous ne devez modifier aucune des signatures de fonction, ni aucun autre fichier que `helpers.c`.

## Astuces

### Implémentez `grayscale`

Un filtre courant est le filtre « en niveaux de gris », où nous prenons une image et voulons la convertir en noir et blanc. Comment cela fonctionne-t-il ?

- Rappelez-vous que si les valeurs rouge, verte et bleue sont toutes définies sur `0x00` (hexadécimal pour `0`), le pixel est noir. Et si toutes les valeurs sont définies sur `0xff` (hexadécimal pour `255`), le pixel est blanc. Tant que les valeurs rouge, verte et bleue sont toutes égales, le résultat sera des nuances de gris variables sur le spectre noir-blanc, les valeurs plus élevées signifiant des teintes plus claires (plus proches du blanc) et les valeurs plus faibles signifiant des teintes plus foncées (plus proches du noir).
- Donc, pour convertir un pixel en niveaux de gris, il suffit de s'assurer que les valeurs rouge, verte et bleue sont toutes de la même valeur. Mais comment savoir quelle valeur leur donner ? Eh bien, il est probablement raisonnable de s'attendre à ce que si les valeurs rouge, verte et bleue d'origine étaient toutes assez élevées, la nouvelle valeur devrait également être assez élevée. Et si les valeurs d'origine étaient toutes faibles, la nouvelle valeur devrait également être faible.
- En fait, pour garantir que chaque pixel de la nouvelle image ait toujours la même luminosité ou obscurité générale que l'ancienne image, vous pouvez prendre la **moyenne** des valeurs rouge, verte et bleue pour déterminer la nuance de gris à appliquer au nouveau pixel.

Si vous appliquez l'algorithme ci-dessus à chaque pixel de l'image, le résultat sera une image convertie en niveaux de gris. Écrivez du pseudo-code pour vous aider à résoudre ce problème.

    void grayscale(int height, int width, RGBTRIPLE image[height][width])
    {
        // Boucler sur tous les pixels

            // Prendre la moyenne des valeurs rouge, verte et bleue

            // Mettre à jour les valeurs des pixels
    }

Tout d'abord, comment pouvez-vous faire une boucle sur tous les pixels ? Rappelez-vous que les pixels de l'image sont stockés dans le tableau à deux dimensions `image`. Pour itérer sur un tableau à deux dimensions, vous aurez besoin de deux boucles, l'une imbriquée dans l'autre.

    void grayscale(int height, int width, RGBTRIPLE image[height][width])
    {
        // Boucler sur tous les pixels
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                // Prendre la moyenne des valeurs rouge, verte et bleue

                // Mettre à jour les valeurs des pixels
            }
        }
    }

Maintenant, vous pouvez utiliser `image[i][j]` pour accéder à n'importe quel pixel individuel de l'image. Mais comment prendre la moyenne des éléments rouge, vert et bleu ? Rappelez-vous que chaque élément de `image` est un `RGBTRIPLE`, qui est la `struct` définie dans `bmp.h` pour représenter un pixel. La syntaxe habituelle pour accéder aux membres d'une `struct` s'applique, dans laquelle `image[i][j].rgbtRed` vous donnera accès à la valeur rouge de `RGBTRIPLE`, `image[i][j].rgbtGreen` vous donnera accès à sa valeur verte, et ainsi de suite.

Lorsque vous calculez la moyenne, gardez à l'esprit que les valeurs des composants `rgbtRed`, `rgbtGreen` et `rgbtBlue` d'un pixel sont tous des entiers. Assurez-vous donc d'[arrondir](https://manual.cs50.io/3/round) tous les nombres à virgule flottante à l'entier le plus proche lorsque vous les affectez à une valeur de pixel ! Et pourquoi voudriez-vous diviser la somme de ces entiers par 3,0 et non par 3 ?

Une fois que vous avez fait la moyenne des valeurs rouge, verte et bleue du pixel en une couleur en niveaux de gris résultante, mettez à jour les valeurs rouge, verte et bleue du pixel. À présent, vous connaissez déjà la syntaxe de l'affectation !

### Implémenter `sépia`

La plupart des logiciels de retouche d'images prennent en charge un filtre « sépia », qui donne aux images un aspect ancien en rendant l'ensemble de l'image légèrement brun rougeâtre.

- On peut convertir une image en sépia en prenant chaque pixel et en calculant de nouvelles valeurs rouge, verte et bleue en fonction des valeurs d'origine des trois.
- Il existe un certain nombre d'algorithmes pour convertir une image en sépia, mais pour ce problème, nous vous demandons d'utiliser l'algorithme suivant. Pour chaque pixel, les valeurs de couleur sépia doivent être calculées en fonction des valeurs de couleur d'origine comme indiqué ci-dessous.
  sepiaRouge = 0,393 _ rougeOriginal + 0,769 _ vertOriginal + 0,189 _ bleuOriginal
  sepiaVert = 0,349 _ rougeOriginal + 0,686 _ vertOriginal + 0,168 _ bleuOriginal
  sepiaBleu = 0,272 _ rougeOriginal + 0,534 _ vertOriginal + 0,131 _ bleuOriginal

- Bien sûr, le résultat de chacune de ces formules peut ne pas être un entier, mais chaque valeur peut être arrondie à l'entier le plus proche. Il est également possible que le résultat de la formule soit un nombre supérieur à 255, la valeur maximale pour une valeur de couleur 8 bits. Dans ce cas, les valeurs rouge, verte et bleue doivent être plafonnées à 255. Par conséquent, nous pouvons garantir que les valeurs rouge, verte et bleue résultantes seront des nombres entiers compris entre 0 et 255, inclus.

Écrivez un pseudoc code pour vous aider à résoudre ce problème et à vous souvenir de l'utilisation de boucles `for` imbriquées pour visiter chaque pixel.

    void sépia(int hauteur, int largeur, RGBTRIPLE image[hauteur][largeur])
    {
        // Boucler sur tous les pixels
        for (int i = 0 ; i < hauteur ; i++)
        {
            for (int j = 0 ; j < largeur ; j++)
            {
                // Calculer les valeurs sépia

                // Mettre à jour le pixel avec des valeurs sépia
            }
        }
    }

Pour calculer les valeurs `sépia`, relisez les puces ci-dessus. Vous avez une formule pour calculer les valeurs sépia, mais il y a encore quelques pièges. En particulier, vous devrez :

- Arrondir le résultat de chaque calcul à l'entier le plus proche
- S'assurer que la valeur résultante n'est pas supérieure à 255

Comment une fonction qui renvoie le plus petit de deux entiers peut-elle être utile lors de l'implémentation de `sépia`, en particulier lorsque vous devez vous assurer que la valeur d'une couleur n'est pas supérieure à 255 ? Vous pouvez, mais ce n'est pas obligatoire, écrire votre propre fonction d'assistance pour faire exactement cela !

### Implémenter `refléter`

Certains filtres peuvent également déplacer les pixels. La réflexion d'une image, par exemple, est un filtre où l'image résultante est ce que vous obtiendriez en plaçant l'image originale devant un miroir.

- Tous les pixels sur le côté gauche de l'image doivent se retrouver à droite, et vice versa.
- Notez que tous les pixels originaux de l'image originale seront toujours présents dans l'image réfléchie, c'est juste que ces pixels ont peut-être été réarrangés pour être à un endroit différent dans l'image.

Dans la fonction `refléter`, vous devrez donc permuter les valeurs des pixels sur les côtés opposés d'une ligne. Écrivez un pseudoc code pour vous aider à démarrer :

    void refléter(int hauteur, int largeur, RGBTRIPLE image[hauteur][largeur])
    {
        // Boucler sur tous les pixels
        for (int i = 0 ; i < hauteur ; i++)
        {
            for (int j = 0 ; j < largeur ; j++)
            {
                // Permuter les pixels
            }
        }
    }

Rappelez-vous du cours comment nous avons implémenté l'échange de deux valeurs avec une variable temporaire. Pas besoin d'utiliser une fonction séparée pour l'échange, sauf si vous le souhaitez !

Et c'est le bon moment pour penser à vos boucles `for` imbriquées. La boucle `for` externe itère sur chaque ligne, tandis que la boucle `for` interne itère sur chaque pixel de cette ligne. Cependant, pour réussir à refléter une ligne, avez-vous besoin d'itérer sur chaque pixel ?

### Implémenter `flou`

Il existe plusieurs façons de créer l'effet d'un flou ou d'un adoucissement d'une image. Pour ce problème, nous utiliserons le "flou de boîte", qui consiste à prendre chaque pixel et, pour chaque valeur de couleur, à lui donner une nouvelle valeur en faisant la moyenne des valeurs de couleur des pixels voisins.

- Considérez la grille de pixels suivante, où nous avons numéroté chaque pixel.
  ![une grille de pixels](grid.png)
- La nouvelle valeur de chaque pixel serait la moyenne des valeurs de tous les pixels qui sont à 1 rangée et à 1 colonne du pixel d'origine (formant une boîte 3x3). Par exemple, chacune des valeurs de couleur du pixel 6 serait obtenue en faisant la moyenne des valeurs de couleur d'origine des pixels 1, 2, 3, 5, 6, 7, 9, 10 et 11 (notez que le pixel 6 lui-même est inclus dans la moyenne). De même, les valeurs de couleur du pixel 11 seraient obtenues en faisant la moyenne des valeurs de couleur des pixels 6, 7, 8, 10, 11, 12, 14, 15 et 16.
- Pour un pixel situé sur le bord ou le coin, comme le pixel 15, nous rechercherions toujours tous les pixels à 1 rangée et à 1 colonne : dans ce cas, les pixels 10, 11, 12, 14, 15 et 16.

Lors de l'implémentation de la fonction `flou`, vous constaterez peut-être que le fait de flouter un pixel finit par affecter le flou d'un autre pixel. Il serait préférable de créer une copie de `image` en déclarant un nouveau tableau à deux dimensions avec du code tel que `RGBTRIPLE copy[height][width];`. Puis copiez `image` dans `copy`, pixel par pixel, avec des boucles `for` imbriquées, comme ceci :

    void blur(int height, int width, RGBTRIPLE image[height][width])
    {
        // Créer une copie de image
        RGBTRIPLE copy[height][width];
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                copy[i][j] = image[i][j];
            }
        }
    }

Maintenant, vous pouvez lire les couleurs des pixels à partir de `copy` mais écrire (c'est-à-dire modifier) les couleurs des pixels dans `image` !

## Procédure pas à pas

**Veuillez noter qu'il y a 5 vidéos dans cette liste de lecture.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/K0v9byp9jd0?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T3837jmUt0ep7Tpmnxdv9NVut"></iframe></div>

## Comment tester

Assurez-vous de tester tous vos filtres sur les fichiers bitmap d'exemple fournis !

### Justesse

    check50 cs50/problems/2024/x/filter/less

### Style

    style50 helpers.c

## Comment soumettre

    submit50 cs50/problems/2024/x/filter/less

