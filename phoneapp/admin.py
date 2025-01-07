from django.contrib import admin
from .models import Phone, About, Computer, Tablet, Earphones, NewRealeses

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone_name', 'price', 'discount_price', 'image', 'description')
    search_fields = ('phone_name', 'description')

admin.site.register(Phone, PhoneAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')
    search_fields = ('title', 'content')

admin.site.register(About, AboutAdmin)

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('computer_name', 'price', 'discount_price', 'image', 'description')
    search_fields = ('computer_name', 'description')

admin.site.register(Computer, ComputerAdmin)

class TabletAdmin(admin.ModelAdmin):
    list_display = ('tablet_name', 'price', 'discount_price', 'image', 'description')
    search_fields = ('tablet_name', 'description')

admin.site.register(Tablet, TabletAdmin)

class EarphonesAdmin(admin.ModelAdmin):
    list_display = ('earphones_name', 'price', 'discount_price', 'image', 'description')
    search_fields = ('earphones_name', 'description')

admin.site.register(Earphones, EarphonesAdmin)

class NewrealesesAdmin(admin.ModelAdmin):
    list_display = ('newrealeses_name', 'price', 'discount_price', 'image', 'description')
    search_fields = ('newrealeses_name', 'description')

admin.site.register(NewRealeses, NewrealesesAdmin)