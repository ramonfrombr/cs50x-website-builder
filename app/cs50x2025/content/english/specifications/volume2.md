### Copy WAV header from input file to output file

Your first TODO is to copy the WAV file header from `input` and write it to `output`. First, though, you’ll need to learn about a few special data types.

So far, we’ve seen a number of different types in C, including `int`, `bool`, `char`, `double`, `float`, and `long`. However, inside a header file called `stdint.h` are the declarations of a number of _other_ types that allow us to very precisely define the size (in bits) and sign (signed or unsigned) of an integer. Two types in particular will be useful to us when working with WAV files:

- `uint8_t` is a type that stores an 8-bit (hence `8`!) unsigned (i.e., not negative) integer (hence `uint`!). We can treat each byte of a WAV file’s header as a `uint8_t` value.
- `int16_t` is a type that stores a 16-bit signed (i.e., positive or negative) integer. We can treat each sample of audio in a WAV file as an `int16_t` value.

You’ll likely want to create an array of bytes to store the data from the WAV file header that you’ll read from the input file. Using the `uint8_t` type to represent a byte, you can create an array of `n` bytes for your header with syntax like

    uint8_t header[n];

replacing `n` with the number of bytes. You can then use `header` as an argument to [`fread`](https://manual.cs50.io/3/fread) or [`fwrite`](https://manual.cs50.io/3/fwrite) to read into or write from the header.

Recall that a WAV file’s header is always exactly 44 bytes long. Note that `volume.c` already defines a variable for you called `HEADER_SIZE`, equal to the number of bytes in the header.

The below is a pretty big hint, but here’s how you could accomplish this TODO!

    // Copy header from input file to output file
    uint8_t header[HEADER_SIZE];
    fread(header, HEADER_SIZE, 1, input);
    fwrite(header, HEADER_SIZE, 1, output);

### Write updated data to output file

Your next TODO is to read samples from `input`, update those samples, and write the updated samples to `output`. When reading files, it’s common to create a “buffer” in which to temporarily store data. There, you can modify the data and—once it’s ready—write the buffer’s data to a new file.

Recall that we can use the `int16_t` type to represent a sample of a WAV file. To store an audio sample, then, you can create a buffer variable with syntax like:

    // Create a buffer for a single sample
    int16_t buffer;

With a buffer for samples in place, you can now read data into it, one sample at a time. Try using `fread` for this task! You can use `&buffer`, the address of `buffer`, as an argument to `fread` or `fwrite` to read into or write from the buffer. (Recall that the `&` operator is used to get the address of the variable.)

    // Create a buffer for a single sample
    int16_t buffer;

    // Read single sample into buffer
    fread(&buffer, sizeof(int16_t), 1, input)

Now, to increase (or decrease) the volume of a sample, you need only multiply it by some factor.

    // Create a buffer for a single sample
    int16_t buffer;

    // Read single sample into buffer
    fread(&buffer, sizeof(int16_t), 1, input)

    // Update volume of sample
    buffer *= factor;

And finally, you can write that updated sample to `output`:

    // Create a buffer for a single sample
    int16_t buffer;

    // Read single sample from input into buffer
    fread(&buffer, sizeof(int16_t), 1, input)

    // Update volume of sample
    buffer *= factor;

    // Write updated sample to new file
    fwrite(&buffer, sizeof(int16_t), 1, output);

There’s just one problem: you’ll need to _continue_ reading a sample into your buffer, updating its volume, and writing the updated sample to the output file while there are still samples left to read.

- Thankfully, per its documentation, `fread` will return the number of items of data successfully read. You may find this useful to check for when you’ve reached the end of the file!
- Keep in mind there’s no reason you can’t call `fread` inside of a `while` loop’s conditional. You could, for example, make a call to `fread` like the following:

        while (fread(...))
        {

        }

It’s quite the hint, but see the below for an efficient way to solve this problem:

    // Create a buffer for a single sample
    int16_t buffer;

    // Read single sample from input into buffer while there are samples left to read
    while (fread(&buffer, sizeof(int16_t), 1, input) != 0)
    {
        // Update volume of sample
        buffer *= factor;

        // Write updated sample to new file
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

Because the version of C you’re using treats non-zero values as `true` and zero values as `false`, you could simplify the above syntax to the following:

    // Create a buffer for a single sample
    int16_t buffer;

    // Read single sample from input into buffer while there are samples left to read
    while (fread(&buffer, sizeof(int16_t), 1, input))
    {
        // Update volume of sample
        buffer *= factor;

        // Write updated sample to new file
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }
