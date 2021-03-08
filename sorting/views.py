from django.shortcuts import render

def sorting(request):
    ''' Render sorting page '''
    template = "sorting/sorting.html"
    return render(request, template)
