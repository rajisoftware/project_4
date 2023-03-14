from django.shortcuts import render

# Create your views here.
def chitra(request):
    return render(request,'chitra.html',context={'name':'chitra','points':100})
def subramanyam(request):
    return render(request,'subramanyam.html',context={'name':'subramanyam','points':100})
