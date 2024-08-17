## Anniversaires

![capture d’écran du site web Anniversaires](https://cs50.harvard.edu/x/2024/psets/9/birthdays/birthdays.png)

## Problème à résoudre

Créez une application web pour suivre les anniversaires de vos amis.

## Pour commencer

Ouvrez [VS Code](https://cs50.dev/).

Pour commencer, cliquez dans la fenêtre de votre terminal, puis exécutez `cd` tout seul. Vous devriez constater que son « message » ressemble à celui ci-dessous.

    $

Cliquez dans cette fenêtre de terminal, puis exécutez

    wget https://cdn.cs50.net/2023/fall/psets/9/birthdays.zip

suivi de Entrée pour télécharger un ZIP appelé `birthdays.zip` dans votre espace de codage. Veillez à ne pas oublier l’espace entre `wget` et l’URL suivante, ni aucun autre caractère d’ailleurs !

Maintenant, exécutez

    unzip birthdays.zip

pour créer un dossier appelé `birthdays`. Vous n’avez plus besoin du fichier ZIP, vous pouvez donc exécuter

    rm birthdays.zip

et répondre par « y » suivi de Entrée à l’invite pour supprimer le fichier ZIP que vous avez téléchargé.

Maintenant, tapez

    cd birthdays

suivi de Entrée pour vous déplacer dans (c'est-à-dire ouvrir) ce répertoire. Votre invite devrait maintenant ressembler à ce qui suit :

    birthdays/ $

Si tout s’est bien passé, vous devez exécuter

    ls

et vous devriez voir les fichiers et dossiers suivants :

    app.py  birthdays.db  static/  templates/

Si vous rencontrez des problèmes, suivez à nouveau les mêmes étapes et voyez si vous pouvez déterminer où vous vous trompez !

## Compréhension

Dans `app.py`, vous trouverez le début d’une application web Flask. L’application comporte une route (`/`) qui accepte à la fois les requêtes `POST` (après `if`) et les requêtes `GET` (après `else`). Actuellement, lorsque la route `/` est demandée via `GET`, le modèle `index.html` est restitué. Lorsque la route `/` est demandée via `POST`, l’utilisateur est redirigé vers `/` via `GET`.

`birthdays.db` est une base de données SQLite avec une table, `birthdays`, qui comporte quatre colonnes : `id`, `name`, `month` et `day`. Il y a déjà quelques lignes dans cette table, bien que votre application web permette finalement d’insérer des lignes dans cette table !

Dans le répertoire `static`, il y a un fichier `styles.css` contenant le code CSS pour cette application web. Pas besoin de modifier ce fichier, bien que vous puissiez le faire si vous le souhaitez !

Dans le répertoire `templates`, il y a un fichier `index.html` qui sera restitué lorsque l’utilisateur consulte votre application web.

## Détails de l’implémentation

Terminez la mise en œuvre d’une application web permettant aux utilisateurs de stocker et de suivre les anniversaires.

- Lorsque la route `/` est demandée via `GET`, votre application web doit afficher, dans un tableau, toutes les personnes de votre base de données ainsi que leurs anniversaires.
  - Tout d’abord, dans `app.py`, ajoutez une logique dans la gestion de votre requête `GET` pour interroger la base de données `birthdays.db` pour tous les anniversaires. Transmettez toutes ces données à votre modèle `index.html`.
  - Ensuite, dans `index.html`, ajoutez une logique pour restituer chaque anniversaire comme une ligne dans le tableau. Chaque ligne doit comporter deux colonnes : une colonne pour le nom de la personne et une autre colonne pour l’anniversaire de la personne.
- Lorsque la route `/` est demandée via `POST`, votre application web doit ajouter un nouvel anniversaire à votre base de données, puis restituer à nouveau la page d’accueil.
  - Tout d’abord, dans `index.html`, ajoutez un formulaire HTML. Le formulaire doit permettre aux utilisateurs de taper un nom, un mois d’anniversaire et un jour d’anniversaire. Assurez-vous que le formulaire est envoyé à `/` (son « action ») avec une méthode de `post`.
  - Ensuite, dans `app.py`, ajoutez une logique dans votre gestion de demande `POST` pour `INSÉRER` une nouvelle ligne dans la table `birthdays` en fonction des données fournies par l’utilisateur.

En option, vous pouvez également :

- Ajouter la possibilité de supprimer et/ou de modifier des entrées d’anniversaire.
- Ajouter des fonctionnalités supplémentaires de votre choix !

## Astuces

### Créer un formulaire via lequel les utilisateurs peuvent soumettre des anniversaires

Dans `index.html`, notez ce TODO :

    <!-- TODO : Créer un formulaire permettant aux utilisateurs de soumettre un nom, un mois et un jour -->

Souvenez-vous que pour créer un formulaire, vous pouvez utiliser l’élément HTML `form`. Vous pouvez créer un élément HTML `form` avec les balises d’ouverture et de fermeture suivantes :

    <form>
    </form>

Bien sûr, un formulaire a encore besoin de champs de saisie (et d’un bouton via lequel l’utilisateur peut soumettre le formulaire !). Souvenez-vous que les éléments HTML `input` créent, entre autres, des zones de saisie dans un formulaire. Vous pouvez spécifier leur attribut `type` pour leur permettre d’accepter du `texte` ou des `nombres`. Attribuez également aux éléments `input` un attribut `name` afin de pouvoir les différencier.

    <form>
        <input name="name" type="text">
        <input name="month" type="number">
        <input name="day" type="number">
    </form>

Votre formulaire peut bénéficier d’un bouton sur lequel l’utilisateur peut cliquer pour soumettre ses données. Ajoutez un élément `input` de type `submit`, qui permettra à l’utilisateur de faire exactement cela. Si vous souhaitez que le bouton lui-même comporte un texte explicatif, essayez de définir l’attribut `value`.

    <form>
        <input name="name" type="text">
        <input name="month" type="number">
        <input name="day" type="number">
        <input type="submit" value="Ajouter un anniversaire">
    </form>

Où seront soumises les données de l’utilisateur ? Actuellement, nulle part ! Souvenez-vous que vous pouvez spécifier l’attribut `action` d’un formulaire pour indiquer quelle route doit être demandée après la soumission du formulaire. Les données du formulaire seront soumises avec la demande résultante. L’attribut `method` spécifie quelle méthode de demande HTTP utiliser lors de la soumission du formulaire.

    <form action="/" method="post">
        <input name="name" type="text">
        <input name="month" type="number">
        <input name="day" type="number">
        <input type="submit" value="Ajouter un anniversaire">
    </form>

Avec cela, votre formulaire devrait être parfaitement fonctionnel, bien qu’il puisse encore être amélioré ! Envisagez d’ajouter des valeurs `placeholder` pour améliorer un peu les choses :

    <form action="/" method="post">
        <input name="name" placeholder="Nom" type="text">
        <input name="month" placeholder="Mois" type="number">
        <input name="day" placeholder="Jour" type="number">
        <input type="submit" value="Ajouter un anniversaire">
    </form>

Et envisagez d’ajouter une certaine validation côté client pour vous assurer que l’utilisateur coopère avec l’intention de votre formulaire. Par exemple, un champ `input` de type `number` peut également avoir un attribut `min` et `max` spécifié, qui détermine la valeur minimale et maximale qu’un utilisateur peut saisir.

    <form action="/" method="post">
        <input name="name" placeholder="Nom" type="text">
        <input name="month" placeholder="Mois" type="number" min="1" max="12">
        <input name="day" placeholder="Jour" type="number" min="1" max="31">
        <input type="submit" value="Ajouter un anniversaire">
    </form>

### Ajouter une requête de formulaire d'utilisateur à la base de données

Dans `app.py`, remarquez la note TODO suivante :

    # TODO : Ajouter la saisie de l'utilisateur à la base de données

N'oubliez pas que Flask dispose de quelques méthodes pratiques pour accéder aux données de formulaire soumises via `POST` ! En particulier :

    # Accéder aux données du formulaire
    request.form.get(NAME)

où `NAME` fait référence à l'attribut `name` de l'élément `input` particulier avec les données soumises. Si vos éléments `input` ont été nommés `name`, `month` et `day`, vous pouvez accéder (et stocker !) leurs valeurs respectivement avec les éléments suivants :

    # Accéder aux données du formulaire
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

Les valeurs soumises par l'utilisateur dans les éléments d'entrée `name`, `month` et `day` sont maintenant disponibles pour vous en tant que variables Python.

L'étape suivante consiste à ajouter ces valeurs à votre base de données ! Grâce à cette ligne particulière :

    db = SQL("sqlite:///birthdays.db")

`app.py` a déjà établi une connexion avec `birthdays.db` sous le nom de `db`. Vous pouvez maintenant exécuter des requêtes SQL en appelant `db.execute` avec une requête SQL valide. Si vous souhaitez ajouter l'anniversaire de Carter le 1er janvier, vous pouvez exécuter l'instruction SQL suivante :

    INSERT INTO birthdays (name, month, day) VALUES('Carter', 1, 1);

Configurez `app.py` pour qu'il exécute cette même requête, mais avec des espaces réservés pour les valeurs à insérer, comme suit :

    # Accéder aux données du formulaire
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

    # Insérer des données dans la base de données
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

Et cela devrait faire l'affaire ! Essayez de soumettre le formulaire, d'ouvrir `birthdays.db` et d'utiliser une requête `SELECT` pour afficher le contenu de la table `birthdays`. Vous devriez voir les données du formulaire soumis à votre disposition.

Au fur et à mesure que vous créez des applications plus avancées, vous voudrez également ajouter une _validation côté serveur_ : autrement dit, un moyen de vérifier si les données de l'utilisateur sont valides _avant_ de faire quoi que ce soit d'autre ! L'une des premières validations que vous pouvez effectuer est de vérifier si l'utilisateur a soumis des données ou non ! Si vous essayez de récupérer les données du formulaire avec `request.form.get` et que l'utilisateur n'en a soumis aucune, `request.form.get` renverra une chaîne vide. Vous pouvez vérifier cette valeur en Python comme suit :

    # Accéder aux données du formulaire
    name = request.form.get("name")
    if not name:
        return redirect("/")

    month = request.form.get("month")
    if not month:
        return redirect("/")

    day = request.form.get("day")
    if not day:
        return redirect("/")

    # Insérer des données dans la base de données
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

Désormais, vous n'insérerez pas de ligne tant que vous ne serez pas sûr que l'utilisateur a fourni toutes les données dont vous avez besoin.

Quelques autres choses pourraient toujours mal tourner ! Et si l'utilisateur ne fournissait en fait pas une valeur numérique pour `month` ou `day` ? Une façon de vérifier est d'essayer de convertir la valeur en un entier avec `int` et, si la conversion échoue, de rediriger l'utilisateur vers la page d'accueil.

    # Accéder aux données du formulaire
    name = request.form.get("name")
    if not name:
        return redirect("/")

    month = request.form.get("month")
    if not month:
        return redirect("/")
    try:
        month = int(month)
    except ValueError:
        return redirect("/")

    day = request.form.get("day")
    if not day:
        return redirect("/")
    try:
        day = int(day)
    except ValueError:
        return redirect("/")

    # Insérer des données dans la base de données
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

Et même si l'utilisateur a entré un nombre, il est préférable de vérifier qu'il se trouve dans la bonne plage !

    # Accéder aux données du formulaire
    name = request.form.get("name")
    if not name:
        return redirect("/")

    month = request.form.get("month")
    if not month:
        return redirect("/")
    try:
        month = int(month)
    except ValueError:
        return redirect("/")
    if month < 1 or month > 12:
        return redirect("/")

    day = request.form.get("day")
    if not day:
        return redirect("/")
    try:
        day = int(day)
    except ValueError:
        return redirect("/")
    if day < 1 or day > 31:
        return redirect("/")

    # Insérer des données dans la base de données
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

### Afficher les anniversaires dans `birthdays.db`

Une fois qu'un utilisateur peut envoyer des anniversaires et les stocker dans `birthdays.db`, votre prochaine tâche est de vous assurer que ces anniversaires sont affichés dans `index.html`.

Tout d'abord, vous devez récupérer tous les anniversaires de `birthdays.db`. Vous pourriez le faire avec la requête SQL :

    SELECT * FROM birthdays;

Voir la TODO suivante dans `app.py` :

    # TODO : Afficher les entrées de la base de données sur index.html

Envisagez de configurer `app.py` pour exécuter cette requête SQL chaque fois que la page est chargée avec une requête `GET` :

    # Requête pour tous les anniversaires
    birthdays = db.execute("SELECT * FROM birthdays")

Maintenant, tous les anniversaires dans la table `birthdays` de `birthdays.db` sont à votre disposition dans une variable Python nommée `birthdays`. En particulier, les résultats de la requête SQL sont stockés sous forme d'une liste de dictionnaires. Chaque dictionnaire représente une ligne retournée par la requête, et chaque clé dans le dictionnaire correspond à un nom de colonne de la table `birthdays` (c'est-à-dire « nom », « mois » et « jour »).

Pour afficher ces anniversaires dans `index.html`, vous pouvez vous baser sur la fonction `render_template` de Flask. Vous pouvez spécifier que `index.html` doit être rendu avec la variable `birthdays` en spécifiant un argument de mot-clé, également appelé `birthdays`, et en le définissant égal à la variable `birthdays` que vous venez de créer.

    # Requête pour tous les anniversaires
    birthdays = db.execute("SELECT * FROM birthdays")

    # Afficher la page d'anniversaires
    return render_template("index.html", birthdays=birthdays)

Pour être clair, le nom sur le côté gauche du `=`, `birthdays`, est le nom sous lequel vous pouvez accéder aux données d'anniversaire dans `index.html` lui-même.

Maintenant que `index.html` est rendu avec un accès aux données d'anniversaire, vous pouvez utiliser Jinja pour afficher correctement les données. Jinja, comme Python, peut parcourir les éléments d'une liste. Et Jinja, comme Python, peut accéder aux éléments d'un dictionnaire par leurs clés. Dans ce cas, la syntaxe Jinja pour le faire est le nom du dictionnaire, suivi d'un `.`, puis du nom de la clé d'accès.

    {% for birthday in birthdays %}
        <tr>
            <td></td>
            <td>/</td>
        </tr>
    {% endfor %}

Et c'est tout ! Essayez de recharger la page pour voir les anniversaires affichés.

### Procédure détaillée

<div class="alert alert-primary" data-alert="primary" role="alert"><p>Cette vidéo a été enregistrée lorsque le cours utilisait encore CS50 IDE pour écrire le code. Bien que l'interface puisse sembler différente de votre espace de codes, le comportement des deux environnements devrait être largement similaire !</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/HXwvj8x1Fcs"></iframe>

<details><summary>Vous ne savez pas comment résoudre ?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/lVwv4o8vmvI"></iframe></details>

### Test

Pas de `check50` pour cette série de problèmes ! Mais assurez-vous de tester votre application Web en ajoutant des anniversaires et en vous assurant que les données apparaissent dans votre tableau comme prévu.

Exécutez `flask run` dans votre terminal lorsque vous êtes dans votre répertoire `birthdays` pour démarrer un serveur Web qui dessert votre application Flask.

## Comment soumettre

    submit50 cs50/problems/2024/x/birthdays

