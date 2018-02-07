#!/usr/bin/env python
#-*- encoding:utf-8 -*-

"""
Refactor Inventory
------------------

The following code represents a working solution to the inventory exercise,
with two additional features:

1. Log files are read in from disk
2. The resulting data structure is printed

Refactor this script into separate functions that can be called to process log
files and print out the final total for each part (you should end up with 4-6
functions). Keep an eye out for the following code smells:

1. Repeated code -> turn it into a single function
2. Inline comments -> turn them into names
3. Bad names -> object names should clearly describe what they do
4. Magic numbers -> replace them with named constants
5. Global objects -> encapsulate them inside functions
6. Temporal coupling -> separate ordered steps into a main block or function
"""

# Import statements
from glob import glob
from io import open
import os


def findAdditionalFiles():

    root=os.path.dirname(__file__)
    log_files=glob(os.path.join(root,'data', '*.log'))
    return log_files   
    
    
def readInventory(log_file,warehouse_log_list):
     
                
    with open(log_file, 'r', encoding='utf-8') as f:
        read_log_file = f.read()    
    for line in read_log_file.strip().splitlines(): # split string on lines
        if len(line.split()) != 2: 
            warning="{} is not valid".format(line)
            print(warning)
        else: 
            warehouse_log_list.append([line.split()[0], int(line.split()[1])]) # append line
    return warehouse_log_list
    
          
    
def displayWarehouseLog(warehouse_log_dict): 
    template = "{:^10.10s}|{:^10.10s}"
    
    log_output='\n'+template.format("Part Name", "Count")+'\n'+'|'.join(['-' * 10] * 2)
    for part_name, count in warehouse_log_dict.items():
        log_output+="\n"+template.format(part_name, str(count)) 
    log_output+="\n"

    print(log_output)
    
def updateWarehouseLog():
    warehouse_log_list = []
    warehouse_log_dict = {}
     
    for log_file in findAdditionalFiles():
        warehouse_log_list=readInventory(log_file, warehouse_log_list)
        
    for transaction in warehouse_log_list:
        warehouse_log_dict[transaction[0]] = warehouse_log_dict.get(transaction[0], 0) + transaction[1] # increment 
    
    displayWarehouseLog(warehouse_log_dict)

    
updateWarehouseLog()



             
        


    

    
