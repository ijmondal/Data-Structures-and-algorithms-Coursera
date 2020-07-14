# python3
import sys


def compute_min_refills(distance, tank, n, stops):
    # write your code here
    stops.insert(0,0)
    stops.insert(n+1, distance)
    dist_diff = [0] * len(stops)
    refill =0
    actual_tank = tank
    for i in range(1, len(stops)):
        dist_diff[i] = stops[i] - stops[i-1]
    
    for i in range(0, len(dist_diff)-1):
       if dist_diff[i+1] <= tank and dist_diff[i+1] <= actual_tank:
           tank = tank - dist_diff[i+1]
       elif dist_diff[i+1] > actual_tank:
           return -1
       else:
           tank = actual_tank - dist_diff[i+1]
           refill +=1
           
           
           
    return refill       
        

if __name__ == '__main__':
    # to stop entering multi line input, press (ctrl + d)
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, n, stops))
