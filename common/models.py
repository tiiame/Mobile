from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Produkt(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_avaible = models.BooleanField(default=True)
    guarantee = models.CharField(max_length=255, null=True, )
    delivery = models.CharField(max_length=255, null=True, )
    pickup = models.CharField(max_length=255, null=True, )
    life_time = models.CharField(max_length=255, null=True, )
    made_by = models.CharField(max_length=255, null=True, )
    category = models.CharField(max_length=255, null=True, )

    def __str__(self):
        return self.name

class Productimage(models.Model):
    product = models.ForeignKey(Produkt, on_delete=models.CASCADE, )
    color = models.CharField(max_length=255, null=True, )
    image_1 = models.ImageField(upload_to='product_images', null=True, )
    image_2 = models.ImageField(upload_to='product_images', null=True,)
    image_3 = models.ImageField(upload_to='product_images', null=True,)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=True)

    def __str__(self):
        return self.product.name


class Productprice(models.Model):
    product = models.ForeignKey(Produkt, on_delete=models.CASCADE, )
    price = models.CharField(max_length=255, null=True,)
    memory = models.CharField(max_length=255, null=True, )

    def __str__(self):
        return self.product.name

class Productinfo(models.Model):
    product = models.ForeignKey(Produkt, on_delete=models.CASCADE, )
    key = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.product.name


class ProductinfoType(models.Model):
    name = models.CharField(max_length=255, null=True, )

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, null=True, )
    image = models.ImageField(upload_to='category_images', null=True,)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=255, null=True, )
    Price = models.CharField(max_length=255, null=True, )
    time = models.CharField(max_length=255, null=True, )
    product = models.ForeignKey(Produkt, on_delete=models.CASCADE, )

    def __str__(self):
        return self.title


class ServiceApplication(models.Model):
    sevice = models.ForeignKey(Service, on_delete=models.CASCADE, )
    full_name = models.CharField(max_length=255, null=True, )
    phone_number = models.CharField(max_length=255, null=True, )

    def __str__(self):
        return self.sevice.title

class Client(models.Model):
    image = models.ImageField(upload_to='client_images', null=True, )
    full_name = models.CharField(max_length=255, null=True,)
    position = models.CharField(max_length=255, null=True, )
    type = models.CharField(max_length=255, null=True, )

    def __str__(self):
        return self.full_name
    


































    