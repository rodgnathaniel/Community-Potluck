from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

import json

def events_view(request):

    return render(request, "home/events_home.html", {})
