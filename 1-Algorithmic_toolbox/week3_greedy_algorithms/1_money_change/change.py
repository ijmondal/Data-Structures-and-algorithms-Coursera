# Uses python3
import sys

def get_change(m):
    #write your code here
    coins =0
    if m >= 10:
        coins = m // 10
        m = m % 10
    if m >= 5 and m < 10:
        coins = coins +  (m // 5)
        m %= 5
    if m >0 and m <5:
        coins += m // 1
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
