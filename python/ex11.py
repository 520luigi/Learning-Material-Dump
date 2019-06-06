# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex11.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/29 21:21:47 by szheng            #+#    #+#              #
#    Updated: 2018/07/29 21:21:49 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("How old are you in years?", end=' ')
age = input()
print("How tall are you in inches?", end=' ') #space in end leaves the amount after inches?
height = input()
print("How much do you weight in lbs?", end=' ')
weight = input()

print(f"So, you're {age} years old, {height} inches all, and {weight} pounds.")

#if you add spaces before and after input of numbers, they are included in input
