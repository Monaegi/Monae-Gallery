import calendar

from rest_framework.views import APIView
from rest_framework.response import Response


class CalendarView(APIView):
    def get(self, request, year, month):
        cal = calendar.TextCalendar()
        days = [0] + list(cal.itermonthdays(int(year), int(month)))
        week_list = [days[i:i+7] for i in range(0, len(days), 7)]
        if week_list[0][6] == 0:
            return Response({"calendar": week_list[1:]})
        return Response({"calendar": week_list})
