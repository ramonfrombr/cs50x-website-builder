# Volume

![WAV file waveform](https://cs50.harvard.edu/x/2024/psets/4/volume/wav_file.png)

## Problem to Solve

[WAV files](https://docs.fileformat.com/audio/wav/) are a common file format for representing audio. WAV files store audio as a sequence of “samples”: numbers that represent the value of some audio signal at a particular point in time. WAV files begin with a 44-byte “header” that contains information about the file itself, including the size of the file, the number of samples per second, and the size of each sample. After the header, the WAV file contains a sequence of samples, each a single 2-byte (16-bit) integer representing the audio signal at a particular point in time.

Scaling each sample value by a given factor has the effect of changing the volume of the audio. Multiplying each sample value by 2.0, for example, will have the effect of doubling the volume of the origin audio. Multiplying each sample by 0.5, meanwhile, will have the effect of cutting the volume in half.

In a file called `volume.c` in a folder called `volume`, write a program to modify the volume of an audio file.

## Demo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-mc2hPhYDt1spoMjlqNMuqC4Uc" src="https://asciinema.org/a/mc2hPhYDt1spoMjlqNMuqC4Uc.js"></script>

## Distribution Code

For this problem, you’ll extend the functionality of code provided to you by CS50’s staff.

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $

Next execute

    wget https://cdn.cs50.net/2023/fall/psets/4/volume.zip

in order to download a ZIP called `volume.zip` into your codespace.

Then execute

    unzip volume.zip

to create a folder called `volume`. You no longer need the ZIP file, so you can execute

    rm volume.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd volume

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    volume/ $

If all was successful, you should execute

    ls

and see a file named `volume.c`. Executing `code volume.c` should open the file where you will type your code for this problem set. If not, retrace your steps and see if you can determine where you went wrong!

## Implementation Details

Complete the implementation of `volume.c`, such that it changes the volume of a sound file by a given factor.

- The program should accept three command-line arguments. The first is `input`, which represents the name of the original audio file. The second is `output`, which represents the name of the new audio file that should be generated. The third is `factor`, which is the amount by which the volume of the original audio file should be scaled.
  - For example, if `factor` is `2.0`, then your program should double the volume of the audio file in `input` and save the newly generated audio file in `output`.
- Your program should first read the header from the input file and write the header to the output file.
- Your program should then read the rest of the data from the WAV file, one 16-bit (2-byte) sample at a time. Your program should multiply each sample by the `factor` and write the new sample to the output file.
  - You may assume that the WAV file will use 16-bit signed values as samples. In practice, WAV files can have varying numbers of bits per sample, but we’ll assume 16-bit samples for this problem.
- Your program, if it uses `malloc`, must not leak any memory.

## Hints

### Understand the code in `volume.c`

Notice first that `volume.c` is already set up to take three command-line arguments, `input`, `output`, and `factor`.

- `main` takes both an `int`, `argc`, and an array of `char *`s (strings!), `argv`.
- If `argc`, the number of arguments at the command-line including the program itself, is not equal to 4, the program will print its proper usage and exit with status code 1.

        int main(int argc, char \*argv[])
        {
            // Check command-line arguments
            if (argc != 4)
            {
                printf("Usage: ./volume input.wav output.wav factor\n");
                return 1;
            }

            // ...
        }

Next, `volume.c` uses [`fopen`](https://manual.cs50.io/3/fopen) to open the two files provided as command-line arguments.

- It’s best practice to check if the result of calling `fopen` is `NULL`. If it is, the file wasn’t found or wasn’t able to be opened.

        // Open files and determine scaling factor
        FILE *input = fopen(argv[1], "r");
        if (input == NULL)
        {
            printf("Could not open file.\n");
            return 1;
        }

        FILE *output = fopen(argv[2], "w");
        if (output == NULL)
        {
            printf("Could not open file.\n");
            return 1;
        }

Later, these files are closed with `fclose`. Whenever you call `fopen`, you should later call `fclose`!

        // Close files
        fclose(input);
        fclose(output);

Before closing the files, though, notice that we have a few TODOs.

        // TODO: Copy header from input file to output file

        // TODO: Read samples from input file and write updated data to output file

Odds are you’ll need to know the factor by which to scale the volume, hence why `volume.c` already converts the third command-line argument to a `float` for you!

        float factor = atof(argv[3]);
