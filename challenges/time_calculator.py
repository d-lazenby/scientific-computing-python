def add_time(start, duration, start_dow=None):
    
    def _split_time(time):
        split1 = time.split()
        hours = split1[0].split(':')[0]
        minutes = split1[0].split(':')[1]
        if len(split1) == 2:
            ampm = split1[1]
        else:
            ampm = None

        return hours, minutes, ampm
    # get hours and minutes
    h1, m1, ampm = _split_time(start)
    h2, m2, _ = _split_time(duration)
    
    # calculate sum of minutes
    additional_h, minutes = divmod(int(m1) + int(m2), 60)

    # Convert time to 24h
    if ampm == 'PM':
        h1_24 = int(h1) + 12
    else:
        h1_24 = int(h1)

    total_hours = h1_24 + int(h2) + additional_h

    days, hours = divmod(total_hours, 24)

    if hours >= 12:
      tod = 'PM'
    else:
      tod = 'AM'
    
    hours = hours % 12
    if hours == 0:
        hours = 12
        
    return f"{hours}:0{minutes} {tod}" if minutes < 10 else f"{hours}:{minutes} {tod}"


print(add_time('6:30 PM', '205:12'))

