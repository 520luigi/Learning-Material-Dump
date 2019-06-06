# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_mathclass.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/19 14:54:30 by szheng            #+#    #+#              #
#    Updated: 2018/10/19 16:34:01 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

def make_array(arguments):
    array = []
    i = 1
    while i < len(arguments):
        array.append(int(arguments[i]))
        i += 1
    return (array)

def minimum(array):
    min_value = array[0]
    for i in array:
        if i < min_value:
            min_value = i
    return (min_value)

def maximum(array):
    max_value = array[0]
    for i in array:
        if i > max_value:
            max_value = i
    return (max_value)

def mean(array):
    return (round(sum(array)/len(array), 2))

def median(array):
    n = len(array)
    if n % 2 == 1:
        return (round(sorted(array)[n//2], 2))
    else:
        return (round(sum(sorted(array)[n//2-1:n//2+1])/2.0, 2))

def mode(array):
    return (max(array, key = array.count))

def set_range(array):
    return (maximum(array) - minimum(array)) 

def main(argv):
    if len(argv) < 2:
        print("Usage: python3 01_mathclass.py <list of numbers>")
        exit(1)
    array = make_array(argv)
    print ("Min: ", minimum(array))
    print ("Max: ", maximum(array))
    print ("Mean: ", mean(array))
    print ("Median: ", median(array))
    print( "Mode: ", mode(array))
    print ("Range:", set_range(array))

main(sys.argv)
