## Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/LiGhjz9ColQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

<details><summary>Not sure how to solve?</summary><div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/-rtZkTAK2gg?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div></details>

## How to Test

Your program should behave per the examples below.

    $ ./volume input.wav output.wav 2.0

When you listen to `output.wav` (as by control-clicking on `output.wav` in the file browser, choosing **Download**, and then opening the file in an audio player on your computer), it should be twice as loud as `input.wav`!

    $ ./volume input.wav output.wav 0.5

When you listen to `output.wav`, it should be half as loud as `input.wav`!

### Correctness

    check50 cs50/problems/2024/x/volume

### Style

    style50 volume.c

## How to Submit

    submit50 cs50/problems/2024/x/volume
