#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 23:08:11 2018

@author: aghoshal
"""

from utilsRestFind import readcsv
from transformUtil import saveList, searchRestaurants

def find_open_restaurants(csv_filename, search_datetime):
    list_final = []
    a = readcsv(csv_filename)
    list_final = saveList(a)
    restList = searchRestaurants(list_final, search_datetime)
    return restList

if __name__ == '__main__':
    csv_filename = '/Users/aghoshal/Desktop/restaurant.csv'
    search_datetime = '2018-10-29 00:40:06.197134'
    print find_open_restaurants(csv_filename, search_datetime)