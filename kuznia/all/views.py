from django.shortcuts import render, redirect , get_object_or_404 , Http404
from .models import *
from .forms import *

def order_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)
    quantity = int(request.POST.get('quantity', 1))
    total_price = product.price * quantity
    try:
        order = Order.objects.get(session=session, product=product)
        order.quantity += quantity
        order.total_price += total_price
        order.save()
    except Order.DoesNotExist:
        order = Order.objects.create(session=session, image=product.images.first().image, product=product, quantity=quantity,
                                     total_price=total_price)

    return redirect('cart_view')




def cart_view(request):
    orders = Order.objects.filter(session_id=request.session.session_key)
    total_price = sum(order.total_price for order in orders)
    return render(request, 'cart_view.html', {'orders': orders, 'total_price': total_price})

def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})


def singly(request , some_parameter):
    context = Product.objects.get(id = some_parameter)
    return render(request , 'post_pages.html' , {'info' : context})

#
# def f(request):
#     session_key = request.session.session_key
#     session = Session.objects.get(session_key=session_key)
#     order = Order.objects.filter(session = session)
#     res = []
#     total_price = sum(orders.total_price for orders in order)
#     for i in order:
#         res.append(f"{i.product} - {i.quantity} штук = {i.total_price}")
#     res.append(f'Общая сумма {total_price}')
#     context = Cart.objects.create(session = session , products = res)
#     return render(request, 'all_products.html')



# def orders_post(request):
#     if request.method == 'POST':
#         form = orders_form(request.POST)
#         if form.is_valid():
#             try:
#                 session = Session.objects.get(session_key=request.session.session_key)
#                 branch_number = form.cleaned_data.get('branch_number')
#                 first_name = form.cleaned_data.get('first_name')
#                 last_name = form.cleaned_data.get('last_name')
#                 patronymic = form.cleaned_data.get('patronymic')
#                 phone_number = form.cleaned_data.get('phone_number')
#                 Orders_dispatch.objects.create(session = session, branch_number =branch_number , first_name=first_name , last_name=last_name , patronymic = patronymic , phone_number = phone_number)
#                 return redirect('/complite')
#             except:
#                 return redirect('/error')
#     else:
#         form = orders_form()
#     context = {
#         'form' : form,
#     }
#     return render(request , 'orders_client.html' , context)


def orders_post(request):
    if request.method == 'POST':
        form = orders_form(request.POST)
        if form.is_valid():
            try:
                session = Session.objects.get(session_key=request.session.session_key)
                branch_number = form.cleaned_data.get('branch_number')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                patronymic = form.cleaned_data.get('patronymic')
                phone_number = form.cleaned_data.get('phone_number')
                country = form.cleaned_data.get('country')
                city = form.cleaned_data.get('city')

                # Создаем Orders_dispatch
                order = Orders_dispatch.objects.create(session=session, branch_number=branch_number,
                                                       first_name=first_name, last_name=last_name,
                                                       patronymic=patronymic, phone_number=phone_number , country = country , city = city)

                order_finall = Order.objects.filter(session=session)
                res = []
                total_price = sum(orders.total_price for orders in order_finall)
                for i in order_finall:
                    res.append(f"{i.product} - {i.quantity} штук = {i.total_price}")
                res.append(f'Общая сумма {total_price}')

                # Создаем связанный объект Cart
                cart = Cart.objects.create(product_orders=order, session=session, products=res)

                orders_to_delete = Order.objects.filter(session = session)

                # Удалить объекты
                orders_to_delete.delete()

                return redirect('/complete')
            except:
                return redirect('/error')
    else:
        form = orders_form()
    context = {
        'form': form,
    }
    return render(request, 'orders_client.html', context)




def complete(request):
    return render(request, 'complete.html')


def base(request):
    try:
        session = Session.objects.get(session_key=request.session.session_key)
        Orders = Order.objects.filter(session = session)
        b = len(Orders)
    except:
        b = 0
    categories = Categories.objects.all()
    tg_search = request.GET.get('search', '')

    if tg_search:
        products = Product.objects.filter(name__icontains=tg_search)
    else:
        products = Product.objects.all()

    context = {
        'categories': categories,
        'products': reversed(products),
        'search_query': tg_search,  # передаем обратно строку поиска для отображения в шаблоне
        'len_order' : b,
    }
    print(Image.objects.all())
    return render(request, 'base.html', context)


# def show_categories(request , categories):
#     try:
#         bd_post = Categories.objects.get(categories=categories)
#         # Дальнейшая обработка, если объект найден
#         res = bd_post.categor.all()
#         context = {'res' : res}
#         return render(request , 'categories.html' , context)
#     except:
#         # Обработка случая, когда объект не был найден
#         raise Http404("Categories does not exist")


def show_categories(request, categories):
    session = Session.objects.get(session_key=request.session.session_key)
    Orders = Order.objects.filter(session=session)
    categories_all = Categories.objects.all()
    try:
        category = Categories.objects.get(categories=categories)
        parent_category = category.parent
        related_categories = category.children.all()

        all_categories = [category]
        if related_categories:
            all_categories.extend(related_categories)

        products = Product.objects.filter(categories__in=all_categories)

        context = {
            'categories':categories_all , #для отображения всех категорий
            'category': category, #для получения категории
            'parent_category': parent_category,
            'related_categories': related_categories,
            'products': reversed(products),
            'len_order' : len(Orders),
        }
        return render(request, 'categories.html', context)
    except Categories.DoesNotExist:
        raise Http404("Category does not exist")


def delete(request , order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('/cart')





def test(request):
    return render(request , 'test.html')