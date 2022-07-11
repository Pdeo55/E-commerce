from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shopping/images', default="")

    def __str__(self): 
        return self.product_name


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80, default="")
    phone_no = models.CharField(max_length=80, default="")
    comment = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name


class Orders(models.Model):
    Order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000)
    Country = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=6, default="")
    phone = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.email
