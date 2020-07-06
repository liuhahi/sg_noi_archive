import time

def dp(p, d):     
    if p == 1:
        # if d == 0:            
        #     return 0
        # else:
        return 1
    elif p > 1:
        # if p == 2:
        #     if d == 0 or d == 1:            
        #         return 8
        #     else:
        #         return 9
        # if d == 0:
        #     return 8 * (dp(p - 1, 2)) + dp(p - 1, 1)
        if d == 1:
            return 7 * (dp(p - 1, 2)) + dp(p - 1, 1) 
        else:
            return 8 * (dp(p - 1, 2)) + dp(p - 1, 1)


# def all_number_start_with_d_and_have_p_digit(p, d):
    # 20:1   2  3  4  5  6  7  8  9
    #    10,11,12,15,16,17.18,19,20
    # 143: (0 dao 100) + (100 dao 140) + (140 dao 143)


def main():
    filename = 'input/test2.in'
    count = 0
    # 671288625357697 => 
    # 108120520931457
    # 5586396958196672 =>
    # 763140212649935
    # for x in range(10):

    with open(filename) as f:
        mylist = f.read().splitlines()
        N = int(mylist[0])
        arr = mylist[1:20]
        print('n is', N)
        # arr = mylist
        start = time.perf_counter()        
        for x in range(1, 300):
            # T, num = list(map(int, arr[x].split()))
            T = 1
            if T == 1:
                num_str = str(x)
                p = len(num_str)
                # d = int(num_str[0])
                count = 0
                if "4" in num_str or "13" in num_str:
                    print("-1")
                    continue
                num = int(num_str)
                if num <= 12:
                    if num < 4:
                        print(num) 
                    else:
                        print(num - 1)
                    continue
                # pre = 0
                # length = 0
                # is_last = False
                # if x == 10:
                #     pre = 1
                digit = len(num_str)
                for c in num_str:     
                    if digit == 2 and len(num_str) > 3 and int(num_str[-2:0]) <= 12:
                        if num < 4:
                            count += num + 1 
                        else:
                            count += num                                    
                    # length += 1
                    # if length == len(num_str):
                    #     is_last = True                   
                    else:
                        d = int(c)
                        # if d == 0:
                        #     count += 0                                                                  
                        if d < 4:    
                            # print('pre', pre, is_last)   
                            # if pre == 1 and is_last:
                            #     # print('current is', num_str, d)
                            #     count += 1                        
                            if d == 1:

                                count += dp(p, 0)                                           
                            else:
                                count += (d - 1)* dp(p, 2) + dp(p, 1) 
                                # print(num_str,'before count is', count)
                        elif d > 4:
                            count += (d - 2)* dp(p, 2) + dp(p, 1)
                    # print('pre is', pre)
                    p = p - 1   
                    digit -= 1                          
                print(count)
            elif T == 2:
                print('doing..')
                # print(dp(p, d))
        print(time.perf_counter() - start)
