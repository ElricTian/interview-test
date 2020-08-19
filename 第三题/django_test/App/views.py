from django.http import HttpResponse
from django.shortcuts import render
from App.models import DoubanSpider


def get(request):
    DoubanSpider.objects.create()
    return HttpResponse("200")


def index(request):
    contents = DoubanSpider.objects.all()
    print(contents)
    data = {
        'contents': contents,
    }
    return render(request, "index.html", context=data)


def se(request):
    result = DoubanSpider.objects.all()
    return HttpResponse(result)