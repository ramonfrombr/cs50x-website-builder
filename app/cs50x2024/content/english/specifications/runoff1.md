# Runoff

## Problem to Solve

You already know about plurality elections, which follow a very simple algorithm for determining the winner of an election: every voter gets one vote, and the candidate with the most votes wins.

But the plurality vote does have some disadvantages. What happens, for instance, in an election with three candidates, and the ballots below are cast?

![Five ballots, tie betweeen Alice and Bob](https://cs50.harvard.edu/x/2024/psets/3/fptp_ballot_1.png)

A plurality vote would here declare a tie between Alice and Bob, since each has two votes. But is that the right outcome?

There’s another kind of voting system known as a ranked-choice voting system. In a ranked-choice system, voters can vote for more than one candidate. Instead of just voting for their top choice, they can rank the candidates in order of preference. The resulting ballots might therefore look like the below.

![Five ballots, with ranked preferences](https://cs50.harvard.edu/x/2024/psets/3/ranked_ballot_1.png)

Here, each voter, in addition to specifying their first preference candidate, has also indicated their second and third choices. And now, what was previously a tied election could now have a winner. The race was originally tied between Alice and Bob, so Charlie was out of the running. But the voter who chose Charlie preferred Alice over Bob, so Alice could here be declared the winner.

Ranked choice voting can also solve yet another potential drawback of plurality voting. Take a look at the following ballots.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2024/psets/3/ranked_ballot_3.png)

Who should win this election? In a plurality vote where each voter chooses their first preference only, Charlie wins this election with four votes compared to only three for Bob and two for Alice. But a majority of the voters (5 out of the 9) would be happier with either Alice or Bob instead of Charlie. By considering ranked preferences, a voting system may be able to choose a winner that better reflects the preferences of the voters.

One such ranked choice voting system is the instant runoff system. In an instant runoff election, voters can rank as many candidates as they wish. If any candidate has a majority (more than 50%) of the first preference votes, that candidate is declared the winner of the election.

If no candidate has more than 50% of the vote, then an “instant runoff” occurrs. The candidate who received the fewest number of votes is eliminated from the election, and anyone who originally chose that candidate as their first preference now has their second preference considered. Why do it this way? Effectively, this simulates what would have happened if the least popular candidate had not been in the election to begin with.

The process repeats: if no candidate has a majority of the votes, the last place candidate is eliminated, and anyone who voted for them will instead vote for their next preference (who hasn’t themselves already been eliminated). Once a candidate has a majority, that candidate is declared the winner.

Sounds a bit more complicated than a plurality vote, doesn’t it? But it arguably has the benefit of being an election system where the winner of the election more accurately represents the preferences of the voters. In a file called `runoff.c` in a folder called `runoff`, create a program to simulate a runoff election.

## Demo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-4rhSKgaZQsY93RLj0xgu7nwKB" src="https://asciinema.org/a/4rhSKgaZQsY93RLj0xgu7nwKB.js"></script>

## Distribution Code

### Download the distribution code

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $

Next execute

    wget https://cdn.cs50.net/2023/fall/psets/3/runoff.zip

in order to download a ZIP called `runoff.zip` into your codespace.

Then execute

    unzip runoff.zip

to create a folder called `runoff`. You no longer need the ZIP file, so you can execute

    rm runoff.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd runoff

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    runoff/ $

If all was successful, you should execute

    ls

and see a file named `runoff.c`. Executing `code runoff.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong!
