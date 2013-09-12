'''
Created on Sep 12, 2013

@author: Brian
'''
from sys import stdout
import locale

class Product(object):
    '''
    A product is an item an inventory might have.
    
    A product has a price, ID, and a quantity on hand.
    '''


    def __init__(self, ident, price, quantity):
        self.price = locale.currency(float(price.strip()))
        self.ident = ident.strip()
        self.quantity = quantity.strip()
        
    def print_product (self):
        print('{} ({} each) has a quantity of {}'.format(self.ident, self.price, self.quantity))
        
class Inventory(object):
    '''
    Keeps track of various products and can sum up the inventory value
        
    '''
    
    
    def __init__(self):
        self.totalInventory = 0
        self.productList = list()
        
    def add_product(self, ident, price, quantity):
        for x in self.productList:
            if x.ident == ident:
                print('Product already in Inventory:', end ='')
                x.print_product()
        else:
            self.productList.append(Product(ident, price, quantity))
            self.totalInventory +=  int(quantity)
        
    def delete_product(self, ident):
        for x in self.productList:
            if x.ident == ident:
                del self.productList[self.productList.index(ident)]
                return True
        else:
            return False
        
    def print_inventory_size(self):
        print('Inventory has a total quantity of {}'.format(self.totalInventory))
        
    def print_inventory(self):
        for x in self.productList:
            x.print_product()
        