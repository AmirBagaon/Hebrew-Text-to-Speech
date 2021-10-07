from django.shortcuts import render

from django.http import HttpResponse
import json
from django.shortcuts import *
from django.template import RequestContext
import json
from django.shortcuts import *
from django.template import RequestContext
from main.dataHandler import DataHanlder
from main.forms import InputForm, TranslateForm

def index(request):
    return render(request, "toSpeech.html")
def text_to_speech(request):
    return render(request, "toSpeech.html")
def text_utils(request):
    return render(request, "text_utils.html")
def translate_view(request):
    if request.method == "POST":
        print("here in translate_view")
        return render(request, "temp.html")
    context ={}
    context['form']= TranslateForm()
    return render(request, "translate.html", context)

def temp(request):
    returnValue = ""
    if request.method == "POST":
        print(request.POST)
        data = request.POST["input_area"]
        convertion_type = request.POST["convertion_type"]

        handler = DataHanlder(data, convertion_type)
        returnValue = handler.handle()
        
    return HttpResponse(json.dumps({'message': returnValue}), content_type="application/json")

# def something(request):
#     context ={}
#     context['form']= InputForm()
#     return render(request, "something.html", context)