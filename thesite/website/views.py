from django.shortcuts import render
from django.http import HttpResponse
def post_list(request):
    return render(request, 'website/post_list.html', {})

def index(request):
    return HttpResponse("<h2>HEY!</h2>")
