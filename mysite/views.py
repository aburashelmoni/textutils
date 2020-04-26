# I have created the Website
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Rashel' , 'place':'Dhaka'}
    return render(request,'index.html', params)

def index2(request):
    params = {'name':'Rashel' , 'place':'Dhaka'}
    return render(request,'index2.html', params)

def aboutus(request):
    params = {'name':'Rashel' , 'place':'Dhaka'}
    return render(request,'aboutus.html', params)

def contactus(request):
    params = {'name':'Rashel' , 'place':'Dhaka'}
    return render(request,'contactus.html', params)    

def analyze(request):

    #Get the text
    djtext = request.POST.get('text', 'default')
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Capitalized the given Charachter', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        params = {'purpose':'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Remove Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(charcount == "on"):        
        count = len(djtext)
        if(removepunc != "on" and fullcaps !="on" and newlineremover != "on" and extraspaceremover != "on"):
            analyzed =  count
        else:
            analyzed = f"{djtext} \n {count}"
        params = {'purpose':'Character Counter', 'analyzed_text': analyzed}
    
    if(removepunc != "on" and fullcaps !="on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)