from bd import *

class Products:
    def __init__(self , prod , price):
        self.prod = prod
        self.price = price
        self.convert_product = dict(zip(self.prod , self.price))


    def convert_product(self):
        return dict(zip(self.prod , self.price))


class Braslet:
    counter = 0

    def __init__(self):
        Braslet.counter += 1
        self.number_braslet = Braslet.counter
        self.buy_product = []
        self.sum = 0
        self.cool = True


    def buy_something(self):
        products= Products(['мясо' , 'рыба'] , [10 , 11])
        while True:
            take = str(input('Что вы хотите преобрести?\nЕсли уже все взяли , для выхода нажмите 0\n'))
            if take == '0':
                break
            else:
                if take in products.convert_product.keys():
                    self.sum += products.convert_product.get(take)
                    self.buy_product.append(take)
                    self.cool = False


    def examination(self):
        while self.cool == False:
            print(f'{self.number_braslet}     На браслете неуплата на сумму {self.sum} за такие товары как {self.buy_product}')
            a = int(input("Введите номер карты для оплаты данной суммы"))
            if len(str(a)) == 10:
                break
        self.cool = True
        return 'На браслете нету задолжности , можете проходить'




b = Braslet()
b1 = Braslet()
b1.buy_something()
b.buy_something()
print(b1.examination())
print(b.examination())