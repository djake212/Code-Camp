def add_time(start, duration, day = -1):
  timelst1 = start.split()
  timelst2 = timelst1[0].split(':')
  hour = int(timelst2[0])
  minute = int(timelst2[1])
  daysPast = 0
  weeklst = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
  if day != -1:
    try:
      daynum = weeklst.index(day.lower())
    except:
      return 'Enter valid start date'
      quit()
    
  if timelst1[1].upper() == 'PM':
    if hour != 12:
      hour += 12
  
  durlst = duration.split(':')
  houradd = int(durlst[0])
  minadd = int(durlst[1])
  if (minute + minadd) >= 60:
    hour += int((minute + minadd) / 60)
    minute = (minute + minadd) % 60
  else:
    minute += minadd
  if (hour + houradd) >= 24:
    daysPast = int((hour + houradd) / 24)
    hour = (hour + houradd)%24
  else:
    hour += houradd

  if day != -1:
    daynum = (daynum + daysPast) % 7
    daystr = weeklst[daynum].title()
  
  if daysPast > 1:
    pastmes = ' (' + str(daysPast) + ' days later)'
  elif daysPast == 1:
    pastmes = ' (next day)'
  else:
    pastmes = ''

  ampm = 'AM'
  if hour > 12:
    ampm = 'PM'
    hour -= 12
  elif hour == 12: ampm = 'PM'
    
  if minute <= 9:
    minute = '0' + str(minute)

  if hour == 0: hour = 12

  if day == -1:
    new_time = str(hour) + ':' + str(minute) + ' ' + ampm + pastmes
  else:
    new_time = str(hour) + ':' + str(minute) + ' ' + ampm + ', ' + daystr + pastmes

  return new_time