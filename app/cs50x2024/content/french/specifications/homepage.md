# Page d’accueil

Créez une page d’accueil simple à l’aide de HTML, CSS et JavaScript.

## Contexte

Internet a rendu possible des choses incroyables : nous pouvons utiliser un moteur de recherche pour obtenir des informations sur tout ce que l’on peut imaginer, communiquer avec des amis et des membres de notre famille dans le monde entier, jouer à des jeux, suivre des cours, et bien plus encore. Mais il s’avère que presque toutes les pages que nous pouvons visiter sont construites sur trois langages de base, chacun ayant un objectif légèrement différent :

1.  HTML, ou _HyperText Markup Language_, qui est utilisé pour décrire le contenu des sites Web ;
2.  CSS, _Cascading Style Sheets_, qui est utilisé pour décrire l’esthétique des sites Web ; et
3.  JavaScript, qui est utilisé pour rendre les sites Web interactifs et dynamiques.

Créez une page d’accueil simple qui vous présente, votre passe-temps ou activité parascolaire favori, ou tout autre sujet qui vous intéresse.

## Pour commencer

Connectez-vous à [cs50.dev](https://cs50.dev/), cliquez sur votre fenêtre de terminal et exécutez `cd` tout seul. Vous devriez constater que l’invite de votre fenêtre de terminal ressemble à ce qui suit :

    $

Exécutez ensuite

    wget https://cdn.cs50.net/2023/fall/psets/8/homepage.zip

afin de télécharger un fichier ZIP appelé `homepage.zip` dans votre espace de codes.

Exécutez ensuite

    unzip homepage.zip

pour créer un dossier appelé `homepage`. Vous n’avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm homepage.zip

et répondre par « y » suivi d’Entrée à l’invite pour supprimer le fichier ZIP que vous avez téléchargé.

Tapez maintenant

    cd homepage

suivi d’Entrée pour vous déplacer dans (c’est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit :

    homepage/ $

Exécutez `ls` tout seul, et vous devriez voir quelques fichiers :

    index.html  styles.css

Si vous rencontrez des problèmes, suivez à nouveau ces mêmes étapes et voyez si vous pouvez déterminer où vous vous êtes trompé ! Vous pouvez immédiatement démarrer un serveur pour afficher votre site en exécutant

    http-server

dans la fenêtre du terminal. Puis, cliquez avec la touche Commande (si vous êtes sur Mac) ou avec la touche Contrôle (si vous êtes sur PC) sur le premier lien qui apparaît :

    http-server running on LINK

Où LINK est l’adresse de votre serveur.

## Spécification

Implémentez dans votre répertoire `homepage` un site Web qui doit :

- Contenir au moins quatre pages `.html` différentes, dont au moins une est `index.html` (la page principale de votre site Web), et il doit être possible d’accéder à n’importe quelle page de votre site Web à partir de n’importe quelle autre page en suivant un ou plusieurs hyperliens.
- Utiliser au moins dix (10) balises HTML distinctes en plus de`<html>`, `<head>`, `<body>` et `<title>`. L’utilisation d’une balise (par exemple, `<p>`) plusieurs fois compte toujours comme une (1) de ces dix !
- Intégrer une ou plusieurs fonctionnalités de Bootstrap dans votre site. Bootstrap est une bibliothèque populaire (qui est fournie avec de nombreuses classes CSS et plus) grâce à laquelle vous pouvez embellir votre site. Consultez [la documentation de Bootstrap](https://getbootstrap.com/docs/5.2/) pour commencer. En particulier, certains [composants de Bootstrap](https://getbootstrap.com/docs/5.2/components/) pourraient vous intéresser. Pour ajouter Bootstrap à votre site, il suffit d’inclure

        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

dans le `<head>` de vos pages, en dessous duquel vous pouvez également inclure

        <link href="styles.css" rel="stylesheet">

pour lier votre propre CSS.

- Avoir au moins un fichier de feuille de style de votre propre création, `styles.css`, qui utilise au moins cinq (5) sélecteurs CSS différents (par exemple, balise (`example`), classe (`.example`) ou ID (`#example`)), et dans lequel vous utilisez au total au moins cinq (5) propriétés CSS différentes, telles que `font-size` ou `margin` ; et
- Intégrer une ou plusieurs fonctionnalités de JavaScript dans votre site pour rendre votre site plus interactif. Par exemple, vous pouvez utiliser JavaScript pour ajouter des alertes, pour avoir un effet à un intervalle récurrent, ou pour ajouter de l’interactivité aux boutons, aux menus déroulants ou aux formulaires. N’hésitez pas à être créatif !
- Assurez-vous que votre site s’affiche correctement sur les navigateurs des appareils mobiles ainsi que sur les ordinateurs portables et les ordinateurs de bureau.

Vous devez également créer un fichier texte, `specification.txt`, qui répertorie les 10 balises HTML et les 5 propriétés CSS que vous avez utilisées, ainsi qu’une brève description (en une phrase) de la façon dont vous avez choisi d’utiliser JavaScript et Bootstrap.

## Test

Si vous souhaitez voir à quoi ressemble votre site pendant que vous travaillez dessus, vous pouvez exécuter `http-server`. Cliquez avec la touche Commande ou Contrôle sur le premier lien présenté par http-server, ce qui devrait ouvrir votre page Web dans un nouvel onglet. Vous devriez alors être en mesure d’actualiser l’onglet contenant votre page Web pour voir vos dernières modifications.

Rappelez-vous également qu’en ouvrant les outils de développement dans Google Chrome, vous pouvez _simuler_ la visite de votre page sur un appareil mobile en cliquant sur l’icône en forme de téléphone à gauche de **Éléments** dans la fenêtre des outils de développement ou, une fois que l’onglet Outils de développement a déjà été ouvert, en tapant `Ctrl`+`Shift`+`M` sur un PC ou `Cmd`+`Shift`+`M` sur un Mac, plutôt que de devoir visiter votre site sur un appareil mobile séparément !

## Évaluation

Pas de `check50` pour cet exercice ! Au lieu de cela, l’exactitude de votre site sera évaluée en fonction de votre respect des exigences de la spécification, telles que décrites ci-dessus, et de la validité et de la régularité de votre HTML. Pour vous assurer que vos pages le sont, vous pouvez utiliser ce [service de validation de balisage](https://validator.w3.org/#validate_by_input), en copiant et collant votre HTML directement dans la zone de texte fournie. Prenez soin d’éliminer tous les avertissements ou erreurs suggérés par le validateur avant de soumettre !

Pensez également :

- si l’esthétique de votre site est telle qu’il est intuitif et simple pour un utilisateur à naviguer ;
- si votre CSS a été factorisé dans un ou plusieurs fichiers CSS séparés ; et
- si vous avez évité la répétition et la redondance en « cascade » des propriétés de style des balises parentes.

Attention, `style50` ne prend pas en charge les fichiers HTML, il vous incombe donc d’indenter et d’aligner proprement vos balises HTML. Sachez également que vous pouvez créer un commentaire HTML avec :

    <!-- Commentaire ici -->

mais commenter votre code HTML n’est pas aussi impératif que commenter le code dans, par exemple, C ou Python. Vous pouvez également commenter votre CSS, dans les fichiers CSS, avec :

    /* Commentaire ici */

## Astuces

Pour des guides relativement complets sur les langages introduits dans ce problème, consultez ces tutoriels :

- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com