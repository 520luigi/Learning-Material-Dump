# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_brainstorm.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/04 22:25:06 by szheng            #+#    #+#              #
#    Updated: 2018/10/05 15:49:12 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import time

categories = ["A boy's name", "Foods you eat for breakfast", "An animal",
        "Things that are cold", "Insects", "TV Shows", "Things that grow",
        "Fruits", "Things that are black", "School subjects", "Movie titles",
        "Muscial instruments", "Authors", "Bodies of water", "Games", "Holidays"]

print(random.choice(categories))

count = 10
answer = []

start_time = time.time()
while count > 0:
    print("You have", count, "chance to answer")
    n = input("Guess: ")
    answer.append(n)
    count -= 1
    if count == 0:
        print("")
print("---------------------------------")
for x in range(len(answer)):
    print ("|", '{num:02d}'.format(num = x + 1), ":", answer[x].center(24), "|")
elapsed_time = time.time() - start_time
print("---------------------------------")
print("It took about", round(elapsed_time, 2), "seconds to enter 10 items!")
