# Tri

## Problème à résoudre

Souviens-toi que nous avons vu quelques algorithmes pour trier une séquence de nombres lors de la conférence : le tri par sélection, le tri par bulle et le tri fusion.

- Le tri par sélection itère sur les parties non triées d'une liste, en sélectionnant l'élément le plus petit à chaque fois et en le déplaçant à l'emplacement approprié.
- Le tri par bulle compare des paires de valeurs adjacentes une par une et les échange si elles ne sont pas dans le bon ordre. Cela continue jusqu'à ce que la liste soit triée.
- Le tri fusion divise récursivement la liste en deux parties, puis fusionne les plus petites listes en une plus grande dans le bon ordre.

Dans ce problème, tu vas analyser trois programmes de tri (compilés !) pour déterminer quels algorithmes ils utilisent. Dans un fichier nommé `answers.txt` dans un dossier nommé `sort`, enregistre tes réponses, accompagnées d'une explication pour chaque programme, en renseignant les espaces marqués `TODO`.

## Code de distribution

Pour ce problème, tu auras besoin d'un « code de distribution » : c'est-à-dire un code écrit par l'équipe CS50. Trois programmes C déjà compilés, `sort1`, `sort2` et `sort3`, ainsi que plusieurs fichiers .txt pour l'entrée et un autre fichier, `answers.txt`, dans lequel écrire tes réponses, sont fournis. Chaque programme `sort1`, `sort2` et `sort3` implémente un algorithme de tri différent : le tri par sélection, le tri par bulle ou le tri fusion (mais pas nécessairement dans cet ordre !). Ta tâche est de déterminer quel algorithme de tri est utilisé par chaque fichier. Commence par télécharger ces fichiers.

### Télécharger les fichiers de distribution

Ouvre [VS Code](https://cs50.dev/).

Commence par cliquer dans la fenêtre de ton terminal, puis exécute `cd` par lui-même. Tu verras que son « invite » ressemble à ce qui suit.

    $

Clique dans cette fenêtre de terminal, puis exécute

    wget https://cdn.cs50.net/2023/fall/psets/3/sort.zip

puis appuie sur Entrée pour télécharger un fichier ZIP intitulé `sort.zip` dans ton espace de code. Attention à ne pas oublier l'espace entre `wget` et l'URL suivante, ou tout autre caractère d'ailleurs !

Exécute maintenant

    unzip sort.zip

afin de créer un dossier intitulé `sort`. Tu n'as désormais plus besoin du fichier ZIP, tu peux donc exécuter

    rm sort.zip

et répondre par « y » suivi d'Entrée à l'invite pour supprimer le fichier ZIP que tu as téléchargé.

## Astuces

### Explore les fichiers .txt

- Plusieurs fichiers .txt te sont fournis. Ces fichiers contiennent n lignes de valeurs, soit inversées, mélangées ou triées.
  - Par exemple, `reversed10000.txt` contient 10 000 lignes de nombres inversés de `10000`, tandis que `random50000.txt` contient 50 000 lignes de nombres dans un ordre aléatoire.
- Les différents types de fichiers .txt peuvent t'aider à déterminer quel tri est lequel. Réfléchis à la façon dont chaque algorithme se comporte avec une liste déjà triée. Et pour une liste inversée ? Ou une liste mélangée ? Il peut être utile de parcourir une petite liste de chaque type et de suivre chaque processus de tri.

### Chronomètre chaque tri avec des entrées différentes

- Pour exécuter les tris sur les fichiers texte, dans le terminal, exécute `./[nom_du_programme] [fichier_texte.txt]`. Vérifie que tu utilises `cd` pour te déplacer dans le répertoire `sort` !
  - Par exemple, pour trier `reversed10000.txt` avec `sort1`, exécute `./sort1 reversed10000.txt`.
- Tu peux trouver qu'il est utile de chronométrer tes tris. Pour ce faire, exécute `time ./[nom_du_fichier] [fichier_texte.txt]`.
  - Par exemple, tu peux exécuter `time ./sort1 reversed10000.txt` pour exécuter `sort1` sur 10 000 nombres inversés. À la fin de la sortie de ton terminal, tu peux regarder le temps « réel » pour voir combien de temps s'est réellement écoulé pendant l'exécution du programme.

## Procédure pas à pas

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/-Bhxxw6JKKY"></iframe>

<details><summary>Tu ne sais pas comment résoudre le problème ?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/uOYhrBs37j0"></iframe></details>

## Comment tester

### Exactitude

    check50 cs50/problems/2024/x/sort

## Comment soumettre

    submit50 cs50/problems/2024/x/sort