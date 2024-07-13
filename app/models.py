from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
#change forms register django
#Category
class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories',null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.name

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

    
class Sanpham(models.Model):
    category = models.ManyToManyField(Category, related_name='san_pham')
    ten_San_Pham = models.CharField(max_length=200,null=True) #max_length=200: là tên tối đa là 200 ký tự, null=True: nếu người dùng không gõ từ gì
    gia = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=False)
    hinh_anh = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.ten_San_Pham
    
    @property
    def ImageURL(self):
        try:
            url = self.hinh_anh.url
        except:
            url=''
        return url
    
class Order(models.Model):
    nguoi_mua = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    ngay_dat_hang = models.DateTimeField(auto_now_add=True)
    Hoan_thanh = models.BooleanField(default=False,null=True,blank=False)
    id_khach_Hang = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.so_luong for item in orderitems])
        return total
    
class OrderItem(models.Model):
    san_pham = models.ForeignKey(Sanpham,on_delete=models.SET_NULL,blank=True,null=True)
    dat_hang = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    so_luong = models.IntegerField(default=0,null=True,blank=True)
    ngay_mua = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total = self.san_pham.gia * self.so_luong
        return total



class ThongTinKhachHang(models.Model):
    nguoi_mua = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    dat_hang = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    dia_chi = models.CharField(max_length=200,null=True)
    thanh_pho = models.CharField(max_length=200,null=True)
    tinh_thanh = models.CharField(max_length=200,null=True)
    so_dien_thoai = models.CharField(max_length=200,null=True)
    ngay_mua = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.dia_chi



    
  
    

   # class Customer: Khachhang
    #class Product: Sanpham
    # class Shipping address: ThongTinKhachHang
    #class Order: Order
    # class OrderItem: OrderItem
    #email: email
    #data_order: ngay_dat_hang
    #customer: nguoi_mua
    #order: dat_hang
    #complete: dat_hang
    #complete: Hoanthanh (khách hàng đã hoàn thành đơn hàng chưa)
    #transaction_id: id_KhachHang
    #quantity: so_luong
    #date_added: ngay_mua
    #product: san_pham
    #address: địa chỉ
    #cyti: thanh_pho
    # state: tinh_thanh
    # mobile: so_dien_thoai
    #image: hinh_anh
    #price: gia
    

    

