import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponseBadRequest, HttpResponseForbidden
# Create your views here.

def index(request):
    # return render(request, "../templates/firstapp/home.html")
    header = "Personal Data"
    langs = ["English", "Deutch", "Kazakh"]
    user = {"name": "Rakhat", "age": "21"}
    addr = ("Almaty", "Qyzylorda", 1)
    value_num = 2
    value_date = datetime.datetime.now()
    value_time = datetime.datetime.now()
    value_title = "this is title"
    data = {"header": header, "langs": langs, "user": user, "addr": addr, "value_num": value_num, "value_date": value_date, "value_time": value_time, "value_title": value_title,}
    return render(request, "../templates/firstapp/index_app1.html", context=data)
def about(request):
    return HttpResponse("<h1>About Me</h1>")
def content(request):
    return HttpResponse("<h1>Content</h1>")
def products(request, product_id=1):
    category = request.GET.get("cat", "Not Identified")
    output = "<h2>Product # {0}, Category: {1}</h2>".format(product_id, category)
    return HttpResponse(output)
def users(request):
    id = request.GET.get("id", "Not Identified")
    name = request.GET.get("name", "Not Identified")
    output = "<h2>User</h2><h3>id:""{0} Name:{1}</h3>".format(id, name)
    return HttpResponse(output)
def details(request):
    return HttpResponsePermanentRedirect("/")

def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Not Correct Data")
    if age > 17:
        return HttpResponse("Access permitted")
    else:
        return HttpResponseForbidden("Access Denied")