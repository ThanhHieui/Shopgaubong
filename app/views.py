from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from.models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def category(request):
    categories = Category.objects.filter(is_sub = False)
    active_category = request.GET.get('category','')
    if active_category:
        san_pham = Sanpham.objects.filter(category__slug = active_category)
    context ={'categories':categories, 'san_pham':san_pham, 'active_category':active_category}
    return render(request, 'app/category.html',context)
        
def register (request):
    form = CreateUserForm()
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context ={'form':form}
    return render(request,'app/register.html',context)
#login
def loginPage (request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username =username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request,'user hoặc password chưa đúng')
    context ={}
    return render(request,'app/login.html',context)
#logout
def logoutPage(request):
    logout(request)
    return redirect('login')
#search
def timKiem(request):
    if request.method =="POST":
        searched = request.POST["searched"]
        keys = Sanpham.objects.filter(ten_San_Pham__icontains=searched)
    if request.user.is_authenticated:
        nguoi_mua = request.user
        dat_hang, created = Order.objects.get_or_create(nguoi_mua=nguoi_mua, Hoan_thanh=False)
        items = dat_hang.orderitem_set.all()
        cartItems = dat_hang.get_cart_items
    else:
        items=[]
        dat_hang = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = dat_hang['get_cart_items']
    san_phams = Sanpham.objects.all()
    return render(request,'app/timkiem.html',{"searched": searched, "keys": keys, 'san_phams': san_phams, 'cartItems': cartItems})
#home
def home(request):
    if request.user.is_authenticated:
        nguoi_mua = request.user
        dat_hang, created = Order.objects.get_or_create(nguoi_mua=nguoi_mua, Hoan_thanh=False)
        items = dat_hang.orderitem_set.all()
        cartItems = dat_hang.get_cart_items
    else:
        items=[]
        dat_hang = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = dat_hang['get_cart_items']
    categories = Category.objects.filter(is_sub = False)
    san_phams = Sanpham.objects.all()
    context= {'categories':categories,'san_phams': san_phams, 'cartItems': cartItems}
    return render(request,'app/home.html', context)
#cart
def cart(request):
    if request.user.is_authenticated:
        nguoi_mua = request.user
        dat_hang, created = Order.objects.get_or_create(nguoi_mua=nguoi_mua, Hoan_thanh=False)
        items = dat_hang.orderitem_set.all()
        cartItems = dat_hang.get_cart_items
    else:
        items=[]
        dat_hang = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = dat_hang['get_cart_items']
    categories = Category.objects.filter(is_sub = False)
    context={'categories':categories,'items':items,'dat_hang': dat_hang, 'cartItems': cartItems}
    return render(request,'app/cart.html', context)
#checkout
def checkout(request):
    if request.user.is_authenticated:
        nguoi_mua = request.user
        dat_hang, created = Order.objects.get_or_create(nguoi_mua=nguoi_mua, Hoan_thanh=False)
        items = dat_hang.orderitem_set.all()
        cartItems = dat_hang.get_cart_items
    else:
        items=[]
        dat_hang = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = dat_hang['get_cart_items']
    categories = Category.objects.filter(is_sub = False)
    context={'categories':categories,'items':items,'dat_hang': dat_hang, 'cartItems': cartItems}
    return render(request,'app/checkout.html', context)
#update
def updateItem(request):
    try:
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        
        nguoi_mua = request.user
        san_pham = Sanpham.objects.get(id=productId)
        dat_hang, created = Order.objects.get_or_create(nguoi_mua=nguoi_mua, Hoan_thanh=False)
        orderItem, created = OrderItem.objects.get_or_create(dat_hang=dat_hang, san_pham=san_pham)
        
        if action == 'add':
            orderItem.so_luong += 1
        elif action == 'remove':
            orderItem.so_luong -= 1
        orderItem.save()
        if orderItem.so_luong <= 0:
            orderItem.delete()
        return JsonResponse('Item was added', safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def chinhsach(request):
    categories = Category.objects.filter(is_sub = False)
    context={'categories':categories}
    return render(request,'app/chinhsach.html', context)
def giatgaubong(request):
    categories = Category.objects.filter(is_sub = False)
    context={'categories':categories}
    return render(request,'app/giatgaubong.html', context)
def gioithieucuahang(request):
    categories = Category.objects.filter(is_sub = False)
    context={'categories':categories}
    return render(request,'app/gioithieucuahang.html', context)
















# class Customer: Khachhang
    #class Product: Sanpham
    # class Shipping address: ThongTinKhachHang
    #class Order: Order
    # class OrderItem: OrderItem
    #data_order: ngay_dat_hang
    #customer: nguoi_mua
    #order: dat_hang
    #complete: dat_hang
    #complete: Hoanthanh (khách hàng đã hoàn thành đơn hàng chưa)
    #transaction_id: id_KhachHang
    #quantity: so_luong
    #date_added: ngay_mua
    #product: san_pham
    #products: san_pham
    #address: địa chỉ
    #cyti: thanh_pho
    # state: tinh_thanh
    # mobile: so_dien_thoai
