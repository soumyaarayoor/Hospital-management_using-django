from django.http import HttpResponse
from django.shortcuts import render
from .models import departments,doctors,booking
from .forms import bookingform
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'index.html')

def booking(request):
    if request.method == "POST":
        form = bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = bookingform()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)
        
   

def doctor(request):
    dict_doc={
        'doctors':doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doc)
def contact(request):
    return render(request,'contact.html')
def department(request):
    dict_dep={
        'dept':departments.objects.all()
    }
    return render(request,'department.html',dict_dep)