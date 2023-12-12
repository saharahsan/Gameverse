"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gameverse import views

app = "gameverse"
urlpatterns = [
    path('', views.index , name="index"),
    path("login/",views.login_view,name = "login"),
    path("signup/",views.signup_view,name = "signup"),
    path("cart/",views.cart_view,name = "cart"),
    path('add/<int:product_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart_view, name='remove_from_cart'),
    path("logout/",views.logout_view,name = "logout"),
    path("Search/",views.search,name="search"),
    path("Search/result",views.search_view,name="search_result"),
    path("category/<int:pk>/",views.Cat_Detail_View.as_view(),name="detail"),
    path("product_detail/<int:pk>/", views.Product_D_View.as_view(), name="product_detail"),
    path('admin/', admin.site.urls),
]
