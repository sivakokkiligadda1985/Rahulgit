from django.shortcuts import render
from django.http import HttpResponse
from main.models import Company

# Create your views here.


def companies_view(request):
    return render(request, 'companies.html', {"companies": Company.objects.all()})
