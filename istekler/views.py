from django.shortcuts import render, redirect
#import calendar
#from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Istek, Hastane
# Import User Model From Django
from django.contrib.auth.models import User
from .forms import IstekForm, HastaneForm
from django.http import HttpResponse
import csv
from django.contrib import messages

# Import PDF Stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Import Pagination Stuff
from django.core.paginator import Paginator



# Show Event
def show_istek(request, istek_id):
    istek = Istek.objects.get(pk=istek_id)
    return render(request, 'istekler/show_istek.html', {
            "istek":istek
            })

# Show Hastane Istekleri
def HastaneIstekleri(request, hastane_id):
    # Grab the venue
    hastane = Hastane.objects.get(id=hastane_id)	
    # Grab the events from that venue
    istekler = hastane.istek_set.all() # TODO !!!
    if istekler:
        return render(request, 'istekler/venue_events.html', {
            "events":istekler
            })
    else:
        messages.success(request, ("That Venue Has No Events At This Time..."))
        return redirect('admin_approval')

# Create My Events Page
def isteklerim(request):
    if request.user.is_authenticated:
        me = request.user.id
        events = Istek.objects.all()
        return render(request, 
            'istekler/isteklerim.html', {
                "events":events
            })

    else:
        messages.success(request, ("You Aren't Authorized To View This Page"))
        return redirect('home')


# TODO hastane icin txt csv ve pdf olusturucular eklenecek!

# Create your views here.
def istek_ekle(request):
    submitted = False
    if (request.method == "POST"):
        form = IstekForm(request.POST)
        if form.is_valid():
            #form.save()
            istek = form.save(commit=False)
            istek.kullanici_adi = request.user # logged in user
            istek.save()
            return 	HttpResponseRedirect('/istek_ekle?submitted=True')	
    else:
        # Just Going To The Page, Not Submitting 
    
        form = IstekForm

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'istekler/istek_ekle.html', {'form':form, 'submitted':submitted})

def istek_guncelle(request, event_id):
    event = Istek.objects.get(pk=event_id)
    form = IstekForm(request.POST or None, instance=event)
    
    if form.is_valid():
        form.save()
        return redirect('list-events') # TODO

    return render(request, 'istekler/istek_guncelle.html', 
        {'event': event,
        'form':form})

def hastane_guncelle(request, venue_id):
    venue = Hastane.objects.get(pk=venue_id)
    form = HastaneForm(request.POST or None, request.FILES or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues') # TODO

    return render(request, 'istekler/hastane_guncelle.html', 
        {'venue': venue,
        'form':form})

def hastane_ara(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Hastane.objects.filter(name__contains=searched)
    
        return render(request, 
        'istekler/hastane_ara.html', 
        {'searched':searched,
        'venues':venues})
    else:
        return render(request, 
        'istekler/hastane_ara.html', 
        {})

def istek_ara(request):
    if request.method == "POST":
        searched = request.POST['searched']
        events = Istek.objects.filter(tibbi_malzeme_ilac_asi__contains=searched)
    
        return render(request, 
        'istekler/istek_ara.html', 
        {'searched':searched,
        'events':events})
    else:
        events = Istek.objects.all()

        return render(request, 
        'istekler/istek_ara.html',{'events':events} 
        )

def show_hastane(request, venue_id):
    venue = Hastane.objects.get(pk=venue_id)
    venue_owner = User.objects.get(pk=venue.owner)

    # Grab the events from that venue
    events = venue.istek_set.all() # TODO !!!

    return render(request, 'istekler/show_hastane.html', 
        {'venue': venue,
        'venue_owner':venue_owner,
        'events':events})

def list_hastane(request):
    #venue_list = Venue.objects.all().order_by('?')
    venue_list = Hastane.objects.all()

    # Set up Pagination
    p = Paginator(Hastane.objects.all(), 3)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = "a" * venues.paginator.num_pages
    return render(request, 'istekler/hastane.html', 
        {'venue_list': venue_list,
        'venues': venues,
        'nums':nums}
        )

def hastane_ekle(request):
    submitted = False
    if request.method == "POST":
        form = HastaneForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user.id # logged in user
            venue.save()
            #form.save()
            return 	HttpResponseRedirect('/hastane_ekle?submitted=True')	
    else:
        form = HastaneForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'istekler/hastane_ekle.html', {'form':form, 'submitted':submitted})

def butun_istekler(request):
    event_list = Istek.objects.all()
    return render(request, 'istekler/istek_listesi.html', 
        {'event_list': event_list})

        
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "ATO"
    # month = month.capitalize()
    # # Convert month from name to number
    # month_number = list(calendar.month_name).index(month)
    # month_number = int(month_number)

    # # create a calendar
    # cal = HTMLCalendar().formatmonth(
    # 	year, 
    # 	month_number)
    # # Get current year
    # now = datetime.now()
    # current_year = now.year
    
    # Query the Events Model For Dates
    event_list = Istek.objects.all()

    # Get current time
    #time = now.strftime('%I:%M %p')
    return render(request, 
        'istekler/home.html', {
        "name": name,
        # "year": year,
        # "month": month,
    
        "event_list": event_list,
        })