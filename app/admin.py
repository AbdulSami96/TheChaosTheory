from django.contrib import admin
from app.models import contactdetails
from app.models import Product
from app.models import productinfo
from app.models import review



# Register your models here.
 
admin.site.register(contactdetails)
admin.site.register(Product)
admin.site.register(productinfo)
admin.site.register(review)


