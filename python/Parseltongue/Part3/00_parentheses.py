# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_parentheses.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/17 15:28:32 by szheng            #+#    #+#              #
#    Updated: 2018/10/17 20:58:58 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def capitalize(s):
    ret = ""
    count = 0
    for char in s:
        if char.isalpha() and count % 2 == 0:
            ret += char.upper()
            count += 1
        elif char.isalpha() and count % 2 != 0:
            ret += char.lower()
            count += 1
        else:
            ret += char
    return ret

def checkVowels(s):
    ret = ""
    newstring = capitalize(s)
    for char in newstring:
        if (char == 'A' or char == 'E' or char == "I" or char == "O" or char == "U"):
            char = '*'
        ret += char
    return ret

def matched(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

# python has a neat way of detecting errors, by using try (a block of code for erros)
# then except (lets you handle the error). In this case, we check if arg1 exist, if 
# not, then print out the system error, and exit.
if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
    except IndexError:
        print ("Usage: python 00_parentheses.py <string>")
        sys.exit(1)

length = len(sys.argv)
if (length > 2):
    print ("Error, too many inputs!")
    sys.exit(1)
else:
    print (capitalize(sys.argv[1]))
    print (checkVowels(sys.argv[1]))
    print ("Balanced?", matched(sys.argv[1]))
