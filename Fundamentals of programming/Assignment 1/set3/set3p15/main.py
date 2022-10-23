def is_perfect(num):
    sum=1
    div=2
    while div*div<num:
        if num%div==0: sum=sum+div+num/div
        div+=1
    if div*div==num: sum=sum+div
    if sum==num:return 1
    else: return 0

if __name__ == '__main__':
    n=int(input("Your number is: "))
    perf_num=n-1
    ok=0
    while perf_num>5 and ok==0:
        if is_perfect(perf_num)==1:
            print(f"The largest perfect number smaller than {n} is {perf_num}")
            ok=1
        else: perf_num-=1
    if ok==0: print(f"There is no perfect number smaller than {n}")