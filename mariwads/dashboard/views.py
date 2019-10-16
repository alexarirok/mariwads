from django.shortcuts import render

def index(request):
    template = 'dash/base.html'
    return render(request, template, { })
