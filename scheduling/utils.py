from datetime import datetime

from scheduling.models.schedule_model import Schedule
from scheduling.models.appointment_model import Appointment


def free_time_intervals(day: datetime, user: int) -> [(datetime, datetime), ...]:
    """
    :param day: direct day
    :param user: direct user
    :return: list free time intervals
    """

    schedules = Schedule.objects.filter(start_datetime__day=day.day,
                                        start_datetime__month=day.month,
                                        start_datetime__year=day.year,
                                        user=user).order_by('start_datetime')

    intervals = []
    for schedule in schedules:
        intervals.append((schedule.start_datetime, schedule.end_datetime))

    appointments = Appointment.objects.filter(start_datetime__day=day.day,
                                              start_datetime__month=day.month,
                                              start_datetime__year=day.year,
                                              specialist=user).order_by('start_datetime')

    new_intervals = []
    for appointment in appointments:
        for interval in intervals:
            if interval[0] < appointment.start_datetime < interval[1]:
                intervals.append((interval[0], appointment.start_datetime))
                intervals.append((appointment.start_datetime+appointment.procedure.duration, interval[1]))
                intervals.remove(interval)

    return intervals
