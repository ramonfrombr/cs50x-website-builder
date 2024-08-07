# Filter

![Harvard Yard with edge detection](https://cs50.harvard.edu/x/2024/psets/4/filter/more/yard-edges.bmp)

## Problem to Solve

Perhaps the simplest way to represent an image is with a grid of pixels (i.e., dots), each of which can be of a different color. For black-and-white images, we thus need 1 bit per pixel, as 0 could represent black and 1 could represent white, as in the below.

![a simple bitmap](https://cs50.harvard.edu/x/2024/psets/4/filter/more/bitmap.png)

In this sense, then, is an image just a bitmap (i.e., a map of bits). For more colorful images, you simply need more bits per pixel. A file format (like [BMP](https://en.wikipedia.org/wiki/BMP_file_format), [JPEG](https://en.wikipedia.org/wiki/JPEG), or [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)) that supports “24-bit color” uses 24 bits per pixel. (BMP actually supports 1-, 4-, 8-, 16-, 24-, and 32-bit color.)

A 24-bit BMP uses 8 bits to signify the amount of red in a pixel’s color, 8 bits to signify the amount of green in a pixel’s color, and 8 bits to signify the amount of blue in a pixel’s color. If you’ve ever heard of RGB color, well, there you have it: red, green, blue.

If the R, G, and B values of some pixel in a BMP are, say, `0xff`, `0x00`, and `0x00` in hexadecimal, that pixel is purely red, as `0xff` (otherwise known as `255` in decimal) implies “a lot of red,” while `0x00` and `0x00` imply “no green” and “no blue,” respectively. In this problem, you’ll manipulate these R, G, and B values of individual pixels, ultimately creating your very own image filters.

In a file called `helpers.c` in a folder called `filter-more`, write a program to apply filters to BMPs.

## Demo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-DC5vtWOatmXC3Ff825YxHE0CZ" src="https://asciinema.org/a/DC5vtWOatmXC3Ff825YxHE0CZ.js"></script>

## Distribution Code

For this problem, you’ll extend the functionality of code provided to you by CS50’s staff.

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $

Next execute

    wget https://cdn.cs50.net/2023/fall/psets/4/filter-more.zip

in order to download a ZIP called `filter-more.zip` into your codespace.

Then execute

    unzip filter-more.zip

to create a folder called `filter-more`. You no longer need the ZIP file, so you can execute

    rm filter-more.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd filter-more

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    filter-more/ $

Execute `ls` by itself, and you should see a few files: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c`, and `Makefile`. You should also see a folder called `images` with four BMP files. If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

## Background

### A Bit(map) More Technical

Recall that a file is just a sequence of bits, arranged in some fashion. A 24-bit BMP file, then, is essentially just a sequence of bits, (almost) every 24 of which happen to represent some pixel’s color. But a BMP file also contains some “metadata,” information like an image’s height and width. That metadata is stored at the beginning of the file in the form of two data structures generally referred to as “headers,” not to be confused with C’s header files. (Incidentally, these headers have evolved over time. This problem uses the latest version of Microsoft’s BMP format, 4.0, which debuted with Windows 95.)

The first of these headers, called `BITMAPFILEHEADER`, is 14 bytes long. (Recall that 1 byte equals 8 bits.) The second of these headers, called `BITMAPINFOHEADER`, is 40 bytes long. Immediately following these headers is the actual bitmap: an array of bytes, triples of which represent a pixel’s color. However, BMP stores these triples backwards (i.e., as BGR), with 8 bits for blue, followed by 8 bits for green, followed by 8 bits for red. (Some BMPs also store the entire bitmap backwards, with an image’s top row at the end of the BMP file. But we’ve stored this problem set’s BMPs as described herein, with each bitmap’s top row first and bottom row last.) In other words, were we to convert the 1-bit smiley above to a 24-bit smiley, substituting red for black, a 24-bit BMP would store this bitmap as follows, where `0000ff` signifies red and `ffffff` signifies white; we’ve highlighted in red all instances of `0000ff`.

![red smile](https://cs50.harvard.edu/x/2024/psets/4/filter/more/red_smile.png)

Because we’ve presented these bits from left to right, top to bottom, in 8 columns, you can actually see the red smiley if you take a step back.

To be clear, recall that a hexadecimal digit represents 4 bits. Accordingly, `ffffff` in hexadecimal actually signifies `111111111111111111111111` in binary.

Notice that you could represent a bitmap as a 2-dimensional array of pixels: where the image is an array of rows, each row is an array of pixels. Indeed, that’s how we’ve chosen to represent bitmap images in this problem.
