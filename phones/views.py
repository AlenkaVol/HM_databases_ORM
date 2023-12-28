from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    if sort == 'name':
        phones = Phone.objects.order_by('name')
        context = {'phones': phones}
        return render(request, template, context)
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
        context = {'phones': phones}
        return render(request, template, context)
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price',)
        context = {'phones': phones}
        return render(request, template, context)
    else:
        phones = Phone.objects.all()
        context = {'phones': phones}
        return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
