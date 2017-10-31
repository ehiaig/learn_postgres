#!/bin/python3

import sys

def productOfPages(a, b, c, d, p, q):
    x = [a,b,c,d]
    y = [p,q]

    for number in y:
        if number in x:
            x.remove(number)
    return int(x[0]) * int(x[1])

if __name__ == "__main__":
    # answer = productOfPages(20, 10, 40, 30, 10, 30 )
    answer = productOfPages(5, 5, 10, 10, 5, 10)
    print(answer)