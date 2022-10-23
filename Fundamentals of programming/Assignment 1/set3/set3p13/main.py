def det_div(position, num):
    if num%2==0:
        while num%2==0:
            num=num/2
        position-=1
        if position<=0: return position,2
    div=3
    while div<=num:
        if num%div==0:
            while num%div==0: num=num/div
            position-=1
            if position<=0: return position,div
        div=div+2
    return position,div
if __name__ == '__main__':
    n=int(input("Input your number: "))
    copy = n
    n-=1
    aux=1
    current = 2
    while n!=0:
        n,aux=det_div(n,current)
        current+=1
    print(f"The {copy}th element is {aux}! :)")