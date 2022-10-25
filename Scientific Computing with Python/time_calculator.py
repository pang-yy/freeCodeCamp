def add_time(start, duration, startingDay=""):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # turn into 24-hour format
    start = start.split(':')
    hour = 0
    minute = 0
    if start[1][-2:] == "PM":
        hour = int(start[0]) + 12
    else:
        hour = int(start[0])
    minute = int(start[1][:2])

    minute += int(duration[-2:])
    hour += int((duration.split(':'))[0])
    if minute >= 60:
        hour += 1
        minute -= 60
    
    count = 0
    msg = ''
    while hour >= 24:
        hour -= 24
        count += 1
    if hour >= 13:
        hour -= 12
        period = 'PM'
    else:
        if hour == 12:
            period = 'PM'
        else:
            period = 'AM'
            if hour == 0:
                hour += 12
    msg += str(hour) + ':' + "{:02d}".format(minute) + ' ' + period

    if startingDay != '':
        position = days.index(startingDay.lower())
        position += count
        while position >= 7:
            position -= 7
        endDay = days[position]
        msg += ', ' + endDay.capitalize()

    if count > 1:
        msg += ' (' + str((count)) + ' days later)'
    elif count == 1:
        msg += ' (next day)'
    return msg
    