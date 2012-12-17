# Create your views here.
from django.shortcuts import render_to_response
def create(request):
    return render_to_response('blog/create_page.html',)
