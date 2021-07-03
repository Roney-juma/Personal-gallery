from django.shortcuts import render, redirect
import datetime as dt
from .models import Image

# Create your views here.
#Function to display photos that have been posted today.
def todays_pics(request):

    date = dt.date.today()
    pics = Image.todays_pics()

    return render (request, 'all-photos/recent_pics.html',{"date":date, "pics":pics}) 

#Function to redirect to photos posted in the past
def past_pics (request, past_date):
    #Convert date from the url string

    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False
    
    if date ==dt.date.today():
        return redirect(todays_pics)

    return render(request, 'all-photos/past_pics.html', {"date": date})
    