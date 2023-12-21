from django.shortcuts import render
from .models import Icon



# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')