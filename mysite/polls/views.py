from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello PY 118!")


def return_simple_html(request): 
    blog_entries = \
        [{"title": "Klopotenko",
         "body": "receipies"}]


    return render(request, 'child.html', 
                  context={"blog_entries":blog_entries})
