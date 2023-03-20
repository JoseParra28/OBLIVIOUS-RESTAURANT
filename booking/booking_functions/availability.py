import datetime
from booking.models import Table, Booking


def check_availability(table_number, arrival_time, departure_time):
    
