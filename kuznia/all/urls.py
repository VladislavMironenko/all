"""
URL configuration for testing1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Другие URL...
    path('test/' , views.test),
    path('', views.base, name='all_products'),  # URL для страницы со всеми товарами
    path('' , views.delete , name = 'delete'),
    path('order/<int:product_id>/', views.order_product, name='order_product'),  # URL для добавления товара в корзину
    path('cart/', views.cart_view, name='cart_view'),# URL для страницы корзины
    path('order/' , views.orders_post , name = 'order') ,
    path('complete/', views.complete),
    path('delete/<int:order_id>/', views.delete, name='delete'),
    path('<str:categories>/', views.show_categories, name='show_categories'),
    path('<int:some_parameter>', views.singly, name='pathing'),
    # path('done/' , views.done , name = 'done')
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)