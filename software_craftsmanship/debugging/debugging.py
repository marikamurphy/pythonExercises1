#!/usr/bin/env python
#-*- encoding:utf-8 -*-

"""
This exercise contains several bugs. Use the output from the logging messages
to diagnose the problem and change the code to handle it. If you're stumped,
try using '%run -p debugging.py' in IPython to enter the python debugger at the
level of the exception.
"""

from glob import glob
from io import open
import logging
import os


logging.basicConfig(filename='debug.log', level=logging.DEBUG)

def find_log_files(directory, pattern):
    root=os.path.dirname(__file__)
    file_list = glob(os.path.join(root,directory, pattern))
    logging.debug("found log files: {}".format(file_list))
    return file_list

def create_display_table(inventory, col_width=15):
    col_width = int(col_width)
    table_template = "{name:^{w}.{w}s}|{number:^{w}.{w}s}"
    table = []
    table.append(table_template.format(w=col_width, name="Part Name", number="Count"))
    table.append('|'.join(['-' * col_width] * 2))
    for key, value in inventory.items():
        logging.debug("adding key: {}, value: {}".format(key, value))
        table.append(table_template.format(w=col_width, name=key, number=str(value)))
    return '\n'.join(table)

def log_from_string(text):
    log = []
    for transaction in text.strip().lower().splitlines():
        logging.debug("found transaction: '{}'".format(transaction))
        split_transaction = transaction.split()
        if(len(split_transaction)!=2):
            logging.warning("'{}' is not a valid record".format(transaction))
        else:  
            part_name = split_transaction[0]
            order_size = float(split_transaction[1])
            log.append({'part_name': part_name, 'order_size': order_size})
    return log

def update_inventory(log, inventory):
    inventory = dict(inventory)
    for transaction in log:
        part_name = transaction['part_name']
        order_size = transaction['order_size']
        inventory[part_name] = inventory.get(part_name, 0) + order_size
        logging.debug("updated inventory to: {}".format(inventory))
    return inventory

def calculate_final_inventory(logfile_directory, logfile_pattern):
    logging.info('starting calculate_final_inventory')
    inventory = {}
    for log_file in find_log_files(logfile_directory, logfile_pattern):
        with open(log_file, 'r', encoding='utf-8') as f:
            log = log_from_string(f.read())
        inventory = update_inventory(log=log, inventory=inventory)
    table = create_display_table(inventory)
    logging.info('finishing calculate_final_inventory')
    return table


if __name__ == '__main__':
    print(calculate_final_inventory('data', '*.log'))
