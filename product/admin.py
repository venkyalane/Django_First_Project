from django.contrib import admin
from product.models import Product
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("product_id","product_name", "product_qty","product_prize")

admin.site.register(Product, MemberAdmin)