# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_rainbow.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/19 14:02:49 by szheng            #+#    #+#              #
#    Updated: 2018/10/19 14:18:16 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for foreground_color in range(30,38):
            s1 = ''
            for background_color in range(40,48):
                format = ';'.join([str(style), str(foreground_color), str(background_color)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, "42")
            print(s1)
        print('\n')

#print_format_table()

def print_colorful_text(string, style, foreground, background):
    format = ';'.join([str(style), str(foreground), str(background)])
    s = '\x1b[%sm %s \x1b[0m' % (format, string)
    print(s, end =" ")

def print_rainbow():
    a = 41
    for i in "RAINBOW":
        print_colorful_text(i, 0, 30, a)
        a += 1

print_rainbow()
