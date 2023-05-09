#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    //If n is odd, print Weird
    if (n % 2) == 1:
        print("Weird")
    //If  is even and in the inclusive range of  to , print Not Weird
    elif ((n % 2) == 0) & (n >= 2) & (n <= 5):
        print("Not Weird") 
    //If  is even and in the inclusive range of  to , print Weird
    elif ((n % 2) == 0) & (n >= 6) & (n <= 20):
        print("Weird")
    //If  is even and greater than , print Not Weird    
    else:
        print("Not Weird")

        


