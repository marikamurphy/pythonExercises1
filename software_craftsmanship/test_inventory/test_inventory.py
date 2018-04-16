#!/usr/bin/env python
#-*- encoding:utf-8 -*-

"""
This module contains four unit tests and one integration test whose purpose is
to validate the functions inside of inventory.py. Currently, the tests all
fail because they are asserting False. Your task is to replace these assert
statements with ones that will test for correct behavior under normal
circumstances, and for common edge cases. For numbers, common edge cases
include 0 and -1. For containers, common edge cases include being empty.
"""

import os
import pytest
import shutil

import inventory as module

blank_log = ""
empty_log = "  \n  \n  \n"
bad_log = " too many things\n on each new line"
good_log = "frombicator 10\nfrombicator -5"
empty_output = """   Part Name   |     Count     \n---------------|---------------"""
good_output = """   Part Name   |     Count     \n---------------|---------------\n  frombicator  |       5       """

@pytest.fixture(scope='function')
def write_directory():
    """This fixture puts a temporary data directory on disk to be written
    to and read from in the `test_calculate_final_inventory` function below
    """
    test_directory = 'test_dir'
    test_file = 'test_file.fake'
    if os.path.isdir(test_directory):
        raise OSError("Temporary directory already exists")
    if os.path.isfile(test_file):
        raise OSError("Temporary file already exists")
    os.mkdir(test_directory)
    yield test_directory, test_file
    shutil.rmtree(test_directory)

def test_find_log_files():
    """Make sure this function behaves properly when there are no log files"""
    assert len(module.find_log_files('..','*'))>0
    assert module.find_log_files('..', '|:<>/\\') == []

def test_create_display_table():
    """Make sure this function correctly handles inventories, whether they are
    filled or empty"""
    output = module.create_display_table({}, col_width=4)
    assert output == 'Part|Coun\n----|----'
    output = module.create_display_table({'one':1}, col_width=5)
    assert output == 'Part |Count\n-----|-----\n one |  1  '

def test_log_from_string():
    """Make sure this function correctly handles log files, badly formatted
    log files and empty log files """
    data = ""
    output = module.log_from_string(data)
    assert output == []
    data = "one    11\ntwo    22"
    output = module.log_from_string(data)
    assert output == [
        {'part_name': 'one', 'order_size': 11},
        {'part_name': 'two', 'order_size': 22}
    ]
    data = " a hot mess "
    output = module.log_from_string(data)
    assert output == []

def test_update_inventory():
    """Make sure this function behaves properly for normal containers and
    empty containers"""
    data = [{'part_name': 'one', 'order_size': 1}]
    output = module.update_inventory(data, {})
    assert output == {'one' : 1}
    data = [{'part_name': 'one', 'order_size': 1}]
    output = module.update_inventory(data, {'one': -1})
    assert output == {'one' : 0}
    data = []
    output = module.update_inventory(data, {'one': 1})
    assert output == {'one': 1}

def test_calculate_final_inventory(write_directory):
    """Make sure this function behaves properly for normal files, empty
    files, and files with bad records"""
    test_directory, test_file = write_directory
    test_text = [blank_log, empty_log, bad_log, good_log]
    expected_result = [empty_output, empty_output, empty_output, good_output]
    for text, result in zip(test_text, expected_result):
        with open(os.path.join(test_directory, test_file), 'w') as f:
            f.write(text)
        output = module.calculate_final_inventory(test_directory, test_file)
        assert output == result
