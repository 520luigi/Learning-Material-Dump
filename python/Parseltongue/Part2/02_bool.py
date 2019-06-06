# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_bool.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/05 15:50:55 by szheng            #+#    #+#              #
#    Updated: 2018/10/05 16:08:45 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

L1 = [False,True,True,None,True,None,None,False,False,None,True,False]
L2 = ["or","or","or","==","!=","==","and","==","!=","and","==","or"]
L3 = [False,False,None,None,True,True,False,True,None,False,True,None]

part1 = random.choice(L1)
part2 = random.choice(L2)
part3 = random.choice(L3)
string = str(part1) + ' ' + str(part2) + ' ' + str(part3)

print(string, "=>", eval(string))
