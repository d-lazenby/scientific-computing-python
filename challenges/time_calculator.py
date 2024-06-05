def add_time(start, duration, start_dow=None):
    # Get hours and minutes for time and duration
    time_h, time_m, ampm = split_time(start)
    duration_h, duration_m, _ = split_time(duration)
    
    # Calculate sum of minutes
    additional_h, minutes = divmod(int(time_m) + int(duration_m), 60)

    # Convert time to 24h
    if ampm == 'PM':
        time_h_24 = int(time_h) + 12
    else:
        time_h_24 = int(time_h)

    total_hours = time_h_24 + int(duration_h) + additional_h
    
    days, hours = divmod(total_hours, 24)
    
    # If we have more than 12 hours leftover, it's the afternoon
    if hours >= 12:
      tod = 'PM'
    else:
      tod = 'AM'
    
    # 12 PM should be labelled 12, not 0
    hours = hours % 12
    if hours == 0:
        hours = 12

    new_time = f"{hours}:0{minutes} {tod}" if minutes < 10 else f"{hours}:{minutes} {tod}"

    # Minutes left of the current day
    minutes_remaining = time_to_new_day(time_h, time_m, ampm)

    # Number of days and minutes we're adding on
    days, duration_mins_remaining = days_and_minutes(duration_h, duration_m)

    # If this is true, we've gone onto the next day
    if duration_mins_remaining > minutes_remaining:
        days += 1
        
    # Fix format of output to include new day of week
    if start_dow:
        DAYS_OF_WEEK = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

        start_dow_idx = DAYS_OF_WEEK[start_dow.title()]
        new_dow = ', ' + list(DAYS_OF_WEEK.keys())[list(DAYS_OF_WEEK.values()).index((start_dow_idx + days) % 7 )]
    
    else:
        new_dow = ''

    if days == 0:
        return new_time + new_dow
    elif days == 1:
        return new_time + new_dow + ' (next day)'
    else:
        return new_time + new_dow + f" ({days} days later)"
    
def split_time(time):
    split1 = time.split()
    hours = split1[0].split(':')[0]
    minutes = split1[0].split(':')[1]
    if len(split1) == 2:
        ampm = split1[1]
    else:
        ampm = None

    return hours, minutes, ampm

def time_to_new_day(hours, minutes, ampm):
    
    if ampm == 'PM':
        hours_to_next = 12 - int(hours)
    else:
        hours_to_next = 24 - int(hours)

    mins_to_next = hours_to_next * 60 - int(minutes)

    return mins_to_next

def days_and_minutes(hours, minutes):
    
    days, hours_r = divmod(int(hours), 24)

    minutes_r = hours_r * 60 + int(minutes)
    
    return days, minutes_r

# TESTS
print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)
