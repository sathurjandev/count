from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    words = request.GET['word']
    worddict = {}
    list = words.split()
    for word in list:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word]=1
    return render(request,'count.html',{ 'word':words, 'count':len(list), 'dict':worddict})