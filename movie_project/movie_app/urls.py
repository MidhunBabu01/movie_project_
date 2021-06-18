from django.urls import path
from movie_app import views

app_name = "movie_app"

urlpatterns = [
    path('',views.index,name='index'),
    path('allmovies/', views.allmovieslist, name='allmovies'),
    path('moviedetails/<int:movie_id>', views.moviedetails, name='moviedetails')

]
