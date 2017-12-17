import calendar

from rest_framework.views import APIView
from rest_framework.response import Response


class CalendarView(APIView):
    def get(self, request, year, month):
        cal = calendar.TextCalendar()
        return Response({"calendar": cal.monthdayscalendar(int(year), int(month))})
