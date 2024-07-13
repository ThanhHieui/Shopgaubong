from django.contrib import admin
from.models import *
# Register your models here.
admin.site.register(Sanpham)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ThongTinKhachHang)


















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
    #address: địa chỉ
    #cyti: thanh_pho
    # state: tinh_thanh
    # mobile: so_dien_thoai