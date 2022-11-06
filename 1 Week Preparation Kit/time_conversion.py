#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    string_array = s.rsplit(":");
    hour = string_array[0];
    if 'AM' in string_array[2]:
        if hour == '12':
            military = '00';
        else:
            military = str(hour);
    elif 'PM' in string_array[2]:
        if hour == '12':
            military = hour;
        else:
            military = str(int(hour) + 12);
    string_array[0] = military;
    no_am_pm = string_array[2].strip('APM');
    string_array[2] = no_am_pm;
    no_am_pm = ':'.join(string_array);
    return  no_am_pm

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
