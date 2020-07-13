# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    travelled = 0
    for i,stop in enumerate(stops):
       print(i,stop)
        

if __name__ == '__main__':
    # to stop entering multi line input, press (ctrl + d)
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
