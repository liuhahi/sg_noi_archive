import time

def fun9(k):
    if k == 1:
        return 8
    elif k == 2:
        return 79
    elif k == 3:
        return 710
    elif k > 3:
        return (fun9(k-1)-fun9(k-2))* 10 + fun9(k-3)
    return 0

def main():
    filename = 'input/4.1.in'
    with open(filename) as f:
        mylist = f.read().splitlines()
        N = int(mylist[0])
        arr = mylist[1:20]
        print('n is', N)
        start = time.perf_counter()
        for x in range(N):
            T, num = list(arr[x].split())
            n = fun9(len(num))
            print(n)
                # print(dp(p, d))
        print(time.perf_counter() - start)

if __name__ == "__main__":
    main()