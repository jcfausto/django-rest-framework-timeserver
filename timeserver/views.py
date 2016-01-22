from rest_framework.views import APIView
from .mixins import JSONResponseMixin
from datetime import datetime
from pytz import timezone as pytz_timezone
import pytz

class TimeView(APIView):

	def get(self, request):
		"""
		Takes a timezone (or UTC by default) and returns the current time 
		"""
		timezone = request.GET.get('timezone')

		#Standard check and defaults to UTC in case of missing or incorrect timezone.
		try:
			if timezone:
				tz = pytz_timezone(timezone)
			else:
				tz = pytz.utc
		except:
			tz = pytz.utc

		time = tz.localize(datetime.now())

		#give more that needed information about the time, because we can. 
		data = {
			'time' : time.isoformat(),
			'year' : time.year,
			'month' : time.month,
			'day' : time.day,
			'hour' : time.hour,
			'minute' : time.minute, 
			'second' : time.second, 
			'microsecond' : time.microsecond, 
			'timezone' : time.tzname() if time.tzinfo else '',
		}

		# returns the data formatted in JSON and sets up response
		return JSONResponseMixin(data)
