def add_time(start, duration, weekday=None):

    st_h = start.split(':')[0]
    st_h = int(st_h)
    st_m = start.split(':')[1]
    st_m= st_m.split(' ')[0]
    st_m= int(st_m)

    ampm_i = start.split(' ')[1]

    dur_h = duration.split(':')[0]
    dur_h = int(dur_h)
    dur_m = duration.split(':')[1]
    dur_m = int(dur_m)

    if ampm_i == 'AM':
        new_h = st_h + dur_h

    elif ampm_i == 'PM':
        new_h = st_h + dur_h + 12
        
    new_m = st_m + dur_m

    dd = new_h // 24
    if dd >= 1 and dd < 2:
        dl = ' (next day)'
        new_h = new_h -24
    elif dd>=2:
        dds = str(dd)
        dl = ' (' +  dds + ' days later)'
        new_h = new_h - (dd * 24)
    else:
        new_h_s = new_h
        dl = ''

    if new_h > 12:
        new_h = new_h - 12
        ampm = 'PM'
    else:
        ampm = 'AM'

    mm = new_m // 60
    if mm >= 1:
        new_h = new_h + 1
        new_m = new_m - 60

    new_h_s = str(new_h)
    new_m_s = str(new_m)

    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if weekday is not None:
        weekday1 = weekday.capitalize()
        index = week.index(weekday1)
        ddd = index + dd
        if ddd > 6:
            cat = ddd // 7
            ddd = ddd - (cat * 7)
        weekday2 = week[ddd]

    if weekday is not None:
        new_time = new_h_s + ':' + new_m_s + ' ' + ampm +', '+ weekday2 + dl
        return new_time
    else:
        new_time = new_h_s + ':' + new_m_s + ' ' + ampm + dl
        return new_time

xx = add_time("10:30 PM", "10515:13", "saTuRdaY")
#xx = add_time("3:30 AM", "157820000:13")
print(xx)
