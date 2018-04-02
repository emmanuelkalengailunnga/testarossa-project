from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'pub': 'Tata as-tu ta Toyota?'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist)})

def about(request):
    return render(request, 'about.html', {'title': 'Much to do about ado'})
