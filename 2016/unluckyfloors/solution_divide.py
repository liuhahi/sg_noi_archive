import time

def dp(d, s): 
    if s == 4:
        return 0    
    if d == 0:
        return 0    
    elif d == 1:
        return 1
    elif d > 1:
        if s == 0:
            return dp(d-1, 0) + dp(d-1, 1) + dp(d-1, 2) + dp(d-1,3) \
                + dp(d-1,5) + dp(d-1,6) + dp(d-1,7) + dp(d-1,8) + dp(d-1,9)
        elif s == 1:
            return 7 * (dp(d-1, 2)) + dp(d-1, 1) 
        else:
            return 8 * (dp(d-1, 2)) + dp(d-1, 1)


# def all_number_start_with_d_and_have_p_digit(p, d):
    # 20:1   2  3  4  5  6  7  8  9
    #    10,11,12,15,16,17.18,19,20
    # 143: (0 dao 100) + (100 dao 140) + (140 dao 143)
'''
dp(1, 0) = 0
dp(1, 1) = 1
dp(1, 2) = 1
dp(1, 3) = 1

dp(1, 5) = 1
dp(1, 6) = 1
dp(1, 7) = 1
dp(1, 8) = 1
dp(1, 9) = 1
dp(2, 0) = 8 
dp(2, 1) = 8
dp(2, 2) = 9
dp(2, 3) = 9

dp(2, 5) = 9
dp(2, 6) = 9
dp(2, 7) = 9
dp(2, 8) = 9
dp(2, 9) = 9
dp(3, 0) = 79
dp(3, 1) = 87
dp(3, 2) = 87
'''

def main():
    filename = 'input/test.in'
    count = 0
    print(dp(2,0), dp(1,2))
    with open(filename) as f:
        mylist = f.read().splitlines()
        N = int(mylist[0])
        arr = mylist[1:100]
        # arr = mylist
        start = time.perf_counter()        
        for x in range(97):
            T, num = list(map(int, arr[x].split()))            
            if T == 1:
                num_str = str(num)
                p = len(num_str)
                # d = int(num_str[0])
                count = 0
                if "4" in num_str or "13" in num_str:
                    print("-1")
                    continue
                pre = 0
                for c in num_str:                     
                    d = int(c)                                                              
                    if d == 0:
                        dp(p-1, 0)
                        # if p == 1:
                        #     count += 1
                        # else:
                        #     count += 0                      
                    elif d == 1: 
                        count += dp(p, 0)
                    elif d == 2:
                        count += dp(p, 0) + dp(p, 1)
                    elif d == 3:
                        count += dp(p, 0) + dp(p, 1) + dp(p, 2)
                    elif d > 4:
                        for i in range(d):
                            count += dp(p, i)
                        if pre == 1:
                            count -= dp(p, 3)
                    # elif d == 5:
                    #     if pre == 1:
                    #         count += dp(p, 0) + dp(p, 1) + dp(p, 2)
                    #     else:
                    #         count += dp(p, 0) + dp(p, 1) + dp(p, 2) + dp(p, 3)
                    #     # count += (d - 2) * dp(p, 2) + dp(p, 1) 
                    # elif d == 6:
                    #     if pre == 1:
                    #         count += dp(p, 0) + dp(p, 1) + dp(p, 2) + dp(p, 3) + dp(p, 4) + dp(p, 5)                                                                    
                    #     else:
                    #         count += dp(p, 0) + dp(p, 1) + dp(p, 2) + dp(p, 3) + dp(p, 4) + dp(p, 5) + dp(p, 6)
                    # elif d == 7:
                        
                    #     count += dp(p, 0) + dp(p, 1) + dp(p, 2) + dp(p, 3) + dp(p, 4) + dp(p, 5) + dp(p, 6)
                    # elif d == 8:
                    #     count += dp(p, 0) + dp(p, 1) + dp(p, 2) + dp(p, 3) + dp(p, 4) + dp(p, 5) + dp(p, 6) + dp(p, 7)
                    # elif d == 9:
                    #     count += dp(p, 0) + dp(p, 1) + dp(p, 2) + dp(p, 3) + dp(p, 4) + dp(p, 5) + dp(p, 6) + dp(p, 7) + dp(p, 8)                                               

                    # elif d < 4:                                                                                                                                                 
                    #     count += (d - 2)* dp(p, 2) + dp(p, 1) + dp(p, 0)
                    # elif d > 4:
                    #     count += (d - 3)* dp(p, 2) + dp(p, 1) + dp(p, 0) 
                    p = p - 1
                    pre = d                  
                print(count)
            elif T == 2:
                print('doing..')
                # print(dp(p, d))
        print(time.perf_counter() - start)
'''
dp(1, 0) = 0
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
d = starting number

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

start with 2
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