'''
1  = dp(1, 0) + dp(1, 1)
2  = dp(1, 0) + dp(1, 1) + dp(1, 2)
3  = dp(1, 0) + dp(1, 1) + dp(1, 2) + dp(1, 3)
5  = dp(1, 0) + dp(1, 1) + dp(1, 2) + dp(1, 3) + dp(1, 5)
6  = dp(1, 0) + dp(1, 1) + dp(1, 2) + dp(1, 3) + dp(1, 5) + dp(1, 6)
7  = dp(1, 0) + dp(1, 1) + dp(1, 2) + dp(1, 3) + dp(1, 5) + dp(1, 6) + dp(1, 7) 
8  = dp(1, 0) + dp(1, 1) + dp(1, 2) + dp(1, 3) + dp(1, 5) + dp(1, 6) + dp(1, 7) + dp(1, 8) 
9  = dp(1, 0) + dp(1, 1) + dp(1, 2) + dp(1, 3) + dp(1, 5) + dp(1, 6) + dp(1, 7) + dp(1, 8) + dp(1, 9)
10 = dp(2, 0) + dp(1, 0)
11 = dp(2, 0) + dp(1, 0) + dp(1, 1)
12 = dp(2, 0) + dp(1, 0) + dp(1, 1) + dp(1, 2)
15 = dp(2, 0) + dp(1, 0) + dp(1, 1) + dp(1, 2), + dp(1, 5)
16 = dp(2, 0) + dp(1, 0) + dp(1, 1) + dp(1, 2), + dp(1, 5) + dp(1, 6)
17 = dp(2, 0) + dp(1, 0) + dp(1, 1) + dp(1, 2), + dp(1, 5) + dp(1, 6) + dp(1, 7)
18 = dp(2, 0) + dp(1, 0) + dp(1, 1) + dp(1, 2), + dp(1, 5) + dp(1, 6) + dp(1, 7) + dp(1, 8)
19 = dp(2, 0) + dp(1, 0) + dp(1, 1) + dp(1, 2), + dp(1, 5) + dp(1, 6) + dp(1, 7) + dp(1, 8) + dp(1, 9)
20 = dp(2, 0) + dp(1, 0) + dp(2, 1) 
21 = dp(2, 0) + dp(1, 0) + dp(2, 1) + dp(1, 1) 
30 = dp(2, 0) + dp(1, 0) + dp(2, 1) + dp(2, 2) 
100 = dp(3, 0) + dp(1, 0)
111 = dp(3, 0) + dp(1, 0) + dp(2, 0) + dp(1, 0) + dp(1, 1)
150 = dp(3, 0) + dp(2, 0) + dp(2, 1) +  dp(1, 0)



250 = dp(2, 25) + dp(2, 1) + dp(2, 1) +  dp(1, 0)
257 = dp(3, 0) + dp(3, 1) 
    + dp(2, 0) + dp(2, 1) + dp(2, 2) + dp(2, 3) + dp(2, 4) 
    + dp()



25 = dp(2, 0) + dp(2, 1) + 3 + 1 + extra
   = 8 + 8 + 3 + 1 + 1
p = number of digits
d = 开头的数字
dp(p, d)
以d开头的1位数的个数
dp(1, 0) = 7 * 0 + 1 * 1 = 0
dp(1, 1) = 7 * 0 + 1 * 1 = 1
dp(1, 2) = 8 * 0 + 1 * 1 = 1
dp(1, 3) = 8 * 0 + 1 * 1 = 1
dp(1, 4) = -1            = -1
dp(1, 5) = 8 * 0 + 1 * 1 = 1
dp(1, 6) = 8 * 0 + 1 * 1 = 1
dp(1, 7) = 8 * 0 + 1 * 1 = 1
dp(1, 8) = 8 * 0 + 1 * 1 = 1
dp(1, 9) = 8 * 0 + 1 * 1 = 1

total 1 => 7 * 1 + 1 = 8

以d开头的两位数的个数
dp(2, 0) = 7 * 1 + 1 * 1 = 8
dp(2, 1) = 7 * 1 + 1 * 1 = 8 # 10 11 12 15 16 17 18 19 
dp(2, 2) = 8 * 1 + 1 * 1 = 9 # 20 21 22 23 25 26 27 28 29
dp(2, 3) = 8 * 1 + 1 * 1 = 9
dp(2, 4) = -1
dp(2, 5) = 8 * 1 + 1 * 1 = 9
dp(2, 6) = 8 * 1 + 1 * 1
dp(2, 7) = 8 * 1 + 1 * 1
dp(2, 8) = 8 * 1 + 1 * 1
dp(2, 9) = 8 * 1 + 1 * 1

total 2 => 7 * 9 + t(1) = 71

dp(3, 0) = 80
dp(3, 1) = 7 * (8 * 1 + 1 * 1) + 8 * 1 = 71
dp(3, 2) = 8 * (8 * 1 + 1 * 1) + 8 * 1 = 80
dp(3, 3) = 8 * (8 * 1 + 1 * 1) + 8 * 1 = 80
dp(3, 4) = -1
dp(3, 5) = 8 * (8 * 1 + 1 * 1) + 8 * 1 = 80
dp(3, 6) = 8 * (8 * 1 + 1 * 1) + 8 * 1 = 80
dp(3, 7) = 8 * (8 * 1 + 1 * 1) + 8 * 1 = 80
dp(3, 8) = 8 * (8 * 1 + 1 * 1) + 8 * 1 = 80
dp(3, 9) = 8 * (8 * 1 + 1 * 1) + 8 * 1 = 80

total 3 => 631 = 7 * 80 + t(2)

dp(4, 0) = 633
dp(4, 1) = 7 * (8 * (8 * 1 + 1 * 1) + 8 * 1) + 71 = 631
dp(4, 2) = 8 * (8 * (8 * 1 + 1 * 1) + 8 * 1) + 71 = 711
dp(4, 3) = 8 * (8 * (8 * 1 + 1 * 1) + 8 * 1) + 71 = 711
dp(4, 4) = -1
dp(4, 5) = 8 * (8 * (8 * 1 + 1 * 1) + 8 * 1) + 71 = 711
dp(4, 6) = 8 * (8 * (8 * 1 + 1 * 1) + 8 * 1) + 71 = 711
dp(4, 7) = 8 * (8 * (8 * 1 + 1 * 1) + 8 * 1) + 71 = 711

dp(p, d) = 

total 4 => 7 * x + 631

dp(3, 1) total = 8  =>  7 * 9 + 1 * 8 = 71
dp(3, 2) total = 9  =>  8 * 9 + 1 * 8 = 80

dp(4, 1) total = 8  =>  (7 * 9) * (7 * 9 + 1 * 8) + (1 * 8) (7 * 9 + 1 * 8) = 71
dp(4, 2) total = 9  =>  8 * 9 + 1 * 8 = 711
dp(4, 3)  



dp(3, 3) = 8 * 9 + 1 * 8 = 80
dp(3, 4) = -1
dp(3, 5) = 8 * 9 + 1 * 8 = 80
dependency_gragh(3, 6) = 8 * 9 + 1 * 8 = 80
dependency_gragh(3, 7) = 8 * 9 + 1 * 8 = 80
dependency_gragh(3, 8) = 8 * 9 + 1 * 8 = 80
dependency_gragh(3, 9) = 8 * 9 + 1 * 8 = 80

'''
if __name__ == "__main__":
    main()