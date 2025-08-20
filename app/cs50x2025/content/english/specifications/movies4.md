### List the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred

Notice that this query, like the previous, requires you to use data from multiple tables. Recall that you can “nest” queries in SQL, which allows you to break a larger query into smaller ones. Perhaps you could write queries to…

1.  Find the ID of Bradley Cooper
2.  Find the ID of Jennifer Lawrence
3.  Find the IDs of movies associated with Bradley Cooper’s ID
4.  Find the IDs of movies associated with Jennifer Lawrence’s ID
5.  Find movie titles from the movie IDs associated with _both_ Bradley Cooper and Jennifer Lawrence

Then, try nesting those queries to arrive at a single query that returns the movies in which both Bradley Cooper and Jennifer Lawrence starred.

Recall that you can build compound conditions in SQL using `AND` or `OR`.

### List the names of all people who starred in a movie in which Kevin Bacon also starred

Notice that this query, like the previous, requires you to use data from multiple tables. Recall that you can “nest” queries in SQL, which allows you to break a larger query into smaller ones. Perhaps you could write queries to…

1.  Find the ID of Kevin Bacon (the one born in 1958!)
2.  Find the IDs of movies associated with Kevin Bacon’s ID
3.  Find the IDs of people associated with those movie IDs
4.  Find the names of people with those people IDs

Then, try nesting those queries to arrive at a single query that returns the names of all people who starred in a movie in which Kevin Bacon also starred. **Keep in mind that you’ll want to exclude Kevin Bacon himself from the results!**

## Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/v5_A3giDlQs?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Usage

To test your queries in VS Code, you can query the database by running

    $ cat filename.sql | sqlite3 movies.db

where `filename.sql` is the file containing your SQL query.

You can also run

    $ cat filename.sql | sqlite3 movies.db > output.txt

to redirect the output of the query to a text file called `output.txt`. (This can be useful for checking how many rows are returned by your query!)

## How to Test

While `check50` is available for this problem, you’re encouraged to instead test your code on your own for each of the following. You can run `sqlite3 movies.db` to run additional queries on the database to ensure that your result is correct.

If you’re using the `movies.db` database provided in this problem set’s distribution, you should find that

- Executing `1.sql` results in a table with 1 column and 10,276 rows.
- Executing `2.sql` results in a table with 1 column and 1 row.
- Executing `3.sql` results in a table with 1 column and 110,014 rows.
- Executing `4.sql` results in a table with 1 column and 1 row.
- Executing `5.sql` results in a table with 2 columns and 11 rows.
- Executing `6.sql` results in a table with 1 column and 1 row.
- Executing `7.sql` results in a table with 2 columns and 7,192 rows.
- Executing `8.sql` results in a table with 1 column and 4 rows.
- Executing `9.sql` results in a table with 1 column and 19,325 rows.
- Executing `10.sql` results in a table with 1 column and 3,854 rows.
- Executing `11.sql` results in a table with 1 column and 5 rows.
- Executing `12.sql` results in a table with 1 column and 4 rows.
- Executing `13.sql` results in a table with 1 column and 182 rows.

Note that row counts do not include header rows that only show column names.

If your query returns a number of rows that is slightly different from the expected output, be sure that you’re properly handling duplicates! For queries that ask for a list of names, no one person should be listed twice, but two different people who have the same name should each be listed.

### Correctness

    check50 cs50/problems/2024/x/movies

## How to Submit

    submit50 cs50/problems/2024/x/movies

## Acknowledgements

Information courtesy of IMDb ([imdb.com](https://www.imdb.com)). Used with permission.
