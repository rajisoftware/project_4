from django.shortcuts import render

# Create your views here.
def virat(request):
     return render(request,'virat.html',context={'name':'virat','playerno':23})
def dhoni(request):
    return render(request,'dhoni.html',context={'name':'dhoni','playerno':22})
