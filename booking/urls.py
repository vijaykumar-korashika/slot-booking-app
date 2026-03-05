from django.urls import path
from . import views

urlpatterns = [
    path('',views.slot_list,name='slots'),
    path('book/<int:id>/',views.book_slot,name='book'),
    path('booked/',views.booked_slots,name='booked'),
]
