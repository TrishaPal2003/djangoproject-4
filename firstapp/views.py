from django.shortcuts import render

# Create your views here.

def index1(request):
    return render(request,'firstapp/index.html')
    return render(request,'index.html')



