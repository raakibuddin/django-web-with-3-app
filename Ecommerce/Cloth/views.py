from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cloth(request):
    category1 = ' Cloth category1'
    category2 = ' Cloth category2'
    category_details = {'c1' : category1, 'c2' : category2}
    return render(request, 'cloth/cloth.html', category_details)
