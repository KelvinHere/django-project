from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    ''' Renders home page '''
    return HttpResponse('hihi')