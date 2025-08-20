## Specification

Implement the functions in `helpers.c` such that a user can apply grayscale, reflection, blur, or edge detection filters to their images.

- The function `grayscale` should take an image and turn it into a black-and-white version of the same image.
- The `reflect` function should take an image and reflect it horizontally.
- The `blur` function should take an image and turn it into a box-blurred version of the same image.
- The `edges` function should take an image and highlight the edges between objects, according to the Sobel operator.

You should not modify any of the function signatures, nor should you modify any other files other than `helpers.c`.

## Understanding

Let’s now take a look at some of the files provided to you as distribution code to get an understanding for what’s inside of them.

### `bmp.h`

Open up `bmp.h` (as by double-clicking on it in the file browser) and have a look.

You’ll see definitions of the headers we’ve mentioned (`BITMAPINFOHEADER` and `BITMAPFILEHEADER`). In addition, that file defines `BYTE`, `DWORD`, `LONG`, and `WORD`, data types normally found in the world of Windows programming. Notice how they’re just aliases for primitives with which you are (hopefully) already familiar. It appears that `BITMAPFILEHEADER` and `BITMAPINFOHEADER` make use of these types.

Perhaps most importantly for you, this file also defines a `struct` called `RGBTRIPLE` that, quite simply, “encapsulates” three bytes: one blue, one green, and one red (the order, recall, in which we expect to find RGB triples actually on disk).

Why are these `struct`s useful? Well, recall that a file is just a sequence of bytes (or, ultimately, bits) on disk. But those bytes are generally ordered in such a way that the first few represent something, the next few represent something else, and so on. “File formats” exist because the world has standardized what bytes mean what. Now, we could just read a file from disk into RAM as one big array of bytes. And we could just remember that the byte at `array[i]` represents one thing, while the byte at `array[j]` represents another. But why not give some of those bytes names so that we can retrieve them from memory more easily? That’s precisely what the structs in `bmp.h` allow us to do. Rather than think of some file as one long sequence of bytes, we can instead think of it as a sequence of `struct`s.

### `filter.c`

Now, let’s open up `filter.c`. This file has been written already for you, but there are a couple important points worth noting here.

First, notice the definition of `filters` on line 10. That string tells the program what the allowable command-line arguments to the program are: `b`, `e`, `g`, and `r`. Each of them specifies a different filter that we might apply to our images: blur, edge detection, grayscale, and reflection.

The next several lines open up an image file, make sure it’s indeed a BMP file, and read all of the pixel information into a 2D array called `image`.

Scroll down to the `switch` statement that begins on line 101. Notice that, depending on what `filter` we’ve chosen, a different function is called: if the user chooses filter `b`, the program calls the `blur` function; if `e`, then `edges` is called; if `g`, then `grayscale` is called; and if `r`, then `reflect` is called. Notice, too, that each of these functions take as arguments the height of the image, the width of the image, and the 2D array of pixels.

These are the functions you’ll (soon!) implement. As you might imagine, the goal is for each of these functions to edit the 2D array of pixels in such a way that the desired filter is applied to the image.

The remaining lines of the program take the resulting `image` and write them out to a new image file.

### `helpers.h`

Next, take a look at `helpers.h`. This file is quite short, and just provides the function prototypes for the functions you saw earlier.

Here, take note of the fact that each function takes a 2D array called `image` as an argument, where `image` is an array of `height` many rows, and each row is itself another array of `width` many `RGBTRIPLE`s. So if `image` represents the whole picture, then `image[0]` represents the first row, and `image[0][0]` represents the pixel in the upper-left corner of the image.

### `helpers.c`

Now, open up `helpers.c`. Here’s where the implementation of the functions declared in `helpers.h` belong. But note that, right now, the implementations are missing! This part is up to you.

### `Makefile`

Finally, let’s look at `Makefile`. This file specifies what should happen when we run a terminal command like `make filter`. Whereas programs you may have written before were confined to just one file, `filter` seems to use multiple files: `filter.c` and `helpers.c`. So we’ll need to tell `make` how to compile this file.

Try compiling `filter` for yourself by going to your terminal and running

    $ make filter

Then, you can run the program by running:

    $ ./filter -g images/yard.bmp out.bmp

which takes the image at `images/yard.bmp`, and generates a new image called `out.bmp` after running the pixels through the `grayscale` function. `grayscale` doesn’t do anything just yet, though, so the output image should look the same as the original yard.

## Hints

- The values of a pixel’s `rgbtRed`, `rgbtGreen`, and `rgbtBlue` components are all integers, so be sure to round any floating-point numbers to the nearest integer when assigning them to a pixel value!

## Walkthrough

**Please note that there are 5 videos in this playlist.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/vsOsctDernw?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T382OwvMbZuaMGtD9wZkhnhYj"></iframe></div>

## How to Test

Be sure to test all of your filters on the sample bitmap files provided!

### Correctness

    check50 cs50/problems/2024/x/filter/more

### Style

    style50 helpers.c

## How to Submit

    submit50 cs50/problems/2024/x/filter/more
