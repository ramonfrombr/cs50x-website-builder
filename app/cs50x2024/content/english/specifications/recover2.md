### Convert the pseudocode to code

First, consider how to accept a single command-line argument. If the user misuses the program, you should tell them the program’s proper usage.

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Accept a single command-line argument
        if (argc != 2)
        {
            printf("Usage: ./recover FILE\n");
            return 1;
        }

        // Open the memory card

        // While there's still data left to read from the memory card

            // Create JPEGs from the data
    }

Now that you’ve checked for proper usage, you can open the memory card. Keep in mind that you can open `card.raw` programmatically with `fopen`, as with the below.

    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Accept a single command-line argument
        if (argc != 2)
        {
            printf("Usage: ./recover FILE\n");
            return 1;
        }

        // Open the memory card
        FILE *card = fopen(argv[1], "r");

        // While there's still data left to read from the memory card

            // Create JPEGs from the data
    }

You should, of course, check to be sure the file was opened properly! If it wasn’t, tell the user and exit the program: we’ll leave this part up to you.

Next, your program should read the data from the card you’ve opened, until there is no longer any data to read. Along the way, your program should recover every one of the JPEGs from `card.raw`, storing each as a separate file in your current working directory.

First consider how to read `card.raw` all the way through. Recall that, to read data from a file, you need to temporarily store that data in a “buffer.” And recall further that `card.raw` stores data in blocks of 512 bytes. As such, you’ll likely want to create a buffer of 512 bytes to store blocks of data as you read them sequentially. One way of doing so is to use the `uint8_t` type from `stdint.h`, which stores exactly 8 bits (1 byte). The type is called `uint8_t` since it stores an unsigned/positive/non-negative integer that requires 8 bits of space (i.e., one byte).

    #include <stdint.h>
    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Accept a single command-line argument
        if (argc != 2)
        {
            printf("Usage: ./recover FILE\n");
            return 1;
        }

        // Open the memory card
        FILE *card = fopen(argv[1], "r");

        // Create a buffer for a block of data
        uint8_t buffer[512];

        // While there's still data left to read from the memory card

            // Create JPEGs from the data
    }

It’s probably _not_ the best idea, though, to use 512 as a [“magic number”](../../../shorts/magic_numbers/) here. Odds are you could improve this design further!

Now, consider how to read data from the memory card. Per its [manual page](https://man.cs50.io/3/fread), `fread` returns the number of bytes that it has read, in which case it should either return `512` or `0`, given that `card.raw` contains some number of 512-byte blocks. In order to read every block from `card.raw`, after opening it with `fopen`, it should suffice to use a loop like this.

    #include <stdint.h>
    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char *argv[])
    {
        // Accept a single command-line argument
        if (argc != 2)
        {
            printf("Usage: ./recover FILE\n");
            return 1;
        }

        // Open the memory card
        FILE *card = fopen(argv[1], "r");

        // Create a buffer for a block of data
        uint8_t buffer[512];

        // While there's still data left to read from the memory card
        while (fread(buffer, 1, 512, card) == 512)
        {
            // Create JPEGs from the data

        }
    }

That way, as soon as `fread` returns `0` (which is effectively `false`), your loop will end.

Finally, it’s up to you to determine how to programmatically create JPEGs as you continue to read from `card.raw`. For this, you might find the below [walkthrough](#walkthrough) of use to you.

Keep in mind your program should number the files it outputs by naming each `###.jpg`, where `###` is three-digit decimal number from `000` on up. Befriend [`sprintf`](https://man.cs50.io/3/sprintf) and note that `sprintf` stores a formatted string at a location in memory. Given the prescribed `###.jpg` format for a JPEG’s filename, how many bytes should you allocate for that string? (Don’t forget the NUL character!)

To check whether the JPEGs your program spit out are correct, simply double-click and take a look! If each photo appears intact, your operation was likely a success!

And of course, remember to `fclose` every file you’ve opened with `fopen`!

### Keep your working directory clean

Odds are the JPEGs that the first draft of your code spits out won’t be correct. (If you open them up and don’t see anything, they’re probably not correct!) Execute the command below to delete all JPEGs in your current working directory.

    rm *.jpg

If you’d rather not be prompted to confirm each deletion, execute the command below instead.

    rm -f *.jpg

Just be careful with that `-f` switch, as it “forces” deletion without prompting you.

## Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/ooL0r_8N9ms?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## How to Test

### Running the Program

    ./recover card.raw

### Correctness

    check50 cs50/problems/2024/x/recover

### Style

    style50 recover.c

## How to Submit

    submit50 cs50/problems/2024/x/recover
