from django.shortcuts import render

def home(request):
    return render(request, 'base.html')
def home_1(request):
    return render(request, 'base_1.html')