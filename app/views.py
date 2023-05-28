from datetime import datetime, date, timedelta, time
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import localtime, make_aware
from django.views.generic import TemplateView, View
from app.models import Staff, Booking

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'app/index.html'
    login_url = '/accounts/login/'
    # 以下のメソッドはトップページにスタッフリストを表示させるため、一時的に記述
    def get(self, request, *args, **kwargs):
        staff_data = Staff.objects.all
        return render(request, 'app/index.html', {
            'staff_data': staff_data,
        })
        
class StaffView(View):
    def get(self, request, *args, **kwargs):
        staff_data = get_object_or_404(Staff.objects.all)

        return render(request, 'app/staff.html', {
            'staff_data': staff_data,
        })

class CalendarView(View):
    def get(self, request, *args, **kwargs):
        staff_data = Staff.objects.filter(id=self.kwargs['pk']).select_related('user')
        today = date.today()
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if year and month and day:
            # 週始め
            start_date = date(year=year, month=month, day=day)
        else:
            start_date = today
        # 1週間
        days = [start_date + timedelta(days=day) for day in range(7)]
        start_day = days[0]
        end_day = days[-1]

        calendar = {}
        # 9時〜18時
        for hour in range(9, 19):
            row = {}
            for day in days:
                row[day] = True
            calendar[hour] = row


        start_time = make_aware(datetime.combine(start_day, time(hour=9, minute=0, second=0)))
        end_time = make_aware(datetime.combine(end_day, time(hour=19, minute=0, second=0)))
        booking_data = Booking.objects.filter(staff=staff_data[0]).exclude(Q(start__gt=end_time) | Q(end__lt=start_time))
        staff_data = staff_data[0]
        for booking in booking_data:
            local_time = localtime(booking.start)
            booking_date = local_time.date()
            booking_hour = local_time.hour
            if (booking_hour in calendar) and (booking_date in calendar[booking_hour]):
                calendar[booking_hour][booking_date] = False
                print("■■■■■■■■■■■■■■■")
                print("calendar.items: " + str(calendar.items))
        return render(request, 'app/calendar.html', {
            'staff_data': staff_data,
            'calendar': calendar,
            'days': days,
            'start_day': start_day,
            'end_day': end_day,
            'before': days[0] - timedelta(days=7),
            'next': days[-1] + timedelta(days=1),
            'today': today,
        })
