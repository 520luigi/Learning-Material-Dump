# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    03_palindrome.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/05 16:12:10 by szheng            #+#    #+#              #
#    Updated: 2018/10/05 16:41:47 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

string = input("Enter a cool text which may be a palindrome:\n")

def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False

result =''.join(e for e in string if e.isalnum()).lower()
ans = isPalindrome(result)

if ans == 1:
    print("So ratchet! This shizzle mah nizzle IS a palindromeh!")
else:
    print("WTF, get out of here you nub!")
