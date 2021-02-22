durations = [53, 153, 4153, 400153]
sec_in_minute = 60
sec_in_hour = 3600
sec_in_day = 86400

for duration in durations:
    duration_module = duration

    seconds = duration_module % sec_in_hour % sec_in_minute
    minutes = duration_module % sec_in_hour // sec_in_minute
    hours = duration_module % sec_in_day // sec_in_hour
    days = duration_module // sec_in_day

    if duration_module < 0:
        duration_module *= -1

        seconds = duration_module % sec_in_hour % sec_in_minute * -1
        minutes = duration_module % sec_in_hour // sec_in_minute * -1
        hours = duration_module % sec_in_day // sec_in_hour * -1
        days = duration_module // sec_in_day * -1

    print('duration =', duration)

    if duration_module >= sec_in_day:
        print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')

    elif sec_in_hour <= duration_module < sec_in_day:
        print(hours, 'час', minutes, 'мин', seconds, 'сек')

    elif sec_in_minute <= duration_module < sec_in_hour:
        print(minutes, 'мин', seconds, 'сек')

    else:
        print(duration, 'сек')
