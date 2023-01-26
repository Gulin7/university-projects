def form_number(digit_list):
    """
    This function computes the smallest possible number made with the digits in a given frequency list.

    The function starts from 1 and it ads digits to the right one by one, thus making the smallest possible number.
    :param digit_list: the given digits in a form of a list ( frequence )
    :return: the smallest number that can be made with a set of digits
    """
    smallest_nr=0
    for i in range (1,10):
        while digit_list[i]>0:
            digit_list[i]-=1
            smallest_nr = smallest_nr*10+i
    return smallest_nr
if __name__=='__main__':
    digit_list = [0] * 10
    n=int(input("Your chosen number: "))
    copy=n
    while copy>0:
        digit = int(copy % 10)
        digit_list[digit]+=1
        copy=copy//10
    print(f"The smallest number made from the digits your chosen number has is {form_number(digit_list)}")