### Render birthdays in `birthdays.db`

Once a user can submit birthdays and store them in `birthdays.db`, your next task is to ensure those birthdays are rendered in `index.html`.

First, you’ll need to retrieve all birthdays from `birthdays.db`. You could so with the SQL query:

    SELECT * FROM birthdays;

See the following TODO in `app.py`:

    # TODO: Display the entries in the database on index.html

Consider configuring `app.py` to run this SQL query each time the page is loaded with a `GET` request:

    # Query for all birthdays
    birthdays = db.execute("SELECT * FROM birthdays")

Now, all birthdays in the `birthdays` table of `birthdays.db` are available to you in a Python variable named `birthdays`. In particular, the results of the SQL query are stored as a list of dictionaries. Each dictionary represents one row returned by the query, and each key in the dictionary corresponds to a column name of the `birthdays` table (i.e., “name”, “month”, and “day”).

To render these birthdays in `index.html`, you can rely on Flask’s `render_template` function. You can specify that `index.html` should be rendered with the `birthdays` variable by specifying a keyword argument, also called `birthdays`, and setting it equal to the `birthdays` variable you just recently created.

    # Query for all birthdays
    birthdays = db.execute("SELECT * FROM birthdays")

    # Render birthdays page
    return render_template("index.html", birthdays=birthdays)

To be clear, the name on the left-hand side of the `=`, `birthdays`, is the name under which you can access the birthdays data within `index.html` itself.

Now that `index.html` is being rendered with access to the birthdays data, you can use Jinja to render the data properly. Jinja, like Python, can loop through elements of a list. And Jinja, like Python, can access elements a dictionary by their keys. In this case, the Jinja syntax to do so is the name of the dictionary, followed by a `.`, then the name of the key to access.

    {% for birthday in birthdays %}
        <tr>
            <td></td>
            <td>/</td>
        </tr>
    {% endfor %}

And that’s it! Try reloading the page to see the birthdays rendered.

### Walkthrough

<div class="alert alert-primary" data-alert="primary" role="alert"><p>This video was recorded when the course was still using CS50 IDE for writing code. Though the interface may look different from your codespace, the behavior of the two environments should be largely similar!</p></div>

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/HXwvj8x1Fcs"></iframe>

<details><summary>Not sure how to solve?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/lVwv4o8vmvI"></iframe></details>

### Testing

No `check50` for this problem set! But be sure to test your web application by adding some birthdays and ensuring that the data appears in your table as expected.

Run `flask run` in your terminal while in your `birthdays` directory to start a web server that serves your Flask application.

## How to Submit

    submit50 cs50/problems/2024/x/birthdays
