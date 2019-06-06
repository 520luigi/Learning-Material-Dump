# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_phonebook.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: szheng <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/19 16:36:36 by szheng            #+#    #+#              #
#    Updated: 2018/10/19 18:27:03 by szheng           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

names = {}

def read_file(filename):
    with open(filename) as f:
        for line in f:
            key, val = line.rstrip('\n').split(',')
            names[key] = val
'''
def similar_lastname():
    for i in names.keys():
        lastname = []
        for key, val in names.items():
            if i == key:
                lastname.append(names[key])
                print(lastname)

def similar_firstname():'''

new_dict = {}
for pair in names.items():
    if pair[1] not in new_dict.keys():
        new_dict[pair[1]] = []

    new_dict[pair[1]].append(pair[0])
print (new_dict)

def main():
    read_file("names.txt")
    print(names)

main()
