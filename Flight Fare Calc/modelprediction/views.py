from django.shortcuts import render
from django.http import HttpResponse
from modelprediction.machine import *
# Create your views here.
def home(request):
    return render(request,'modelprediction/home.html')

def result(request):
    company=request.GET.get('company')
    source=request.GET.get('source')
    destination=request.GET.get('destination')
    stops=request.GET.get('stops')
    datej=request.GET.get('datej')
    arrival=request.GET.get('arrival')
    deparuture=request.GET.get('departure')
    # print(company,source,stops,destination,arrival,deparuture,datej)
    dic={'company':company,'source':source,'destination':destination,'stops':stops,'datej':datej,'arrival':arrival,'departure':deparuture}
    res=processing(dic)
    dic['max_val']=max(res.values())
    dic.update(res)
    return render(request,'modelprediction/result.html',dic)