### Implement `blur`

There are a number of ways to create the effect of blurring or softening an image. For this problem, we’ll use the “box blur,” which works by taking each pixel and, for each color value, giving it a new value by averaging the color values of neighboring pixels.

- Consider the following grid of pixels, where we’ve numbered each pixel.
  ![a grid of pixels](grid.png)
- The new value of each pixel would be the average of the values of all of the pixels that are within 1 row and column of the original pixel (forming a 3x3 box). For example, each of the color values for pixel 6 would be obtained by averaging the original color values of pixels 1, 2, 3, 5, 6, 7, 9, 10, and 11 (note that pixel 6 itself is included in the average). Likewise, the color values for pixel 11 would be be obtained by averaging the color values of pixels 6, 7, 8, 10, 11, 12, 14, 15 and 16.
- For a pixel along the edge or corner, like pixel 15, we would still look for all pixels within 1 row and column: in this case, pixels 10, 11, 12, 14, 15, and 16.

When implementing the `blur` function, you might find that blurring one pixel ends up affecting the blur of another pixel. It might be best to create a copy of `image` by declaring a new, two-dimensional array with code like `RGBTRIPLE copy[height][width];`. Then copy `image` into `copy`, pixel by pixel, with nested `for` loops, like so:

    void blur(int height, int width, RGBTRIPLE image[height][width])
    {
        // Create a copy of image
        RGBTRIPLE copy[height][width];
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                copy[i][j] = image[i][j];
            }
        }
    }

Now, you can read pixels’ colors from `copy` but write (i.e., change) pixels’ colors in `image`!

## Walkthrough

**Please note that there are 5 videos in this playlist.**

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/K0v9byp9jd0?modestbranding=0&amp;rel=0&amp;showinfo=1&amp;list=PLhQjrBD2T3837jmUt0ep7Tpmnxdv9NVut"></iframe></div>

## How to Test

Be sure to test all of your filters on the sample bitmap files provided!

### Correctness

    check50 cs50/problems/2024/x/filter/less

### Style

    style50 helpers.c

## How to Submit

    submit50 cs50/problems/2024/x/filter/less
