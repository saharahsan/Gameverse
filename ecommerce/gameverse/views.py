from typing import Any
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Catogery,Product,CartItem
from django.db.models import Q
# Create your views here.
def index(request):
    catogery = Catogery.objects.all()
    recommend_products = Product.objects.filter(
            Q(name__icontains='game of the year') | Q(description__icontains='game of the year')
        )
    return render(request,"gameverse/index.html",{"categories": catogery,"product_rec":recommend_products})

class Cat_Detail_View(generic.DetailView):
    model = Catogery
    template_name = "gameverse/category_detail.html"
    context_object_name = "category"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        catogery = Catogery.objects.all()
        context['categories'] = catogery
        return context

class Product_D_View(generic.DetailView):
    model = Product
    template_name = "gameverse/product_detail.html"
    context_object_name = "product"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        catogery = Catogery.objects.all()
        context['categories'] = catogery
        return context
    
    
def search(request):
    catogery = Catogery.objects.all()
    return render(request,"gameverse/search.html",{"categories": catogery})


def search_view(request):
    catogery = Catogery.objects.all()
    all_products = []
    query = request.GET.get('q', '') 
    if query:
        search_products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        if not search_products:
            all_products = Product.objects.all()
        return render(request, 'gameverse/search_result.html', {'products': search_products, 'query': query, 'all_products': all_products,"categories": catogery})  
    else:
        return HttpResponseRedirect(reverse('search'))

def header(request):
    catogery = Catogery.objects.all()
    return render(request,"gameverse/partials/header.html",{"object_list": catogery})

@login_required(login_url="/signup/")
def add_to_cart_view(request,product_id):
    product = Product.objects.get(id = product_id)
    cart_item,created = CartItem.objects.get_or_create(product=product,user = request.user)
    cart_item.quantity += 1
    cart_item.save()
    return HttpResponseRedirect(reverse("cart"))   

@login_required(login_url="/signup/")
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    catogery = Catogery.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request,"gameverse/cart.html",{"categories": catogery,'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart_view(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return HttpResponseRedirect(reverse("cart"))


def signup_view(request):
    if request.method =="GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return render(request,"gameverse/signup.html")
    elif request.method =="POST":
        user = User.objects.create_user(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
            email=request.POST.get("email"),
        )
        return HttpResponseRedirect(reverse('login'))

def login_view(request):
    if request.method =="GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('cart'))
        return render(request,"gameverse/signup.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            next_url = request.POST.get('next') or 'cart'
            print(next_url)
            return redirect(next_url)
        else:
            next_url=request.GET.get('next')
            return render(request,"gameverse/signup.html",{"login_message":"Username or password incorrect",'next':next_url})
      
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
        