# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    fraction = [float(v)/ float(w) for v,w in zip(values, weights)]
    for i in range(n+1):
        if capacity == 0:
            return value
            break
        max_weight = max(fraction)
        index = fraction.index(max_weight)
        fraction[index] = -1
        add_capacity = min(capacity, weights[index])
        value += add_capacity * max_weight
        capacity -= add_capacity
        weights[index] -= add_capacity
    return value
        
    

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
