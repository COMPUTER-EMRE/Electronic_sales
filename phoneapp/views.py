from django.shortcuts import render
from .models import Phone, About, Computer, Tablet, Earphones, NewRealeses
from django.contrib.auth.decorators import login_required

def home(request):
    selected_brands = request.GET.getlist('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    search_query = request.GET.get('search')

    filters = {}
    
    if selected_brands:
        filters['phone_name__in'] = selected_brands

    if min_price:
        filters['price__gte'] = min_price
    if max_price:
        filters['price__lte'] = max_price
    if search_query:
        filters['phone_name__icontains'] = search_query  # Case-insensitive arama

    all_phones = Phone.objects.filter(**filters) if filters else Phone.objects.all()

    phone_dict = {"phones": all_phones, "search": search_query}
    return render(request, 'phoneapp/home.html', context=phone_dict)



@login_required(login_url="/login")
def send(request):
    return render(request, 'phoneapp/send.html')

def about(request):
    about_info = About.objects.all()
    context = {
        'about_info': about_info
    }
    return render(request, 'phoneapp/about.html', context)

def comminecation(request):
    return render(request, 'phoneapp/comminecation.html')

def basket(request):
    return render(request, 'phoneapp/basket.html')

def computer(request):
    selected_brands = request.GET.getlist('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    all_computers = Computer.objects.all()

    if selected_brands:
        all_computers = all_computers.filter(computer_name__in=selected_brands)

    if min_price:
        all_computers = all_computers.filter(price__gte=min_price)
    
    if max_price:
        all_computers = all_computers.filter(price__lte=max_price)

    computer_dict = {"computers": all_computers}
    return render(request, 'phoneapp/computer.html', context=computer_dict)

def tablet(request):
    selected_brands = request.GET.getlist('brand')  # 'brand' parametresini alır
    if selected_brands:
        # 'brand' alanına göre filtreleme yapar
        all_tablets = Tablet.objects.filter(brand__in=selected_brands)
    else:
        all_tablets = Tablet.objects.all()

    tablet_dict = {"tablets": all_tablets, "selected_brands": selected_brands}
    return render(request, 'phoneapp/tablet.html', context=tablet_dict)

def earphones(request):
    all_earphones = Earphones.objects.all()

    # Filtreleme işlemleri
    search_query = request.GET.get('search', '')
    brand_filter = request.GET.getlist('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    color_filter = request.GET.getlist('color')

    if search_query:
        all_earphones = all_earphones.filter(earphones_name__icontains=search_query)

    if brand_filter:
        all_earphones = all_earphones.filter(brand__in=brand_filter)

    if min_price:
        all_earphones = all_earphones.filter(price__gte=min_price)

    if max_price:
        all_earphones = all_earphones.filter(price__lte=max_price)

    if color_filter:
        all_earphones = all_earphones.filter(color__in=color_filter)

    context = {
        'earphones': all_earphones
    }
    return render(request, 'phoneapp/earphones.html', context)



def newrealeses(request):
    all_newrealeses = NewRealeses.objects.all()
    context = {
        'newrealeses' : all_newrealeses
    }
    return render(request, 'phoneapp/newrealeses.html', context)
