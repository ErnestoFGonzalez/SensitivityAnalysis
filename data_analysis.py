# Author: Ernesto González
# Date: 29/12/2019

import numpy as np
import pandas as pd
import pylab


with open('dados.dat', 'r') as infile:
    readlines = infile.readlines()

    for line in readlines:
        print(line)
