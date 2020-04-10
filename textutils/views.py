from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    
def analyze(request):
    # Get the text
    djtext = request.POST.get("text","default")

    # check checkbox values
    removepunc = request.POST.get("removepunc","off")
    fullcaps = request.POST.get("fullcaps","off")
    newlineremove = request.POST.get("newlineremove","off")
    extrasapceremove = request.POST.get("extrasapceremove","off")
    
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    params = {}
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {
                "purpose":"Removed Puncutuations",
                "analyzed_text": analyzed 
                }
        djtext = analyzed
    
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {
                "purpose":"Changed to uppercase",
                "analyzed_text": analyzed 
                }
        djtext = analyzed
    
    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r" :
                analyzed = analyzed + char
        params = {
                "purpose":"Removed new lines",
                "analyzed_text": analyzed 
                }
        djtext = analyzed

    if extrasapceremove == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {
                "purpose":"Removed extra spaces",
                "analyzed_text": analyzed 
                }
    
    if removepunc !="on" and newlineremove != "on" and extrasapceremove !="on" and fullcaps !="on":
        return HttpResponse("Error")


    return render(request,"analyze.html",params)

