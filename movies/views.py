from django.shortcuts import render

# Create your views here.

import json

from django.http     import JsonResponse
from django.views    import View

from actors.models import Actor
from movies.models import Movie

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            actor_lists = movie.actors.all()
            results2 = []
            for actor_list in actor_lists:
                results2.append(
                    {
                        "last_name" : actor_list.last_name,
                    }
                )

            results.append(
                {
                    "title" : movie.title,
                    "running_time" : movie.running_time,
                    "showed actor" : results2, 
                }
            )
        return JsonResponse({'results' : results}, status=200)