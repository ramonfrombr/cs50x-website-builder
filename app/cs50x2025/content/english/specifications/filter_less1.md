# Filter

![Harvard Yard in grayscale](https://cs50.harvard.edu/x/2024/psets/4/filter/less/yard-grayscale.bmp)

## Problem to Solve

Perhaps the simplest way to represent an image is with a grid of pixels (i.e., dots), each of which can be of a different color. For black-and-white images, we thus need 1 bit per pixel, as 0 could represent black and 1 could represent white, as in the below.

![a simple bitmap](https://cs50.harvard.edu/x/2024/psets/4/filter/less/bitmap.png)

In this sense, then, is an image just a bitmap (i.e., a map of bits). For more colorful images, you simply need more bits per pixel. A file format (like [BMP](https://en.wikipedia.org/wiki/BMP_file_format), [JPEG](https://en.wikipedia.org/wiki/JPEG), or [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)) that supports “24-bit color” uses 24 bits per pixel. (BMP actually supports 1-, 4-, 8-, 16-, 24-, and 32-bit color.)

A 24-bit BMP uses 8 bits to signify the amount of red in a pixel’s color, 8 bits to signify the amount of green in a pixel’s color, and 8 bits to signify the amount of blue in a pixel’s color. If you’ve ever heard of RGB color, well, there you have it: red, green, blue.

If the R, G, and B values of some pixel in a BMP are, say, `0xff`, `0x00`, and `0x00` in hexadecimal, that pixel is purely red, as `0xff` (otherwise known as `255` in decimal) implies “a lot of red,” while `0x00` and `0x00` imply “no green” and “no blue,” respectively. In this problem, you’ll manipulate these R, G, and B values of individual pixels, ultimately creating your very own image filters.

In a file called `helpers.c` in a folder called `filter-less`, write a program to apply filters to BMPs.

## Demo

<script async="" data-autoplay="1" data-cols="100" data-loop="1" data-rows="12" id="asciicast-QnLel70SPmbW9nswXTb9Yu9ZD" src="https://asciinema.org/a/QnLel70SPmbW9nswXTb9Yu9ZD.js"></script>

## Distribution Code

For this problem, you’ll extend the functionality of code provided to you by CS50’s staff.

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $

Next execute

    wget https://cdn.cs50.net/2023/fall/psets/4/filter-less.zip

in order to download a ZIP called `filter-less.zip` into your codespace.

Then execute

    unzip filter-less.zip

to create a folder called `filter-less`. You no longer need the ZIP file, so you can execute

    rm filter-less.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd filter-less

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    filter-less/ $

Execute `ls` by itself, and you should see a few files: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c`, and `Makefile`. You should also see a folder, `images/`, with four BMP files. If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!
