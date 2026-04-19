from uuid import uuid4

import uuid

class Store:
    def __init__(self):
        self.catalog = {}
        self.cart = []
        self.orders = {}
    
    def add_product(self, product):
        self.catalog[product['id']] = product.copy()
        return self.catalog
    
    def get_product_by_id(self, product_id):
        return self.catalog.get(product_id)
    
    def remove_product(self, product_id):
        self.catalog.pop(product_id, None)
        return self.catalog
    
    def add_to_cart(self, product_id, quantity):
        product = self.catalog.get(product_id)
        if not product:
            return self.cart
        
        for item in self.cart:
            if item['id'] == product_id:
                item['quantity'] += quantity
                return self.cart
        
        self.cart.append({
            'id': product['id'],
            'name': product['name'],
            'price': product['price'],
            'quantity': quantity
        })
        return self.cart
    
    def place_order(self):
        if not self.cart:
            return self.cart, self.orders
        
        total_amount = sum(item['price'] * item['quantity'] for item in self.cart)
        order_id = str(uuid.uuid4())
        
        self.orders[order_id] = {
            'id': order_id,
            'items': self.cart.copy(),
            'total_amount': total_amount
        }
        
        self.cart = []
        return self.cart, self.orders


def add_product(catalog, product):
    store = Store()
    store.catalog = catalog
    store.add_product(product)
    return store.catalog


def get_product_by_id(catalog, product_id):
    return catalog.get(product_id)


def remove_product(catalog, product_id):
    new_catalog = catalog.copy()
    new_catalog.pop(product_id, None)
    return new_catalog


def add_to_cart(catalog, cart, product_id, quantity):
    product = catalog.get(product_id)
    if not product:
        return cart
    
    new_cart = cart.copy()
    for item in new_cart:
        if item['id'] == product_id:
            item['quantity'] += quantity
            return new_cart
    
    new_cart.append({
        'id': product['id'],
        'name': product['name'],
        'price': product['price'],
        'quantity': quantity
    })
    return new_cart


def place_order(cart, order):
    if not cart:
        return cart.copy(), order.copy()
    
    total_amount = sum(item['price'] * item['quantity'] for item in cart)
    order_id = str(uuid.uuid4())
    
    new_order = order.copy()
    new_order[order_id] = {
        'id': order_id,
        'items': cart.copy(),
        'total_amount': total_amount
    }
    
    return [], new_order

