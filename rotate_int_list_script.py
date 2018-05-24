#!/usr/bin/env python3
# coding: utf-8

import argparse

#method to rotate first element by shift_size
def rotate_first(int_list, shift_size):
    shift=shift_size%len(int_list)
    return int_list[1:1+shift] + int_list[0:1] + int_list[shift+1:]

#method to rotate all elements by shift_size
def rotate_all(int_list, shift_size):
    shift=shift_size%len(int_list)
    return int_list[shift:] + int_list[:shift]

#parse arguments
parser = argparse.ArgumentParser(description='Shift integer values in an integer array.')
parser.add_argument('shift_size', type=int, #nargs='+',
                   help='an integer for the shift size')
parser.add_argument('csv_int_array', help='array to shift')
args = parser.parse_args()

#print label and output
print ("Showing shift of first integer by %d:" % args.shift_size)
print (rotate(args.csv_int_array.split(","), args.shift_size))

#print label and output
print ("Showing shift of all integers by %d:" % args.shift_size)
print (rotate2(args.csv_int_array.split(","), args.shift_size))

