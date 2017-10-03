from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from swx import Target

@csrf_exempt
def LocateTarget(request):
    
    t = Target.TargetLoc()
    targetLoc = t.locate(request.body.decode("utf-8"))
    resp = HttpResponse(targetLoc)
    resp.__setitem__("Content-Type", "application/json")
    
    return resp
