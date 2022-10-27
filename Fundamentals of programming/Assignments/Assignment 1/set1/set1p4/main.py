def largest_num(list):
    """
    This function computes the largest item that can be made with a set of given digits.

    By starting from 9, we keep adding a new digit if it's in our list to the end of the number, therefor it having
    the highest value possible.
    :param list: the list of digits we can use
    :return: returns the largest number that can be made with the given digits
    """
    num=0
    for i in range(9,-1,-1):
        while list[i] != 0 :
            num=num*10+i
            list[i]-=1
    return num
if __name__ == '__main__':
    n = int(input("Enter your number: "))
    copy = n #we use this copy so we don't lose the users number
    digit_list = [0]*10 #a list with all the digits of our number
    while copy>0:
        digit_list[copy%10]+=1
        copy=copy//10
    print(f"The largest number made from the digits in {n} is {largest_num(digit_list)}.")
