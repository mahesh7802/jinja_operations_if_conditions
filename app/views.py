from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':30,'b':10}
    return render(request,'conditions.html',context=d)
