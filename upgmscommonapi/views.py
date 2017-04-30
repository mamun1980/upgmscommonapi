from django.shortcuts import render

def Home(request):
    title = "Surma Union"
    return render(request, 'index.html',{"title": title})