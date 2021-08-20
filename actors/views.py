from django.shortcuts import render

# Create your views here.
import json

from django.http     import JsonResponse
from django.views    import View

from actors.models import Actor
from movies.models import Movie

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            movie_lists = actor.movie_set.all()
            results2 = []
            for movie_list in movie_lists:
                results2.append(
                    {
                        "title" : movie_list.title,
                    }
                )

            results.append(
                {
                    "first_name" : actor.first_name,
                    "last_name" : actor.last_name,
                    "showed movie" : results2, 
                }
            )
        return JsonResponse({'results' : results}, status=200)

# 1시간 21분