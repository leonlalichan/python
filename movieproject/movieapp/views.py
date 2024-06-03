from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie1
from .forms import Movie1Form

def demo(request):

    movies = Movie1.objects.all()


    context = {
        'movie_list': movies
    }

    # Render the template with the provided context
    return render(request, 'index.html', context)
def detail(request,movie_id):
    movie=Movie1.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        images = request.FILES['images']
        movie=Movie1(name=name,desc=desc,year=year,images=images)
        movie.save()

    return render(request,'add.html')
def update(request,id):
    movie=Movie1.objects.get(id=id)
    form= Movie1Form(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method == 'POST':
        movie = Movie1.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render (request,'delete.html')
