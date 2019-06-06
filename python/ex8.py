# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex8.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/29 20:39:39 by szheng            #+#    #+#              #
#    Updated: 2018/07/29 20:39:56 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
