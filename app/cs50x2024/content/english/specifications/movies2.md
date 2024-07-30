## Hints

### Understand the schema of `movies.db`

Whenever you engage with a new database, it’s best to first understand its _schema_. In a terminal window, run `sqlite3 movies.db` so that you can begin executing queries on the database.

First, when `sqlite3` prompts you to provide a query, type `.schema` and press enter. This will output the `CREATE TABLE` statements that were used to generate each of the tables in the database. By examining those statements, you can identify the columns present in each table.

Notice that the `movies` table has an `id` column that uniquely identifies each movie, as well as columns for the `title` of a movie and the `year` in which the movie was released. The `people` table also has an `id` column, and also has columns for each person’s `name` and `birth` year.

Movie ratings, meanwhile, are stored in the `ratings` table. The first column in the table is `movie_id`: a foreign key that references the `id` of the `movies` table. The rest of the row contains data about the `rating` for each movie and the number of `votes` the movie has received on IMDb.

Finally, the `stars` and `directors` tables match people to the movies in which they acted or directed. (Only [principal](https://www.imdb.com/interfaces/) stars and directors are included.) Each table has just two columns: `movie_id` and `person_id`, which reference a specific movie and person, respectively.

The challenge ahead of you is to write SQL queries to answer a variety of different questions by selecting data from one or more of these tables.

### Consistently style your queries

See [sqlstyle.guide](https://www.sqlstyle.guide/) for pointers on good style in SQL, especially as your queries get more complex!

### List the titles of all movies released in 2008

Recall that you can select one (or more) columns from a database using `SELECT`, per the example below,

    SELECT column0, column1 FROM table;

where `column0` is the title of one column, and `column1` is the title of another.

And recall that you can filter the rows returned in a query with the `WHERE` keyword, followed by a condition. You can use `=`, `>`, `<`, and [other operators](https://www.w3schools.com/sql/sql_operators.asp) too.

    SELECT column FROM table
    WHERE condition;

See [this SQL keywords reference](https://www.w3schools.com/sql/sql_ref_keywords.asp) for some SQL syntax that may be helpful!

### Determine the birth year of Emma Stone

Recall that a `WHERE` clause can evaluate conditions not just with numbers, but with strings.

### List the titles of all movies with a release date on or after 2018, in alphabetical order

Try breaking this query into two steps. First, find the movies with a release date on or after 2018. Then, put those movies’ titles in alphabetical order.

To find the movies with a release date on or after 2018, recall that a condition in SQL supports the use of many common [comparison operators](https://www.w3schools.com/sql/sql_operators.asp), including `>=` for “greater than or equal to.” Check to see if your query returns the correct number of movies, per [How to Test](#how-to-test).

Finally, sort the query’s results alphabetically by title. Recall that `ORDER BY` can sort data by a column in your results, per the example below.

    ...
    ORDER BY column;

### Determine the number of movies with an IMDb rating of 10.0

Notice this question asks you not for _individual_ movies with a rating of 10.0, but for the _number_ of movies with such a rating. In other words, you should collect (“aggregate”) the results of your query into a single number (the number of rows). Recall that SQL supports an “aggregation function” called `COUNT`, which you can use on a column per the example below.

    SELECT COUNT(column)
    FROM table;

### List the titles and release years of all Harry Potter movies, in chronological order

For this query, you’ll likely want to make use of SQL’s `LIKE` keyword. Recall that `LIKE` can make use of so-called “wildcard characters”, such as `%`, that will match any character (or sequence thereof).

    SELECT column0, column1
    FROM table
    WHERE column1 LIKE pattern;

### Determine the average rating of all movies released in 2012

Here’s another example of a query in which you’ll need to aggregate data. Consider SQL’s `AVG` aggregation function, to compute an average.

Consider, too, that this query makes use of data stored in two separate tables: `ratings` and `movies`. Recall that—so long as one table has a foreign key that matches a column in another table—you can combine two tables using SQL’s `JOIN` keyword. To use the `JOIN` keyword, you should specify the table you’d like to join and the column by which to do so.

    SELECT column0
    FROM table0
    JOIN table1 ON table0.column1 = table1.column2

### List all movies released in 2010 and their ratings, in descending order by rating

Recall that `ORDER BY` need not always sort in ascending order. You can specify that your results be sorted in _descending_ order by appending `DESC`.

    ...
    ORDER BY column DESC;
