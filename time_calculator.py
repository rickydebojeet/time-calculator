def add_time(start, duration, dayOfWeek = None):
  
  #Conversion of Start 12 hour format to 24 hour format
  startFormat = start.split(" ")
  startTime = startFormat[0].split(":")
  startAmPm = startFormat[1]
  startHour = int(startTime[0])
  startMinute = int(startTime[1])
  
  if startAmPm == "PM" :
    startHour = startHour + 12

  #Conversion of Start hours into minutes
  startMinute = startMinute + (60 * startHour)
  return new_time