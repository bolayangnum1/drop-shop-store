from django.shortcuts import render


def shop(request):
    return render(request, 'shop/shop.html', )


def about(request):
    return render(request, 'about.html', )


def index(request):
    return render(request, 'index.html',)
