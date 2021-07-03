from django.shortcuts import render
import datetime as dt
from .models import Image

# Create your views here.
#Function to display photos that have been posted today.
def todays_pics(request):

    date = dt.date.today()
    pics = Image.todays_pics()

    return render (request, 'all-photos/recent_pics.html',{"date":date, "pics":pics})     