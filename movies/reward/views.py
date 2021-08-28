from django.shortcuts import render
from .models import *
from .forms import *
import datetime
# Create your views here.
def index(request):
    return render(request,'reward/add_reward.html')

def artists(request):
   form=ArtistForm
   if request.method=='POST':
       add_artist=ArtistForm(request.POST)
       if add_artist.is_valid():
           add_artist.save()
           return render(request,'reward/artists.html',{'form':form})
        
   return render(request,'reward/artists.html',{'form':form})

def awards(request):
    form=AwardForm
    if request.method=='POST':
       add_awards=AwardForm(request.POST)
       if add_awards.is_valid():
           add_awards.save()
           return render(request,'reward/awards.html',{'form':form})
    
    return render(request,'reward/awards.html',{'form':form})

def movies(request):
    form=MovieForm
    if request.method=='POST':
       add_movies=MovieForm(request.POST)
       if add_movies.is_valid():
           add_movies.save()
           return render(request,'reward/movies.html',{'form':form})
    
    return render(request,'reward/movies.html',{'form':form})

def rating(request):
    form=RatingForm
    if request.method=='POST':
       add_rating=RatingForm(request.POST)
       if add_rating.is_valid():
           add_rating.save()
           return render(request,'reward/rating.html',{'form':form})

    return render(request,'reward/rating.html',{'form':form})


def topten(req):
    movies= Movie.objects.all().order_by('-avg_rating')[:5]
    return render(req, 'reward/display.html', {"context": movies})
def leastten(req):
    movies= Movie.objects.all().order_by('avg_rating')[:5]
    return render(req, 'reward/display.html', {"context": movies})
def within(request):
    start_date = datetime.date(2020, 1,1)
    end_date = datetime.date(2021, 12,1)
    movies = Movie.objects.filter(release_date__range=(start_date, end_date))
    return render(request, 'reward/display.html', {"context": movies})
def search_results(request):
    # breakpoint()
    form = SearchForm(request.POST or None)
    queryset = None
    if request.method == 'POST':
        queryset = Movie.objects.filter(name__icontains=form['name'].value()) or Movie.objects.filter(artist__name=form['name'].value())
        print(queryset)
    context = {
        "form": form,
        "queryset": queryset}
    return render(request, 'reward/search_display.html', context)