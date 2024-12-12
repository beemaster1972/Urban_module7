class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __repr__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __str__(self):
        return self.__repr__()


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self) -> str:
        with open(self.__file_name, 'r+', encoding='utf-8') as file:
            return file.read()

    def add(self, *products: Product) -> None:
        list_products = self.get_products()
        for product in products:
            if str(product).split()[0] in list_products:
                print(f'{product} уже есть в магазине')
                continue
            list_products += (str(product) + '\n')
        with open(self.__file_name,'w', encoding='utf-8') as file:
            file.write(list_products)


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Carrot', 5.5, 'Vegetables')
    print(p2)  # __str__
    s1.add(p1, p2, p3)
    print(s1.get_products())

