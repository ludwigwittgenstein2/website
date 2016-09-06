#Take a User Request and give them back something
#99% User will request a webpage
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is music app")

# Create your views here.
