def main():
    n = int(input())
    arr = list(map(int,input().split()))
    print(solution (n,arr))


def solution(n, arr):
    resp = 0
    for x,iten in enumerate(arr):
        add = arr.count(iten-1)+arr.count(iten)
        if add >resp:
            resp = add
        add = arr.count(iten+1)+arr.count(iten)
        if add >resp:
            resp = add
    return resp

main()