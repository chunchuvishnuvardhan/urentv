from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import ForeignKey

itemchoices = (
    ("Cameras", "Cameras"),("Clothes","Clothes"),("Shoes","Shoes"),("Chappals","Chappals"),("Syndles","Syndles"), ("Vehicles","Vehicles"), ("Spectacles","Spectacles"), ("Home Appliances","Home Appliances"),("Electronics","Electronics"),("Other","Other")

)


class Product(models.Model):
    product_id=models.AutoField
    category = models.CharField(max_length=20, choices=itemchoices, default='Cameras')
    itemname = models.CharField(max_length=30)
    itemrentperday = models.IntegerField()
    itemowner = models.CharField(max_length=30)
    itemcolour = models.CharField(max_length=30)
    itempic = models.ImageField(upload_to="newapp/images")
    whatsappno = models.CharField(max_length=15)
    whatsappno2=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
    adress = models.CharField(max_length=302)
    desc = models.TextField(max_length=200,default="")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.category




class Feedback(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    feedback=models.TextField(max_length=200)
    def __str__(self):

        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address1 = models.CharField(max_length=111)
    address2 = models.CharField(max_length=111, default="")
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111)


class contact(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField(max_length=300)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_valid = None

    def __str__(self):
        return self.name
