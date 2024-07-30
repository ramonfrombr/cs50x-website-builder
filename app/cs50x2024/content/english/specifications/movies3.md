### List the names of all people who starred in Toy Story

When you see a more complex query such as this one, it’s best to break it down into smaller pieces. Ultimately, your query should arrive at a list of names, per the below.

    -- Select names
    SELECT name
    FROM people
    WHERE ...

But how’s best to arrive at the names of those who starred in Toy Story? Consider that the `people` table alone doesn’t have this information (but the `stars` table might!). Indeed, the `stars` table combines two columns, `person_id` and `movie_id`: any person with a `person_id` that is associated with Toy Story’s `movie_id` starred in Toy Story.

    -- Select names
    SELECT name
    FROM people
    WHERE ...

    -- Select person IDs
    SELECT person_id
    FROM stars
    WHERE movie_id = ...

A natural next step, then, is to find Toy Story’s movie ID.

    -- Select names
    SELECT name
    FROM people
    WHERE ...

    -- Select person IDs
    SELECT person_id
    FROM stars
    WHERE movie_id = ...

    -- Find Toy Story's ID
    SELECT id
    FROM movies
    WHERE title = 'Toy Story';

Of course, you’ve presently written three _separate_ queries. But notice that some queries (the first two) would be complete by including results of the query directly below them. The process of making a query that depends on the results of a “subquery” is called “nesting” queries. It’s quite the hint, but here’s one way to nest the above queries!

    -- Select names
    SELECT name
    FROM people
    WHERE id IN
    (
        -- Select person IDs
        SELECT person_id
        FROM stars
        WHERE movie_id = (

            -- Select Toy Story's ID
            SELECT id
            FROM movies
            WHERE title = 'Toy Story'
        )
    );

### List the names of all people who starred in a movie released in 2004, ordered by birth year

Notice that this query, like the previous, requires you to use data from multiple tables. Recall that you can “nest” queries in SQL, which allows you to break a larger query into smaller ones. Perhaps you could write queries to…

1.  Find the IDs of movies released in 2004
2.  Find the IDs of people who starred in those movies
3.  Find the names of people with those people IDs

Then, try nesting those queries to arrive at a single query that returns all people who starred in a movie released in 2004. Consider how you might then order the results of your query.

### List the names of all people who have directed a movie that received a rating of at least 9.0

Notice that this query, like the previous, requires you to use data from multiple tables. Recall that you can “nest” queries in SQL, which allows you to break a larger query into smaller ones. Perhaps you could write queries to…

1.  Find the IDs of movies with at least a 9.0 rating
2.  Find the IDs of people who directed those movies
3.  Find the names of people with those people IDs

Then, try nesting those queries to arrive at a single query that returns the names of all people who have directed a movie that received a rating of at least 9.0.

### List the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated

Notice that this query, like the previous, requires you to use data from multiple tables. Recall that you can “nest” queries in SQL, which allows you to break a larger query into smaller ones. Perhaps you could write queries to…

1.  Find the ID of Chadwick Boseman
2.  Find the IDs of movies associated with Chadwick Boseman’s ID
3.  Find the movie titles with those movie IDs

Then, try nesting those queries to arrive at a single query that returns the titles of Chadwick Boseman’s movies.

From there, you’ll need to determine the ratings of those titles and sort those titles by rating, in descending order. Consider how you could combine a relevant table (likely `ratings`!) and order the results by a relevant column.

Finally, read up on SQL’s [`LIMIT`](https://www.sqlitetutorial.net/sqlite-limit/) keyword, which will return the top \\(n\\) rows in a query.
