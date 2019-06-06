# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_daenerys.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/04 22:07:58 by szheng            #+#    #+#              #
#    Updated: 2018/10/04 22:22:54 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

n = input("Who goes there?\n")

if (n == "Daenerys of the House Targaryen" or n == "the First of Her Name"
        or n == "The Unburnt" or n == "Queen of the Andals" or
        n == "the Rhoynar and the First Men" or n == "Queen of Meereen" or
        n == "Khaleesi of the Great Grass Sea" or n == "Protector of the Realm"
        or n == "Lady Regnant of the Seven Kingdoms" or 
        n == "Breaker of Chains and Mother of Dragons" or 
        n == "DHTFHNUQARFMQMKGSPRLRSKBCMD"):
    print("Welcome, Daenerys")
elif n == "Dany":
    print("Dany who?")
else:
    print("Move along, now.")
