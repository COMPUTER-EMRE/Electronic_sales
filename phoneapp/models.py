from django.db import models

class Phone(models.Model):
    phone_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='phone_images/', default='phone_images/default_image.jpg')
    description = models.TextField(default='Açıklama mevcut değil.')

    def __str__(self):
        return self.phone_name


class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Computer(models.Model):
    computer_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='computer_images/', default='computer_images/default_image.jpg')
    description = models.TextField(default='Açıklama mevcut değil.')

    def __str__(self):
        return self.computer_name

class Tablet(models.Model):
    tablet_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='tablet_images/', default='tablet_images/default_image.jpg')
    description = models.TextField(default='Açıklama mevcut değil.')

    def __str__(self):
        return self.tablet_name
    
class Earphones(models.Model):
    earphones_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='earphones_images/', default='earphones_images/default_image.jpg')
    description = models.TextField(default='Açıklama mevcut değil')

    def __str__(self):
        return self.earphones_name
    
class NewRealeses(models.Model):
    newrealeses_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='newrealeses_images/', default='newrealeses_images/default_image.jpg')
    description = models.TextField(default='Açıklama mevcut değil')