from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import HotDisplay

def index(request):
    return redirect(reverse(HotDisplay.HOT_URL_NAME))
