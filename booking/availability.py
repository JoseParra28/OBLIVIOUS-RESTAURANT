import datetime
from booking.models import Table, Booking


def check_availability(table_number, arrival_time, departure_time):
    avail_list = []
    booking_list = Booking.objects.filter(table=table)
    for Booking in booking_list:
        if booking.arrival_time > departure_time or booking.departure_time < arrival_time:
            avail_list.append(True)
            else:
                avail_list.append(False)
    return all(avail_list)          
