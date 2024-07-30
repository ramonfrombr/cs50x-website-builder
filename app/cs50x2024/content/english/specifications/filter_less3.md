### `helpers.c`

Now, open up `helpers.c`. Here’s where the implementation of the functions declared in `helpers.h` belong. But note that, right now, the implementations are missing! This part is up to you.

### `Makefile`

Finally, let’s look at `Makefile`. This file specifies what should happen when we run a terminal command like `make filter`. Whereas programs you may have written before were confined to just one file, `filter` seems to use multiple files: `filter.c` and `helpers.c`. So we’ll need to tell `make` how to compile this file.

Try compiling `filter` for yourself by going to your terminal and running

    $ make filter

Then, you can run the program by running:

    $ ./filter -g images/yard.bmp out.bmp

which takes the image at `images/yard.bmp`, and generates a new image called `out.bmp` after running the pixels through the `grayscale` function. `grayscale` doesn’t do anything just yet, though, so the output image should look the same as the original yard.

## Specification

Implement the functions in `helpers.c` such that a user can apply grayscale, sepia, reflection, or blur filters to their images.

- The function `grayscale` should take an image and turn it into a black-and-white version of the same image.
- The function `sepia` should take an image and turn it into a sepia version of the same image.
- The `reflect` function should take an image and reflect it horizontally.
- Finally, the `blur` function should take an image and turn it into a box-blurred version of the same image.

You should not modify any of the function signatures, nor should you modify any other files other than `helpers.c`.

## Hints

### Implement `grayscale`

One common filter is the “grayscale” filter, where we take an image and want to convert it to black-and-white. How does that work?

- Recall that if the red, green, and blue values are all set to `0x00` (hexadecimal for `0`), then the pixel is black. And if all values are set to `0xff` (hexadecimal for `255`), then the pixel is white. So long as the red, green, and blue values are all equal, the result will be varying shades of gray along the black-white spectrum, with higher values meaning lighter shades (closer to white) and lower values meaning darker shades (closer to black).
- So to convert a pixel to grayscale, you just need to make sure the red, green, and blue values are all the same value. But how do you know what value to make them? Well, it’s probably reasonable to expect that if the original red, green, and blue values were all pretty high, then the new value should also be pretty high. And if the original values were all low, then the new value should also be low.
- In fact, to ensure each pixel of the new image still has the same general brightness or darkness as the old image, you can take the **average** of the red, green, and blue values to determine what shade of grey to make the new pixel.

If you apply the above algorithm to each pixel in the image, the result will be an image converted to grayscale. Write some pseudocode to help you solve this problem.

    void grayscale(int height, int width, RGBTRIPLE image[height][width])
    {
        // Loop over all pixels

            // Take average of red, green, and blue

            // Update pixel values
    }

First, how might you loop over all pixels? Recall that the image’s pixels are stored in the two-dimensional array, `image`. To iterate over a two-dimensional array, you’ll need two loops, one nested inside the other.

    void grayscale(int height, int width, RGBTRIPLE image[height][width])
    {
        // Loop over all pixels
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                // Take average of red, green, and blue

                // Update pixel values
            }
        }
    }

Now, you can use `image[i][j]` to access any individual pixel of the image. But how to take the average of the red, green, and blue elements? Recall each element of `image` is an `RGBTRIPLE`, which is the `struct` defined in `bmp.h` to represent a pixel. The usual syntax to access members of a `struct` applies, wherein `image[i][j].rgbtRed` will give you access to the `RGBTRIPLE`’s red value, `image[i][j].rgbtGreen` will give you access to its green value, and so on.

When you compute the average, keep in mind the values of a pixel’s `rgbtRed`, `rgbtGreen`, and `rgbtBlue` components are all integers. So be sure to [round](https://manual.cs50.io/3/round) any floating-point numbers to the nearest integer when assigning them to a pixel value! And why might you want to divide the sum of these integers by 3.0 and not 3?

Once you’ve averaged the pixel’s red, green, and blue values into a resulting grayscale color, go ahead and update the pixel’s red, green, and blue values. By now, you’re already acquainted with the syntax for assignment!
