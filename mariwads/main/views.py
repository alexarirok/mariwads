from django.shortcuts import render, redirect


def home(request):
    template = 'main/home.html'
    return render(request, template, { })



