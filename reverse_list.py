# Author: Samuel Bennett
# Date: 5/12/2021
# Description: Function named reverse_list takes a list of numbers and creates a reverse list of the values.

def reverse_list(randyjohnson):
    for i in range(len(randyjohnson)//2):
        randyjohnson[i], randyjohnson[len(randyjohnson)-i-1] = randyjohnson[len(randyjohnson)-i-1], randyjohnson[i]


val = [7, -3, 12, 9]
reverse_list(val)
print(val)
