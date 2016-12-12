from datetime import datetime, time, timedelta
from threading import Timer
import googleCalendar
import sqlite3
import googleCalendar

# Initialize SQLite
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
"""
x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1
"""
def setCurrentState(val):
    query = 'UPDATE home_wakeup set wakeuptime_plan = "val"'
    cur.execute(query)
def setAlarm():
    eventList = googleCalendar.getEvents()
    timeToGetReady = timedelta(hours=1)
    alarmTime = 0
    latestEvent = datetime.today()
    latestEvent.replace(hour=11,minute=0,second=0)
    if eventList:
        for event in eventList:
            timeOfEvent = datetime.datetime.strptime(event[0],"%Y-%m-%dT%H:%M:%S.%f") #this line doesn't quite parse right yet

            if timeOfEvent < datetime.now():
                continue
            if timeOfEvent > latestEvent:
                alarmTime = latestEvent - timeToGetReady
                break
            alarmTime = timeOfEvent - timeToGetReady
    else:
        alarmTime = latestEvent - timeToGetReady
    setCurrentState(alarmTime)
    print alarmTime
    #t.stop()
    #t.start()

#t = Timer(secs, setAlarm)
#t.start()


    
if __name__ == "__main__":
    setAlarm()
