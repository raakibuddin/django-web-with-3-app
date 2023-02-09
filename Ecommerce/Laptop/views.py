from django.shortcuts import render

# Create your views here.
def laptop (request):
    return render(request, 'laptop/laptop.html')
