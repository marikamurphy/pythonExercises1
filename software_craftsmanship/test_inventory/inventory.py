#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from io import open
from glob import glob
import os


def find_log_files(directory, pattern):
    return glob(os.path.join(directory, pattern))

def create_display_table(inventory, col_width=15):
    col_width = int(col_width)
    table_template = "{name:^{w}.{w}s}|{number:^{w}.{w}s}"
    table = []
    table.append(table_template.format(w=col_width, name="Part Name", number="Count"))
    table.append('|'.join(['-' * col_width] * 2))
    for key, value in inventory.items():
        table.append(table_template.format(w=col_width, name=key, number=str(value)))
    return '\n'.join(table)

def log_from_string(text):
    log = []
    for transaction in text.strip().splitlines():
        split_transaction = transaction.split()
        if len(split_transaction) != 2:
            print("'{}' is not a valid record".format(transaction))
        else:
            part_name = split_transaction[0]
            order_size = int(split_transaction[1])
            log.append({'part_name': part_name, 'order_size': order_size})
    return log

def update_inventory(log, inventory):
    inventory = dict(inventory)
    for transaction in log:
        part_name = transaction['part_name']
        order_size = transaction['order_size']
        inventory[part_name] = inventory.get(part_name, 0) + order_size
    return inventory

def calculate_final_inventory(logfile_directory, logfile_pattern):
    inventory = {}
    for log_file in find_log_files(logfile_directory, logfile_pattern):
        with open(log_file, 'r', encoding='utf-8') as f:
            log = log_from_string(f.read())
        inventory = update_inventory(log=log, inventory=inventory)
    return create_display_table(inventory)


if __name__ == '__main__':
    print(calculate_final_inventory('data', '*.log'))
