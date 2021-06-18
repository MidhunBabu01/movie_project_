from django.contrib import admin

# Register your models here.
from movie_app.models import    ComingSooon,  MovieDetailss, LatestNews

admin.site.register(ComingSooon)
admin.site.register(MovieDetailss)
admin.site.register(LatestNews)
