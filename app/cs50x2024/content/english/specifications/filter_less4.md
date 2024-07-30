### Implement `sepia`

Most image editing programs support a “sepia” filter, which gives images an old-timey feel by making the whole image look a bit reddish-brown.

- An image can be converted to sepia by taking each pixel, and computing new red, green, and blue values based on the original values of the three.
- There are a number of algorithms for converting an image to sepia, but for this problem, we’ll ask you to use the following algorithm. For each pixel, the sepia color values should be calculated based on the original color values per the below.
  sepiaRed = .393 _ originalRed + .769 _ originalGreen + .189 _ originalBlue
  sepiaGreen = .349 _ originalRed + .686 _ originalGreen + .168 _ originalBlue
  sepiaBlue = .272 _ originalRed + .534 _ originalGreen + .131 \* originalBlue

- Of course, the result of each of these formulas may not be an integer, but each value could be rounded to the nearest integer. It’s also possible that the result of the formula is a number greater than 255, the maximum value for an 8-bit color value. In that case, the red, green, and blue values should be capped at 255. As a result, we can guarantee that the resulting red, green, and blue values will be whole numbers between 0 and 255, inclusive.

Write some pseudocode to help you solve this problem and recall the use of nested `for` loops to visit every pixel.

    void sepia(int height, int width, RGBTRIPLE image[height][width])
    {
        // Loop over all pixels
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                // Compute sepia values

                // Update pixel with sepia values
            }
        }
    }

To compute the `sepia` values, revisit the above bullets. You have a formula to compute the sepia values, but there are still a few catches. In particular, you’ll need to…

- Round the result of each computation to the nearest integer
- Ensure the resulting value is no larger than 255

How might a function that returns the lesser of two integers come in handy while implementing `sepia`, particularly when you need to make sure a color’s value is no higher than 255? You’re welcome, but not required, to write a helper function of your own to do just that!

### Implement `reflect`

Some filters might also move pixels around. Reflecting an image, for example, is a filter where the resulting image is what you would get by placing the original image in front of a mirror.

- Any pixels on the left side of the image should end up on the right, and vice versa.
- Note that all of the original pixels of the original image will still be present in the reflected image, it’s just that those pixels may have been rearranged to be in a different place in the image.

In the `reflect` function, then, you’ll need to swap the values of pixels on opposite sides of a row. Write some pseudocode to help you get started:

    void reflect(int height, int width, RGBTRIPLE image[height][width])
    {
        // Loop over all pixels
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                // Swap pixels
            }
        }
    }

Recall from lecture how we implemented swapping two values with a temporary variable. No need to use a separate function for swapping unless you would like to!

And now’s a good time to think about your nested `for` loops. The outer `for` loop iterates over every row, while the inner `for` loop iterates over every pixel in that row. To successfully reflect a row, though, need you iterate over every pixel in it?
