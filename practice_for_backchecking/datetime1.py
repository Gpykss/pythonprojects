import _datetime

if __name__ == '__main--':

    # date = _datetime.date(2025,9,22)
    # today = _datetime.date.today()

    time = _datetime.time(23, 59, 59)
    today_time = _datetime.datetime.now()

    today_time = today_time.strftime("%H : %M : %S  %Y: %m: %d")

    time_current = _datetime.datetime(2030, 2, 10, 10, 35, 10)
    time_future = _datetime.datetime.now()

    if time_current < time_future:
        print("THe date and Time has passed ")
    else:
        print("The date and time  has not passed ")

    print(today_time)