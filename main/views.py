from django.shortcuts import render

# Create your views here.
def home(request):
    ''' Renders home page '''
    template = 'main/index.html'
    return render(request, template)