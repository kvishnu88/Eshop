from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0.0, null=False)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)

    def isExists(self):
        if Customer.objects.filter(email= self.email):
            return True
        return False
