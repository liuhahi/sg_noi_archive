import time
import sys

max_conventional_to_lucky = 0
max_lucky_to_conventional = 0
c_count = 0
l_count = 0

c_dict = {}
l_dict = {}

def isUnlucky(num):
    return "4" in str(num) or "13" in str(num)

def lucky_to_conventional(num):
    global max_lucky_to_conventional
    global l_count
    if isUnlucky(num):
        l_dict[str(num)] = -1
        return -1
    elif num < max_lucky_to_conventional:
        return l_dict[str(num)]
    else:
        for i in range(max_lucky_to_conventional, num + 1):
            if isUnlucky(i):
                l_count += 1
                l_dict[str(i)] = -1
            else:
                l_dict[str(i)] = i - l_count
        max_lucky_to_conventional = num + 1
        return l_dict[str(num)]

def conventional_to_lucky(num):
    global max_conventional_to_lucky
    global c_count

    if num < max_conventional_to_lucky:
        return c_dict[str(num)]
    else:
        for i in range(max_conventional_to_lucky, num + 1):
            if isUnlucky(i):
                c_count += 1
            c_dict[str(i)] = i + c_count
        max_conventional_to_lucky = num + 1
        return c_dict[str(num)]

def main():
    filename = 'input/test2.in'
    count = 0
    with open(filename) as f:
        mylist = f.read().splitlines()
        N = int(mylist[0])
        arr = mylist[1:]
        start = time.perf_counter()
        N = 1000
        for x in range(1, 1000):
            # T, num = list(map(int, arr[x].split()))
            T = 1            
            if T == 1:
                # print(lucky_to_conventional(num))
                print(lucky_to_conventional(x))
            if T == 2:
                print(conventional_to_lucky(num))
        print('time', time.perf_counter() - start)
if __name__ == "__main__":
    main()