
from django.shortcuts import render,redirect
from .models import Slot

def slot_list(request):
    slots = Slot.objects.all()
    return render(request,'slots.html',{'slots':slots})

def book_slot(request,id):
    slot = Slot.objects.get(id=id)
    slot.is_booked = True
    slot.save()
    return redirect('/')

def booked_slots(request):
    slots = Slot.objects.filter(is_booked=True)
    return render(request,'booked.html',{'slots':slots})