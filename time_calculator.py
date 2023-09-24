def add_time(start, duration, day=""):
    start_time = start.split()
    time = start_time[0].split(":")
    c_format = start_time[1]
    start_hour = int(time[0])
    start_minutes = int(time[1])

    l_duration = duration.split(":")
    added_hour = int(l_duration[0])
    added_minutes = int(l_duration[1])

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
    
    if  days_later == 0:
        return f"{final_hour:02d}:{final_minutes:02d} {c_format}"
    if days_later == 1:
        return f"{final_hour:02d}:{final_minutes:02d} {c_format} (next day)"
    if days_later > 1:
        return f"{final_hour:02d}:{final_minutes:02d} {c_format} ({days_later} days later)"


    return "There's an error!"

# print(add_time("8:16 PM", "466:02"))