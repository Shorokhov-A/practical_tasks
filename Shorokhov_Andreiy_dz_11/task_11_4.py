class Storage:
    def __init__(self):
        self.storage_db = {}
        self.send_prods = {}
        self.eq_name_amount = {}

    def add_prod(self, item, amount=1):
        eq_count = {}
        self.eq_name_amount.setdefault(item.eq_name, 0)
        self.eq_name_amount[item.eq_name] = self.eq_name_amount[item.eq_name] + amount
        eq_count[item.eq_name] = self.eq_name_amount[item.eq_name]
        self.storage_db.setdefault(item.eq_class, {}).\
            setdefault(item.eq_type, {}).update(eq_count)
        return self.storage_db

    def send_prod(self, item, amount=1):
        eq_to_send = {}
        eq_count = {}
        eq_to_send.setdefault(item.eq_name, 0)
        self.item_amount_check(item.eq_name, amount)
        self.eq_name_amount[item.eq_name] = self.eq_name_amount[item.eq_name] - amount
        eq_to_send[item.eq_name] = eq_to_send[item.eq_name] + amount
        eq_count[item.eq_name] = self.eq_name_amount[item.eq_name]
        self.storage_db.setdefault(item.eq_class, {}). \
            setdefault(item.eq_type, {}).update(eq_count)
        eq_count[item.eq_name] = eq_to_send[item.eq_name]
        self.send_prods.setdefault(item.eq_class, {}). \
            setdefault(item.eq_type, {}).update(eq_count)
        return self.send_prods

    @property
    def to_send(self):
        return self.send_prods

    def item_amount_check(self, item, value):
        if self.eq_name_amount[item] < value:
            raise ValueError(f'{item} amount out of range.')

    def __str__(self):
        return f'{self.storage_db}'


class OfficeEquipment:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    @property
    def eq_class(self):
        return self.__class__.__name__

    @property
    def eq_name(self):
        return self.name

    def __str__(self):
        return f'{self.brand} {self.name}'


class Printer(OfficeEquipment):
    def __init__(self, name, brand, printer_type):
        super().__init__(name, brand)
        self.printer_type = printer_type

    @property
    def eq_type(self):
        return self.printer_type


class Scanner(OfficeEquipment):
    def __init__(self, name, brand, scanner_type):
        super().__init__(name, brand)
        self.scanner_type = scanner_type

    @property
    def eq_type(self):
        return self.scanner_type


class Copier(OfficeEquipment):
    def __init__(self, name, brand, copier_func):
        super().__init__(name, brand)
        self.copier_func = copier_func

    @property
    def eq_type(self):
        return self.copier_func


if __name__ == '__main__':
    storage = Storage()
    prod_1 = Printer('OfficeJet Pro 88420', 'HP', 'jet printer')
    prod_2 = Scanner('ScanJet Pro 3500', 'HP', 'flatbed scanner')
    prod_3 = Copier('WorkCentre 3025V NI', 'Xerox', 'copier/fax')
    prod_4 = Printer('LaserJet 107w', 'HP', 'laser printer')
    prod_5 = Copier('WorkCentre 3025V_BI', 'Xerox', 'copier')
    prod_6 = Scanner('ScanMate i940', 'Kodak', 'yarn scanner')
    storage.add_prod(prod_1, 3)
    storage.add_prod(prod_3, 2)
    storage.add_prod(prod_2)
    storage.add_prod(prod_4)
    storage.add_prod(prod_5)
    storage.add_prod(prod_6)
    print(storage)
    try:
        storage.send_prod(prod_1, 2)
        storage.send_prod(prod_3, 3)
    except ValueError as e:
        print(f'ERROR: {e}')
    finally:
        print(storage)
        print(storage.to_send)
