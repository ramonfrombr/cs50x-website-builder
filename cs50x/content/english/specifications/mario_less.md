# Mario

## Getting Started

Open [VS Code](https://code.cs50.io/).

Start by clicking inside your terminal window, then execute `cd` by itself. You should find that its “prompt” resembles the below.

    $

Click inside of that terminal window and then execute

    wget https://cdn.cs50.net/2022/fall/psets/1/mario-less.zip

followed by Enter in order to download a ZIP called `mario-less.zip` in your codespace. Take care not to overlook the space between `wget` and the following URL, or any other character for that matter!

Now execute

    unzip mario-less.zip

to create a folder called `mario-less`. You no longer need the ZIP file, so you can execute

    rm mario-less.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd mario-less

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    mario-less/ $

If all was successful, you should execute

    ls

and see a file named `mario.c`. Executing `code mario.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong!

## World 1-1

Toward the end of World 1-1 in Nintendo’s Super Mario Brothers, Mario must ascend right-aligned pyramid of blocks, a la the below.

![screenshot of Mario jumping up a right-aligned pyramid](https://cs50.harvard.edu/x/2023/psets/1/mario/less/pyramid.png)

Let’s recreate that pyramid in C, albeit in text, using hashes (`#`) for bricks, a la the below. Each hash is a bit taller than it is wide, so the pyramid itself will also be taller than it is wide.

           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

The program we’ll write will be called `mario`. And let’s allow the user to decide just how tall the pyramid should be by first prompting them for a positive integer between, say, 1 and 8, inclusive.

Here’s how the program might work if the user inputs `8` when prompted:

    $ ./mario
    Height: 8
           #
          ##
         ###
        ####
       #####
      ######
     #######
    ########

Here’s how the program might work if the user inputs `4` when prompted:

    $ ./mario
    Height: 4
       #
      ##
     ###
    ####

Here’s how the program might work if the user inputs `2` when prompted:

    $ ./mario
    Height: 2
     #
    ##

And here’s how the program might work if the user inputs `1` when prompted:

    $ ./mario
    Height: 1
    #

If the user doesn’t, in fact, input a positive integer between 1 and 8, inclusive, when prompted, the program should re-prompt the user until they cooperate:

    $ ./mario
    Height: -1
    Height: 0
    Height: 42
    Height: 50
    Height: 4
       #
      ##
     ###
    ####

How to begin? Let’s approach this problem one step at a time.

## Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/NAs4FIWkJ4s?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## Pseudocode

First, execute

    cd

to ensure you’re in your codespace’s default directory.

Then, execute

    cd mario-less

to change to your `mario-less` directory.

Then, execute

    code pseudocode.txt

to open the file called `pseudocode.txt` inside that directory.

Write in `pseudocode.txt` some pseudocode that implements this program, even if not (yet!) sure how to write it in code. There’s no one right way to write pseudocode, but short English sentences suffice. Recall how we wrote [pseudocode for finding someone in a phone book](https://docs.google.com/presentation/d/1X3AMSenwZGSE6WxGpzoALAfMg2hmh1LYIJp3N2a1EYI/edit#slide=id.g41907da2bc_0_265). Odds are your pseudocode will use (or imply using!) one or more functions, conditionals, Boolean expressions, loops, and/or variables.

<details><summary>Spoiler</summary><p>There’s more than one way to do this, so here’s just one!</p>

<ol>
  <li>Prompt user for height</li>
  <li>If height is less than 1 or greater than 8 (or not an integer at all), go back one step</li>
  <li>Iterate from 1 through height:
    <ol>
      <li>On iteration <em>i</em>, print <em>i</em> hashes and then a newline</li>
    </ol>
  </li>
</ol>

<p>It’s okay to edit your own after seeing this pseudocode here, but don’t simply copy/paste ours into your own!</p></details>

## Prompting for Input

Whatever your pseudocode, let’s first write only the C code that prompts (and re-prompts, as needed) the user for input. Open the file called `mario.c` inside of your `mario` directory. (Remember how?)

Now, modify `mario.c` in such a way that it prompts the user for the pyramid’s height, storing their input in a variable, re-prompting the user again and again as needed if their input is not a positive integer between 1 and 8, inclusive. Then, simply print the value of that variable, thereby confirming (for yourself) that you’ve indeed stored the user’s input successfully, a la the below.

    $ ./mario
    Height: -1
    Height: 0
    Height: 42
    Height: 50
    Height: 4
    Stored: 4

<details><summary>Hints</summary><ul>
  <li data-marker="*">Recall that you can compile your program with <code class="language-plaintext highlighter-rouge">make</code>.</li>
  <li data-marker="*">Recall that you can print an <code class="language-plaintext highlighter-rouge">int</code> with <code class="language-plaintext highlighter-rouge">printf</code> using <code class="language-plaintext highlighter-rouge">%i</code>.</li>
  <li data-marker="*">Recall that you can get an integer from the user with <code class="language-plaintext highlighter-rouge">get_int</code>.</li>
  <li data-marker="*">Recall that <code class="language-plaintext highlighter-rouge">get_int</code> is declared in <code class="language-plaintext highlighter-rouge">cs50.h</code>.</li>
  <li data-marker="*">Recall that we prompted the user for a positive integer in lecture using a <code class="language-plaintext highlighter-rouge">do while</code> loop in <a href="https://cdn.cs50.net/2022/fall/lectures/1/src1/mario8.c?highlight"><code class="language-plaintext highlighter-rouge">mario.c</code></a>.</li>
</ul></details>

## Building the Opposite

Now that your program is (hopefully!) accepting input as prescribed, it’s time for another step.

It turns out it’s a bit easier to build a left-aligned pyramid than right-, a la the below.

    #
    ##
    ###
    ####
    #####
    ######
    #######
    ########

So let’s build a left-aligned pyramid first and then, once that’s working, right-align it instead!

Modify `mario.c` at right such that it no longer simply prints the user’s input but instead prints a left-aligned pyramid of that height.

<details>
  <summary>Hints</summary>
  <ul>
    <li data-marker="*">Keep in mind that a hash is just a character like any other, so you can print it with <code class="language-plaintext highlighter-rouge">printf</code>.</li>
    <li data-marker="*">Just as Scratch has a <a href="https://docs.google.com/presentation/d/1mRIN6EDK92NJJlazpFfBNKhxrAQUUxJOJW0UH7knS0g/edit#slide=id.gee4e5a99f9_0_313"><code class="language-plaintext highlighter-rouge">repeat</code></a> block, so does C have a <a href="https://docs.google.com/presentation/d/1mRIN6EDK92NJJlazpFfBNKhxrAQUUxJOJW0UH7knS0g/edit#slide=id.gee4e5a99f9_0_313"><code class="language-plaintext highlighter-rouge">for</code></a> loop, via which you can iterate some number times. Perhaps on each iteration, <em>i</em>, you could print that many hashes?</li>
    <li data-marker="*">
      <p>You can actually “nest” loops, iterating with one variable (e.g., <code class="language-plaintext highlighter-rouge">i</code>) in the “outer” loop and another (e.g., <code class="language-plaintext highlighter-rouge">j</code>) in the “inner” loop. For instance, here’s how you might print a square of height and width <code class="language-plaintext highlighter-rouge">n</code>, below. Of course, it’s not a square that you want to print!</p>

      <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>  for (int i = 0; i &lt; n; i++)

      {
      for (int j = 0; j &lt; n; j++)
      {
      printf("#");
      }
      printf("\n");
      }
      </code></pre></div> </div>

</li>
  </ul>
</details>

## Right-Aligning with Dots

Let’s now right-align that pyramid by pushing its hashes to the right by prefixing them with dots (i.e., periods), a la the below.

    .......#
    ......##
    .....###
    ....####
    ...#####
    ..######
    .#######
    ########

Modify `mario.c` in such a way that it does exactly that!

<details><summary>Hint</summary><p>Notice how the number of dots needed on each line is the “opposite” of the number of that line’s hashes. For a pyramid of height 8, like the above, the first line has but 1 hash and thus 7 dots. The bottom line, meanwhile, has 8 hashes and thus 0 dots. Via what formula (or arithmetic, really) could you print that many dots?</p></details>

### How to Test Your Code

Does your code work as prescribed when you input

- `-1` (or other negative numbers)?
- `0`?
- `1` through `8`?
- `9` or other positive numbers?
- letters or words?
- no input at all, when you only hit Enter?

## Removing the Dots

All that remains now is a finishing flourish! Modify `mario.c` in such a way that it prints spaces instead of those dots!

### How to Test Your Code

Execute the below to evaluate the correctness of your code using `check50`. But be sure to compile and test it yourself as well!

    check50 cs50/problems/2023/x/mario/less

Execute the below to evaluate the style of your code using `style50`.

    style50 mario.c

<details><summary>Hint</summary><p>A space is just a press of your space bar, just as a period is just a press of its key! Just remember that <code class="language-plaintext highlighter-rouge">printf</code> requires that you surround both with double quotes!</p></details>

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2023/x/mario/less
