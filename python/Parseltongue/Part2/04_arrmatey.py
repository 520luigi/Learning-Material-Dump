# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    04_arrmatey.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/05 16:42:07 by szheng            #+#    #+#              #
#    Updated: 2018/10/17 15:36:39 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

length = len(sys.argv)
i = 0

while (i < length):
    print("Argv of", i, "is", sys.argv[i])
    i += 1

sortit = sys.argv
sortit.sort(key=len, reverse=True)

for element in sortit:
    print(element)

