#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = input("Number:")
    n = int(n)
    answer = n % 2
    if answer == 1:
        print("Weird")
    elif answer == 0:
        if 2 <= n <= 5:
          print("Not Weird") 
        elif 6 <= n <= 20:
           print("Weird") 
        elif 20 < n:
            print("Not Weird")           