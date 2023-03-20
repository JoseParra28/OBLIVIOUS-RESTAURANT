from django.urls import path
from .views import Table_list, Booking_list

app_name = 'booking'

urlpatterns = [
    path('table_list/', Table_list.as_view(), name='Table_list'),
    path('booking_list/', Booking_list.as_view(), name='Booking_list'),
]
 