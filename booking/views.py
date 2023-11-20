from django.shortcuts import render, redirect
from .models import BookingDate, TimeSlot, Booking
from .forms import TimeSlotForm

# Create your views here.
def view_all(request):
    return  render(request, 'booking/view_all.html')

def create_booking(request):
    if request.method == 'POST':
        timeslot_id = request.POST.get('booking_slot')
        timeslot = TimeSlot.objects.get(id=timeslot_id)
        Booking.objects.create(timeslot=timeslot)
        return redirect('booking_page')

    dates = BookingDate.objects.all().prefetch_related('time_slots')
    return render(request, 'booking/create.html', {'dates' : dates})

def add_timeslot(request):
    if request.method == 'POST':
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_page')
    else:
        form = TimeSlotForm()
    
    return render(request, 'booking/add_timeslot.html', {'form': form})