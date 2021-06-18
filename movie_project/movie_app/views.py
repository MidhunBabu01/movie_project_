from django.shortcuts import render

# Create your views here.
from movie_app.models import  ComingSooon, MovieDetailss, LatestNews 
from django.core.paginator import Paginator, EmptyPage,InvalidPage



def index(request):
    obj = MovieDetailss.objects.all()
    obj2 = MovieDetailss.objects.all()
    popular = MovieDetailss.objects.filter(categories="popular")
    comingsoon = ComingSooon.objects.all()
    toprated = MovieDetailss.objects.filter(categories="toprated")
    flops = MovieDetailss.objects.filter(categories="flop")
    latestnews =LatestNews.objects.all()
    return render(request,'index.html', {"Movie":obj, "Video":obj2, "popular":popular, "comingsoon":comingsoon,"toprated":toprated,"flops":flops,"latestnews":latestnews})

def allmovieslist(request):
    allmovielist = MovieDetailss.objects.all()
    paginator = Paginator(allmovielist,12)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        allmovie = paginator.page(page)
    except(EmptyPage, InvalidPage):
        allmovie = paginator.page(paginator.num_pages)
    return render(request,"allmovielists.html", {"allmovie":allmovie})

def moviedetails(request,movie_id):
    moviesdetail = MovieDetailss.objects.filter(id=movie_id)
    return render(request,"moviesdetails.html", {"moviesdetail":moviesdetail})


