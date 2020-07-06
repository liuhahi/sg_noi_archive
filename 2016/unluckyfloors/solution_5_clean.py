import time

def dp(p, d):   
    if p == 0 or d == 4:
        return 0    
    elif p == 1:
        return 1
    elif p > 1:
        if d == 0:
            return dp(p-1, 0) + dp(p-1, 1) + dp(p-1, 2) + dp(p-1,3) + dp(p-1,5) + dp(p-1,6) + dp(p-1,7) + dp(p-1,8) + dp(p-1,9)
        elif d == 1:
            return 7 * (dp(p - 1, 2)) + dp(p - 1, 1) 
        else:
            return 8 * (dp(p - 1, 2)) + dp(p - 1, 1)

def main():
    filename = 'input/6.1.in'
    count = 0
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
                count = 0
                if "4" in num_str or "13" in num_str:
                    print("-1")
                    continue
                pre = 0
                for c in num_str:                     
                    d = int(c)                                                              
                    if d == 0:
                        count += 0  
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
                    p = p - 1
                    pre = d                  
                print(count)
            elif T == 2:                
                print('doing..')
        print(time.perf_counter() - start)
if __name__ == "__main__":
    main()