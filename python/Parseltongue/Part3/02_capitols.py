# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_capitols.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/17 21:38:06 by szheng            #+#    #+#              #
#    Updated: 2019/04/20 11:08:43 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

capitols = {}

with open('capitols.txt') as f:
    for line in f:
        (key, val) = line.rstrip('\n').split(',')
        capitols[key] = val

while 1:
    user_input = input("Ready: ")
    if user_input == "Done":
        break
    for key, val in capitols.items():
        if user_input == val:
            print(key)
        elif user_input == key:
            print(val)
    if user_input not in capitols and user_input not in capitols.values():
        print("nil")
"""
    for key in capitols:
        if user_input == key:
            print(capitols[key])
        elif user_input == capitols[key]:
            print(key)

    if user_input in capitols:
        print(capitols[user_input])
"""
