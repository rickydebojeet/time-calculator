def add_time(start, duration, day = None):
    duration_hour = int(duration[0:-3])
    duration_minute = int(duration[-2:])

    if len(start) == 8:
        start_hour=int(start[0:2])
        start_minute=int(start[3:5])

    elif len(start)==7:
        start_hour=int(start[0:1])
        start_minute=int(start[2:4])

    if start_hour==12:
        start_hour=0

    if start[-2:]=="PM":
        start_hour+=12
    minute=start_minute+duration_minute

    if minute>=60:
        minute-=60
        duration_hour+=1
    hour = start_hour+duration_hour
    days = hour//24
    day_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    if day:
        # The index() method returns the position at the first occurrence of the specified value.
        index = day_list.index(day.capitalize())
        index = (index+days) % 7
        day = day_list[index]
    hour = hour % 24
    new_time = ''

    if hour>=12:
        hour-=12
        if hour==0:
            hour=12
        # The rjust() function takes two parameters. Eg; string.rjust(20, "o") adds 'o's before 
        # the string and the number of 'o's plus the number of letters of the string adds up to 20
        new_time+=str(hour)+':'+str(minute).rjust(2,'0')+' PM'

    else:
        if hour==0:
            hour=12
        new_time+=str(hour)+':'+str(minute).rjust(2,'0')+' AM'
    if day:
        new_time+=', ' + day

    if days>0:
        new_time+=' '
        if days==1:
            new_time+="(next day)"
        else:
            new_time+="({} days later)".format(days)
    return new_time

print(add_time("5:01 AM", "0:00", "Monday"))
print(add_time("12:00 AM", "5:00", "Tuesday"))
print(add_time('11:59 PM', '48:01', "Wednesday"))
print(add_time('12:00 AM', "12:00", "Monday"))
print(add_time('12:00 PM', '25:00', 'Wednesday'))
print(add_time('4:00 PM', "107:69", "Monday"))
