#astral hoboken sunset and tomorrow sunrise time code

from astral import *
import datetime
locat = tuple(['Hoboken','NJ',40.748997,-74.0338191,'America/New_York',7.9])
l = Location(locat)


def sunsettime():
	print str(l.sunset())#today sunset time

def sunrisetime():
	print str(l.sunrise(datetime.date.today()+datetime.timedelta(days = 1)))#tomorrow sunrise time