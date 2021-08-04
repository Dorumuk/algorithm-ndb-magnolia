# number of city : 2 <= N <=300000
# number of load : 1 <= M <=1000000
# total length : 1 <= K <=300000
# start point(city) : 1 <= X <= N

n = 0
m = 0
k = 0
x = 0


def init():
    n, m, k, x = input().split()
    print(n, m, k, x)


def pointToPoint():
    a, b = input().split()
    # if (1 <= a and b <= n)
