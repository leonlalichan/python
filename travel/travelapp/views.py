
from django.shortcuts import render
from . models import Place
# Create your views here
def demo(request):
    obj=Place.objects.all()
   
    return render(request,"index.html",{'result':obj})

#def add(request):
 #   x = int(request.GET['num1'])
#    y = int(request.GET['num2'])
 #   result = x + y
  #  return render(request,"about.html",{'result':result})


