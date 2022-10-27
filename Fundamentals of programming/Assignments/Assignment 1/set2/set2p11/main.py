def digit_freq(num,digit_list):
    """
    Makes a list with the frequency of digits in a given number.

    :param num: the number whose digits we are counting
    :param digit_list: a list with the frequency of each digit in the given number
    :return: the list changes
    """
    if num==0: digit_list[0]=1
    while num>0:
        digit_list[num%10]=1
        num=num//10

if __name__ == '__main__':
    n1=int(input("The first number is: "))
    n2=int(input("The second number is: "))
    digit_l1= [0] * 10
    digit_l2= [0] * 10
    digit_freq(n1,digit_l1)
    digit_freq(n2,digit_l2)
    if digit_l1!=digit_l2:
        print("The two given number do not have the property!!! ;(")
    else:
        print("The two given number have the property :0")