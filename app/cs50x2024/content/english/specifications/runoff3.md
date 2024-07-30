### Complete the `tabulate` function

- The function should update the number of `votes` each candidate has at this stage in the runoff.
- Recall that at each stage in the runoff, every voter effectively votes for their top-preferred candidate who has not already been eliminated.

As you write your code, consider these hints:

- Recall that `voter_count` stores the number of voters in the election and that, for each voter in our election, we want to count one ballot.
- Recall that for a voter `i`, their top choice candidate is represented by `preferences[i][0]`, their second choice candidate by `preferences[i][1]`, etc.
- Recall that the `candidate` `struct` has a field called `eliminated`, which will be `true` if the candidate has been eliminated from the election.
- Recall that the `candidate` `struct` has a field called `votes`, which you’ll likely want to update for each voter’s preferred candidate.
- Recall that once you’ve cast a vote for a voter’s first non-eliminated candidate, you’ll want to stop there, not continue down their ballot. You can break out of a loop early using `break` inside of a conditional.

### Complete the `print_winner` function.

- If any candidate has more than half of the vote, their name should be printed and the function should return `true`.
- If nobody has won the election yet, the function should return `false`.

As you write your code, consider this hint:

- Recall that `voter_count` stores the number of voters in the election. Given that, how would you express the number of votes needed to win the election?

### Complete the `find_min` function

- The function should return the minimum vote total for any candidate who is still in the election.

As you write your code, consider this hint:

- You’ll likely want to loop through the candidates to find the one who is both still in the election and has the fewest number of votes. What information should you keep track of as you loop through the candidates?

### Complete the `is_tie` function

- The function takes an argument `min`, which will be the minimum number of votes that anyone in the election currently has.
- The function should return `true` if every candidate remaining in the election has the same number of votes, and should return `false` otherwise.

As you write your code, consider this hint:

- Recall that a tie happens if every candidate still in the election has the same number of votes. Note, too, that the `is_tie` function takes an argument `min`, which is the smallest number of votes any candidate currently has. How might you use `min` to determine if the election is a tie (or, conversely, not a tie)?

### Complete the `eliminate` function

- The function takes an argument `min`, which will be the minimum number of votes that anyone in the election currently has.
- The function should eliminate the candidate (or candidates) who have `min` number of votes.

## Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-Vc5aGywKxo?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## How to Test

Be sure to test your code to make sure it handles…

- An election with any number of candidate (up to the `MAX` of `9`)
- Voting for a candidate by name
- Invalid votes for candidates who are not on the ballot
- Printing the winner of the election if there is only one
- Not eliminating anyone in the case of a tie between all remaining candidates

### Correctness

    check50 cs50/problems/2024/x/runoff

### Style

    style50 runoff.c

## How to Submit

    submit50 cs50/problems/2024/x/runoff
