from django.db import models
from datetime import datetime
from datetime import date
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

class Categories(models.Model):
    categories = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.categories



class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Product(models.Model):
    categories = models.ForeignKey(Categories, related_name='categor', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ManyToManyField(Image, blank=True)
    data = models.DateField('Дата публикации' , default = datetime.now)
    description = models.TextField('Описание')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def formatted_price(self):
        return f"{self.price} UAH"

# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     # Другие поля заказа, такие как данные покупателя и т.д.
#
#     def str(self):
#         return f"Order #{self.id} - {self.product.name}"








class Order(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='image/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)



class Orders_dispatch(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество' , max_length=50)
    branch_number = models.CharField('Номер отделения' , max_length=50 ,default=1 ,  blank=False)
    phone_number = models.CharField('Номер телефона' , max_length=50)
    my_checkbox = models.BooleanField(default=False)
    country = models.CharField('Страна' , max_length=50)
    city = models.CharField('Город' , max_length=50)



class Cart(models.Model):
    product_orders = models.ForeignKey(Orders_dispatch, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    products = models.TextField(max_length=1000)

    # def save(self, *args, **kwargs):
    #     super(Cart, self).save(*args, **kwargs)
    #     try:
    #         # Ваша логика создания Cart после сохранения
    #         Cart.objects.create(product_orders=self.product_orders, session=self.session)
    #     except Exception as e:
    #         # Обработка ошибок, если что-то пошло не так
    #         print(f"Error creating Cart: {e}")


class Test(models.Model):
    c = models.CharField(max_length=100)
