from django.shortcuts import render, redirect
from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort')
    phones_objects = Phone.objects.all()

    if sort_pages == 'max_price':
        phones_objects = phones_objects.order_by('price').reverse()
    elif sort_pages == 'min_price':
        phones_objects = phones_objects.order_by('price')
    elif sort_pages == 'name':
        phones_objects = phones_objects.order_by('name')

    context = {'phones': phones_objects,
               }
    return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context=context)

# def index(request):
#     return redirect('catalog')
#
# def show_catalog(request):
#     template = 'catalog.html'
#     sort_by = request.GET.get('sort')
#     print(sort_by)
#     if sort_by == 'name':
#         context = {
#             'phones': Phone.objects.order_by('name').all()
#         }
#     elif sort_by == 'min_price':
#         context = {
#             'phones': Phone.objects.order_by('price').all()
#         }
#     elif sort_by == 'max_price':
#         context = {
#             'phones': Phone.objects.order_by('-price').all()
#         }
#     else:
#         context = {
#             'phones': Phone.objects.order_by('id').all()
#         }
#     #print(context)
#
#     return render(request, template, context)
#
#
# def show_product(request, slug):
#     template = 'product.html'
#     print('slug: ', slug)
#     context = {
#         'phones': Phone.objects.filter(slug__contains=slug)
#     }
#     #print(context)
#     return render(request, template, context)

#
# def show_catalog(request):
#     template = 'catalog.html'
#     context = {}
#     return render(request, template, context)
#
#
# def show_product(request, slug):
#     template = 'product.html'
#     context = {}
#     return render(request, template, context)
