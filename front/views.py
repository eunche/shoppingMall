from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def index(request) :
    posts = Post.objects.all()

    return render(request, 'index.html',{'posts':posts})

def bottom(request) :
    bottoms = Post.objects.filter(category=3)

    return render(request, 'bottom.html',{'bottoms':bottoms})

def cap(request) :
    caps = Post.objects.filter(category=1)

    return render(request, 'cap.html',{'caps':caps})

def outer(request) :
    outers = Post.objects.filter(category=5)

    return render(request, 'outer.html',{'outers':outers})

def shoe(request) :
    shoes = Post.objects.filter(category=2)

    return render(request, 'shoe.html',{'shoes':shoes})

def top(request) :
    tops = Post.objects.filter(category=4)

    return render(request, 'top.html',{'tops':tops})

def search(request):
    try:
        global get
        get = request.GET['search']
    except MultiValueDictKeyError:
        pass
    title = Post.objects.filter(title__contains=get).order_by('-id')
    results = []
    for object in title:
        results.append(object)

    return render(request,'search.html',{'results':results,'get':get})

def detail(request, product_id):
    product = get_object_or_404(Post, pk=product_id)
    category = product.category
    color_option = []
    size_option = []

    if(category==1):
        color_option.append("one color")
        size_option.append("FREE")
    elif(category==2):
        color_option.append("one color")
        size_option.extend(["220","225","230","235","240","245","250","255","260","265","270","275","280"])
    elif(category==3):
        color_option.append("one color")
        size_option.extend(["S","M","L"])
    elif(category==4):
        color_option.append("one color")
        size_option.extend(["S","M","L"])
    elif(category==5):
        color_option.extend(["one color"])
        size_option.extend(["S","M","L"])


    return render(request, 'detail.html', {'product':product,'color_option':color_option,'size_option':size_option})