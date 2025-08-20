## Hints

- You may find Python’s [`csv`](https://docs.python.org/3/library/csv.html) module helpful for reading CSV files into memory. Of particular help might be [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader).

  - For instance, if a file like `foo.csv` has a header row, wherein each string is the name of some field, here’s how you might print those `fieldnames` as a `list`:
    import csv

          with open("foo.csv") as file:
              reader = csv.DictReader(file)
              print(reader.fieldnames)

  - And here’s how you read all of the (other) rows from a CSV into a `list`, wherein each element is a `dict` that represents that row:
    import csv

          rows = []
          with open("foo.csv") as file:
              reader = csv.DictReader(file)
              for row in reader:
                  rows.append(row)

- The [`open`](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) and [`read`](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) functions might also prove useful for reading text files into memory.
- Consider what data structures might be helpful for keeping tracking of information in your program. A [`list`](https://docs.python.org/3/tutorial/introduction.html#lists) or a [`dict`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) may prove useful.
- Remember we’ve defined a function (`longest_match`) that, given both a DNA sequence and an STR as inputs, returns the maximum number of times that the STR repeats. You can then use that function in other parts of your program!

## Walkthrough

<div class="ratio ratio-16x9" data-video=""><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="border" data-video="" src="https://www.youtube.com/embed/j84b_EgntcQ?modestbranding=0&amp;rel=0&amp;showinfo=0"></iframe></div>

## How to Test

While `check50` is available for this problem, you’re encouraged to first test your code on your own for each of the following.

- Run your program as `python dna.py databases/small.csv sequences/1.txt`. Your program should output `Bob`.
- Run your program as `python dna.py databases/small.csv sequences/2.txt`. Your program should output `No match`.
- Run your program as `python dna.py databases/small.csv sequences/3.txt`. Your program should output `No match`.
- Run your program as `python dna.py databases/small.csv sequences/4.txt`. Your program should output `Alice`.
- Run your program as `python dna.py databases/large.csv sequences/5.txt`. Your program should output `Lavender`.
- Run your program as `python dna.py databases/large.csv sequences/6.txt`. Your program should output `Luna`.
- Run your program as `python dna.py databases/large.csv sequences/7.txt`. Your program should output `Ron`.
- Run your program as `python dna.py databases/large.csv sequences/8.txt`. Your program should output `Ginny`.
- Run your program as `python dna.py databases/large.csv sequences/9.txt`. Your program should output `Draco`.
- Run your program as `python dna.py databases/large.csv sequences/10.txt`. Your program should output `Albus`.
- Run your program as `python dna.py databases/large.csv sequences/11.txt`. Your program should output `Hermione`.
- Run your program as `python dna.py databases/large.csv sequences/12.txt`. Your program should output `Lily`.
- Run your program as `python dna.py databases/large.csv sequences/13.txt`. Your program should output `No match`.
- Run your program as `python dna.py databases/large.csv sequences/14.txt`. Your program should output `Severus`.
- Run your program as `python dna.py databases/large.csv sequences/15.txt`. Your program should output `Sirius`.
- Run your program as `python dna.py databases/large.csv sequences/16.txt`. Your program should output `No match`.
- Run your program as `python dna.py databases/large.csv sequences/17.txt`. Your program should output `Harry`.
- Run your program as `python dna.py databases/large.csv sequences/18.txt`. Your program should output `No match`.
- Run your program as `python dna.py databases/large.csv sequences/19.txt`. Your program should output `Fred`.
- Run your program as `python dna.py databases/large.csv sequences/20.txt`. Your program should output `No match`.

### Correctness

    check50 cs50/problems/2024/x/dna

### Style

    style50 dna.py

## How to Submit

    submit50 cs50/problems/2024/x/dna
