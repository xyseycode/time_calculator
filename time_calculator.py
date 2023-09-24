def add_time(start, duration, day=""):
    start_time = start.split()
    time = start_time[0].split(":")
    c_format = start_time[1]
    start_hour = int(time[0])
    start_minutes = int(time[1])

    l_duration = duration.split(":")
    added_hour = int(l_duration[0])
    added_minutes = int(l_duration[1])
    day_value = 0
    final_day = ""

    # for the days
    days = {1:'Sunday',
            2:'Monday',
            3:'Tuesday',
            4:'Wednesday',
            5:'Thurdsday',
            6:'Friday',
            7:'Saturday'}
    
    
    

    # convert start_hour to 24 hour format
    if c_format == 'PM' and 12 > start_hour > 0:
        start_hour += 12

    
    if c_format == 'AM' and start_hour == 12:
        start_hour -= 0
    
    # add the minutes and by that 
    total_minutes = start_minutes + added_minutes
    carryover_minutes = 0
    final_minutes = total_minutes
    if total_minutes > 59:
        carryover_minutes = total_minutes // 60
        final_minutes = total_minutes % 60

    total_hours = start_hour + added_hour + carryover_minutes
    days_later = 0
    final_hour = total_hours

    if total_hours > 23:
        days_later = total_hours // 24
        final_hour = total_hours % 24

    if final_hour < 12:
        c_format = 'AM'
        if final_hour == 0:
            final_hour = 12
    else:
        c_format = 'PM'
        final_hour -= 12
        if final_hour == 0:
            final_hour = 12
    
    if day:
        day = day.title()
        key_list = list(days.keys())
        val_list = list(days.values())
        index = val_list.index(day)
        day_value = key_list[index]
        day_value = day_value + days_later
        if day_value > 7:
            day_value = day_value % 7
            final_day = days[day_value]
        else:
            final_day = days[day_value]
        if  days_later == 0:
            return f"{final_hour}:{final_minutes:02d} {c_format}, {final_day}"
        if days_later == 1:
            return f"{final_hour}:{final_minutes:02d} {c_format}, {final_day} (next day)"
        if days_later > 1:
            return f"{final_hour}:{final_minutes:02d} {c_format}, {final_day} ({days_later} days later)"
    
    if  days_later == 0:
        return f"{final_hour}:{final_minutes:02d} {c_format}"
    if days_later == 1:
        return f"{final_hour}:{final_minutes:02d} {c_format} (next day)"
    if days_later > 1:
        return f"{final_hour}:{final_minutes:02d} {c_format} ({days_later} days later)"


    return "There's an error!"