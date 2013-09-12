'''
Created on Sep 12, 2013

Imports inventory data from a csv file with format
ID, price, quantity

@author: Brian
'''
from sys import stdout
from InventorySide import Inventory
import locale

if __name__ == '__main__':
    
    locale.setlocale(locale.LC_ALL, '')

    
    inventory = Inventory()
    
    #open the inventory file and put the data into a Set
    try:
        f = open('inventory.csv', 'r+')
        
        #read in each line
        eof = False
        while (not eof):
            line = f.readline().strip('\n')
            
            if (not (line == '')): #end of file not reached
                productData = list() #will store (ident, price, quantity)
                
                #separate the single line to obtain product attributes
                eol = False
                while (not eol):
                    tempTuple = line.partition(',')
                   
                    if tempTuple[2] == '':       #partition() will just return an empty string here when on final partition
                        eol = True
                        
                    #if partition returned an empty string here, our file was not formatted correctly
                    if (tempTuple[1] == '') and (not eol):
                        print('file not formatted correctly')
                        eof = True
                        break
                    productData.append(tempTuple[0])
                    line = tempTuple[2]
                #finished reading in line
                inventory.add_product(productData[0], productData[1], productData[2])         
            else:
                eof = True
        f.close()
    except IOError:
        print('file not found.')
        
    inventory.print_inventory_size()
    inventory.print_inventory()
    