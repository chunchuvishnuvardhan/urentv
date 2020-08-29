from django.contrib import admin
from .models import Product,contact,Orders,Feedback
# Register your models here.

admin.site.register(Product)
admin.site.register(contact)
admin.site.register(Orders)
admin.site.register(Feedback)

