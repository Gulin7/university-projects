def find_month(day,mdays):
    """
    This function finds the date we are in (month,day).

    :param day: the day of the year we're working with
    :param mdays: a list with the months number of days
    :return:
    """
    month=1
    while day>mdays[month]:
        day=day-mdays[month]
        month+=1
    return month,day

if __name__ == '__main__':
    mdict={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",
          11:"November",12:"December"}
    year=int(input("The year number is: "))
    day=int(input("The day number is: "))
    mdays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    m,d=find_month(day,mdays)
    daydict={1:"st",2:"nd",3:"rd"}
    for i in range(4,32):
        daydict[i]="th"
    print(f"The date is: {year} {mdict[m]} {d}{daydict[d]}.")
