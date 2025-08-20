## Hints

### Complete the `vote` function

Next, complete the `vote` function.

- Consider that `vote`’s signature, `bool vote(string name)`, shows it takes a single argument, a `string` called `name`, representing the name of the candidate who was voted for.
- `vote` should return a `bool`, where `true` indicates a vote was successfully cast and `false` indicates it was not.

One way to approach this problem is to do the following:

1.  Iterate over each candidate
    1.  Check if candidate’s name matches the input, `name`
        1.  If yes, increment that candidate’s votes and return `true`
        2.  If no, continue checking
2.  If no matches after checking each candidate, return `false`

Let’s write some pseudocode to remind you to do just that:

    // Update vote totals given a new vote
    bool vote(string name)
    {
        // Iterate over each candidate
            // Check if candidate's name matches given name
                // If yes, increment candidate's votes and return true

        // If no match, return false
    }

We’ll leave the implementation in code, though, up to you!

### Complete the `print_winner` function

Finally, complete the `print_winner` function.

- The function should print out the name of the candidate who received the most votes in the election, and then print a newline.
- The election could end in a tie if multiple candidates each have the maximum number of votes. In that case, you should output the names of each of the winning candidates, each on a separate line.

You might think a sorting algorithm would best solve this problem: imagine sorting candidates by their vote totals and printing the top candidate (or candidates). Recall, though, that sorting can be expensive: even Merge Sort, one of the fastest sorting algorithms, runs in \\(O(N \\space log(N))\\).

Consider that you need only two pieces of information to solve this problem:

1.  The maximum number of votes
2.  The candidate (or candidates) with that number of votes

As such, a good solution might require only two searches. Write some pseudocode to remind yourself to do just that:

    // Print the winner (or winners) of the election
    void print_winner(void)
    {
        // Find the maximum number of votes

        // Print the candidate (or candidates) with maximum votes

    }

We’ll leave the code, though, up to you!

## Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ftOapzDjEb8?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## How to Test

Be sure to test your code to make sure it handles…

- An election with any number of candidate (up to the `MAX` of `9`)
- Voting for a candidate by name
- Invalid votes for candidates who are not on the ballot
- Printing the winner of the election if there is only one
- Printing the winner of the election if there are multiple winners

### Correctness

    check50 cs50/problems/2024/x/plurality

### Style

    style50 plurality.c

## How to Submit

    submit50 cs50/problems/2024/x/plurality
