# Birthdays

![screenshot of birthdays website](https://cs50.harvard.edu/x/2024/psets/9/birthdays/birthdays.png)

## Problem to Solve

Create a web application to keep track of friends’ birthdays.

## Getting Started

Open [VS Code](https://cs50.dev/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2023/fall/psets/9/birthdays.zip

followed by Enter in order to download a ZIP called `birthdays.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip birthdays.zip

to create a folder called `birthdays`. You no longer need the ZIP file, so you can execute

    rm birthdays.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd birthdays

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    birthdays/ $

If all was successful, you should execute

    ls

and you should see the following files and folders:

    app.py  birthdays.db  static/  templates/

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

## Understanding

In `app.py`, you’ll find the start of a Flask web application. The application has one route (`/`) that accepts both `POST` requests (after the `if`) and `GET` requests (after the `else`). Currently, when the `/` route is requested via `GET`, the `index.html` template is rendered. When the `/` route is requested via `POST`, the user is redirected back to `/` via `GET`.

`birthdays.db` is a SQLite database with one table, `birthdays`, that has four columns: `id`, `name`, `month`, and `day`. There are a few rows already in this table, though ultimately your web application will support the ability to insert rows into this table!

In the `static` directory is a `styles.css` file containing the CSS code for this web application. No need to edit this file, though you’re welcome to if you’d like!

In the `templates` directory is an `index.html` file that will be rendered when the user views your web application.

## Implementation Details

Complete the implementation of a web application to let users store and keep track of birthdays.

- When the `/` route is requested via `GET`, your web application should display, in a table, all of the people in your database along with their birthdays.
  - First, in `app.py`, add logic in your `GET` request handling to query the `birthdays.db` database for all birthdays. Pass all of that data to your `index.html` template.
  - Then, in `index.html`, add logic to render each birthday as a row in the table. Each row should have two columns: one column for the person’s name and another column for the person’s birthday.
- When the `/` route is requested via `POST`, your web application should add a new birthday to your database and then re-render the index page.
  - First, in `index.html`, add an HTML form. The form should let users type in a name, a birthday month, and a birthday day. Be sure the form submits to `/` (its “action”) with a method of `post`.
  - Then, in `app.py`, add logic in your `POST` request handling to `INSERT` a new row into the `birthdays` table based on the data supplied by the user.

Optionally, you may also:

- Add the ability to delete and/or edit birthday entries.
- Add any additional features of your choosing!

## Hints

### Create a form via which users can submit birthdays

In `index.html`, notice the following TODO:

    <!-- TODO: Create a form for users to submit a name, a month, and a day -->

Recall that, to create a form, you can use the `form` HTML element. You can create a `form` HTML element with the following opening and closing tags:

    <form>
    </form>

Of course, a form still needs input fields (and a button via which the user can submit the form!). Recall that HTML `input` elements create, among other things, input boxes within a form. You can specify their `type` attribute to allow them to accept `text` or `number`s. Also give the `input` elements a `name` attribute so you can differentiate them.

    <form>
        <input name="name" type="text">
        <input name="month" type="number">
        <input name="day" type="number">
    </form>

Your form might benefit from a button the user could click to submit their data. Add an `input` element of type `submit`, which will allow the user to do just that. If you’d like the button itself to have explanatory text, try setting the `value` attribute.

    <form>
        <input name="name" type="text">
        <input name="month" type="number">
        <input name="day" type="number">
        <input type="submit" value="Add Birthday">
    </form>

Where will the user’s data be submitted? Currently, nowhere! Recall that you can specify a form’s `action` attribute to dictate which route should be requested after the form is submitted. The form data will be submitted along with the resulting request. The `method` attribute specifies which HTTP request method to use when submitting the form.

    <form action="/" method="post">
        <input name="name" type="text">
        <input name="month" type="number">
        <input name="day" type="number">
        <input type="submit" value="Add Birthday">
    </form>

With that, your form should be perfectly functional, though it could still be improved! Consider adding `placeholder` values to spruce things up a bit:

    <form action="/" method="post">
        <input name="name" placeholder="Name" type="text">
        <input name="month" placeholder="Month" type="number">
        <input name="day" placeholder="Day" type="number">
        <input type="submit" value="Add Birthday">
    </form>

And consider adding some _client-side validation_, to ensure the user cooperates with the intent of your form. For example, an `input` field of type `number` can also have a `min` and `max` attribute specified, which determine the minimum and maximum value a user can enter.

    <form action="/" method="post">
        <input name="name" placeholder="Name" type="text">
        <input name="month" placeholder="Month" type="number" min="1" max="12">
        <input name="day" placeholder="Day" type="number" min="1" max="31">
        <input type="submit" value="Add Birthday">
    </form>
