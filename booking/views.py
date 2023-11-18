from django.shortcuts import render

# Create your views here.
def view_all(request):
    return  render(request, 'booking/view_all.html')