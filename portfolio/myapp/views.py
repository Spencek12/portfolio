from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    my_var = "This is the way!"
    context = {'my_var': my_var}
    return render(request, 'index.html', context)
