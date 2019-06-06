# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_guess.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/17 21:09:25 by szheng            #+#    #+#              #
#    Updated: 2018/10/17 21:37:22 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import random

array = ["amaze","bliss","dream","enjoy","trust"]

word = random.choice(array)

print("The secret word begins with a " + word[0])

count = 10
while (1):
    ans = input("GUESS: ")
    if ans == "":
        print("You wasted a guess =P")
        count -= 1
    elif len(ans) < 5 or len(ans) > 5:
        print("0, 1, 2, 3, 4 that's how we count to five!")
        count -= 1
    elif ans[0].lower() != word[0]:
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    elif ans[0].lower() == word[0] and ans != word:
        count -= 1
        print("You have " + str(count) + " guesses left!")
    elif ans == word:
        print("Good Job! You are one with the Source.")
        break
    if count == 0:
        break
