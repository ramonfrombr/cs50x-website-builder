### List the names of any songs that have danceability, energy, and valence greater than 0.75

Recall that you can filter results in SQL with `WHERE` clauses, which are followed by some condition which typically tests the values in a row’s columns.

Recall, too, that SQL’s operators function much the same way as C’s. For example, `>` evaluates to “true” when the value on the left is greater than the value on the right. You may chain these expressions together, using `AND` or `OR`, to form one larger condition.

In `4.sql`, then, try writing the following:

    -- The names of any songs that have danceability, energy, and valence greater than 0.75.
    SELECT name
    FROM songs
    WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75;

### Find average energy of all the songs

Recall that SQL supports keywords not just to select particular rows, but also to _aggregate_ the data in those rows. In particular, you might find the `AVG` keyword (to compute averages) useful. To aggregate the results of a column, just apply the aggregation function to that column. For example, `SELECT AVG(energy)` will find the average of the values in the energy column for the given query.

In `5.sql`, then, try writing the following:

    -- The average energy of all the songs.
    SELECT AVG(energy)
    FROM songs;

### List the names of songs that are by Post Malone

Notice that, if you execute `.schema songs` in your sqlite prompt, the `songs` table has song names but not artist names! Instead, `songs` has an `artist_id` column. To list the names of songs by Post Malone, then, you’ll first need to identify Post Malone’s artist id.

    -- Identify Post Malone's artist id
    SELECT id
    FROM artists
    WHERE name = 'Post Malone';

This query returns 54. Now, you could query the `songs` table for any song with Post Malone’s id.

    SELECT name
    FROM songs
    WHERE artist_id = 54;

But, per the specification, you should be mindful not to assume knowledge of any ids. You could improve the design of this query by _nesting_ your two queries.

In `6.sql`, then, try writing the following:

    -- The names of songs that are by Post Malone.
    SELECT name
    FROM songs
    WHERE artist_id =
    (
        SELECT id
        FROM artists
        WHERE name = 'Post Malone'
    );

### Find the average energy of songs that are by Drake

Notice that, similar to the previous query, you’ll need to combine multiple tables to successfully run this query. You could again use nested subqueries, but consider another approach too!

Recall that you can use SQL’s `JOIN` keyword to combine multiple tables into one, so long as you specify which columns across those tables should ultimately match. For example, the following query joins the `songs` and `artists` tables, indicating that the `artist_id` column in the `songs` table and the `id` column in the `artists` table should match:

    SELECT *
    FROM songs
    JOIN artists ON songs.artist_id = artists.id

With these two tables combined, it’s only a matter of filtering your selection to find the average energy of songs by Drake.

In `7.sql`, then, try writing the following:

    -- The average energy of songs that are by Drake
    SELECT AVG(energy)
    FROM songs
    JOIN artists ON songs.artist_id = artists.id
    WHERE artists.name = 'Drake';

### List the names of the songs that feature other artists

For this query, note that songs which feature other artists typically have some mention of “feat.” in their title. Recall that SQL’s `LIKE` keyword can be used to match strings with certain phrases (like “feat.”!). To do so, you can use `%`: a wildcard character that matches any sequence of characters.

In `8.sql`, then, try writing the following:

    -- The names of songs that feature other artists.
    SELECT name
    FROM songs
    WHERE name LIKE '%feat.%';

## Walkthrough

<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/wgKPUd_95AA"></iframe>

<details><summary>Not sure how to solve?</summary><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://video.cs50.io/7hydPL9ZswE"></iframe></details>

## Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) is a feature presenting Spotify users’ 100 most played songs from the past year. In 2021, Spotify Wrapped calculated an [“Audio Aura”](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) for each user, a “reading of \[their\] two most prominent moods as dictated by \[their\] top songs and artists of the year.” Suppose Spotify determines an audio aura by looking at the average energy, valence, and danceability of a person’s top 100 songs from the past year. In `answers.txt`, reflect on the following questions:

- If `songs.db` contains the top 100 songs of one listener from 2018, how would you characterize their audio aura?
- Hypothesize about why the way you’ve calculated this aura might _not_ be very representative of the listener. What better ways of calculating this aura would you propose?

Be sure to submit `answers.txt` along with each of your `.sql` files!

## How to Test

### Correctness

    check50 cs50/problems/2024/x/songs

## How to Submit

    submit50 cs50/problems/2024/x/songs

## Acknowledgements

Dataset from [Kaggle](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018).
