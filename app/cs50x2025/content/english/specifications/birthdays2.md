### Add a user's form submission to the database

In `app.py`, notice the following TODO:

    # TODO: Add the user's entry into the database

Recall that Flask has some handy methods to access form data submitted via `POST`! In particular:

    # Access form data
    request.form.get(NAME)

where `NAME` refers to the `name` attribute of the particular `input` element with submitted data. If your `input` elements were named `name`, `month`, and `day`, you could access (and store!) their values respectively with the following:

    # Access form data
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

Now the values submitted by the user in the `name`, `month`, and `day` input elements are available to you as Python variables.

The next step is to add these values to your database! Thanks to this particular line

    db = SQL("sqlite:///birthdays.db")

`app.py` has already established a connection to `birthdays.db` under the name `db`. You can now execute SQL queries by calling `db.execute` with a valid SQL query. If you wanted to add Carter’s birthday on January 1st, you might run the following SQL statement:

    INSERT INTO birthdays (name, month, day) VALUES('Carter', 1, 1);

Configure `app.py` to run that same query, but with placeholders for the values to insert, as follows:

    # Access form data
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

    # Insert data into database
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

And that should do it! Try submitting the form, opening `birthdays.db`, and using a `SELECT` query to view the contents of the `birthdays` table. You should see the submitted form data available to you.

As you create more advanced applications, you’ll also want to add _server-side validation_: that is, a way to check whether the user’s data is valid _before_ doing anything else! One of the first validations you might make is whether the user submitted any data at all! Should you try to retrieve form data with `request.form.get` where the user didn’t submit any, `request.form.get` will return an empty string. You can check for this value in Python as follows:

    # Access form data
    name = request.form.get("name")
    if not name:
        return redirect("/")

    month = request.form.get("month")
    if not month:
        return redirect("/")

    day = request.form.get("day")
    if not day:
        return redirect("/")

    # Insert data into database
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

Now, you won’t insert a row until you’re sure the user has provided all the data you need.

A few more things could still go wrong! What if the user doesn’t, in fact, provide a numeric value for `month` or `day`? One way to check is to `try` to convert the value to an integer with `int` and, if the conversion fails, to redirect the user back to the homepage.

    # Access form data
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

    # Insert data into database
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

And even if the user has entered a number, best to check it’s in the right range!

    # Access form data
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

    # Insert data into database
    db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
