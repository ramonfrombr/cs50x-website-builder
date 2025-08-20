# Tideman

## Problem to Solve

You already know about plurality elections, which follow a very simple algorithm for determining the winner of an election: every voter gets one vote, and the candidate with the most votes wins.

But the plurality vote does have some disadvantages. What happens, for instance, in an election with three candidates, and the ballots below are cast?

![Five ballots, tie betweeen Alice and Bob](https://cs50.harvard.edu/x/2024/psets/3/fptp_ballot_1.png)

A plurality vote would here declare a tie between Alice and Bob, since each has two votes. But is that the right outcome?

There’s another kind of voting system known as a ranked-choice voting system. In a ranked-choice system, voters can vote for more than one candidate. Instead of just voting for their top choice, they can rank the candidates in order of preference. The resulting ballots might therefore look like the below.

![Five ballots, with ranked preferences](https://cs50.harvard.edu/x/2024/psets/3/ranked_ballot_1.png)

Here, each voter, in addition to specifying their first preference candidate, has also indicated their second and third choices. And now, what was previously a tied election could now have a winner. The race was originally tied between Alice and Bob. But the voter who chose Charlie preferred Alice over Bob, so Alice could here be declared the winner.

Ranked choice voting can also solve yet another potential drawback of plurality voting. Take a look at the following ballots.

![Nine ballots, with ranked preferences](https://cs50.harvard.edu/x/2024/psets/3/condorcet_1.png)

Who should win this election? In a plurality vote where each voter chooses their first preference only, Charlie wins this election with four votes compared to only three for Bob and two for Alice. (Note that, if you’re familiar with the instant runoff voting system, Charlie wins here under that system as well). Alice, however, might reasonably make the argument that she should be the winner of the election instead of Charlie: after all, of the nine voters, a majority (five of them) preferred Alice over Charlie, so most people would be happier with Alice as the winner instead of Charlie.

Alice is, in this election, the so-called “Condorcet winner” of the election: the person who would have won any head-to-head matchup against another candidate. If the election had been just Alice and Bob, or just Alice and Charlie, Alice would have won.

The Tideman voting method (also known as “ranked pairs”) is a ranked-choice voting method that’s guaranteed to produce the Condorcet winner of the election if one exists. In a file called `tideman.c` in a folder called `tideman`, create a program to simulate an election by the Tideman voting method.

## Demo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-FWidrKAwqxtepXlN1T0l5hNnJ" src="https://asciinema.org/a/FWidrKAwqxtepXlN1T0l5hNnJ.js"></script>

## Distribution Code

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $

Next execute

    wget https://cdn.cs50.net/2023/fall/psets/3/tideman.zip

in order to download a ZIP called `tideman.zip` into your codespace.

Then execute

    unzip tideman.zip

to create a folder called `tideman`. You no longer need the ZIP file, so you can execute

    rm tideman.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd tideman

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    tideman/ $

If all was successful, you should execute

    ls

and see a file named `tideman.c`. Executing `code tideman.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong!
