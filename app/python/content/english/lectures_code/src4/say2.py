# Demonstrates own module

import sys

from falas0 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
