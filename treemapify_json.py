#!/bin/env python
# -*- coding: utf-8 -*-

#
## Its time I use Recursion in real life, 😎
#

import copy

STRING_DELIMITER = '.'

def spawn_branch(delimited_string, apparent_root, item_price):
    delimited_string_tokens = delimited_string.split(STRING_DELIMITER)
    branch = delimited_string_tokens[0]
    if not delimited_string:
        if 'children' in apparent_root:
            # Leafs don't have children; populate price and count
            apparent_root['price'] = item_price
            apparent_root['count'] = 1
            del apparent_root['children']
        else:
            # Add to price, increment counter and return the apparent tree
            apparent_root['price'] = apparent_root['price'] + item_price
            apparent_root['count'] = apparent_root['count'] + 1
        return apparent_root

    children = copy.deepcopy(apparent_root['children'])
    if any(child['name'] == branch for child in children):
        child_index = get_index_of_key(children, branch)
        post_period_str = delimited_string[delimited_string.find('.')+1:]
        print "REMANING STRING:", post_period_str
        del apparent_root['children'][child_index]
        apparent_root['children'].append(spawn_branch(post_period_str, children[child_index], item_price))
    else:
        post_period_str = delimited_string[delimited_string.find('.')+1:]
        print "REMANING STRING:", post_period_str
        apparent_root['children'].append(spawn_branch(post_period_str, get_dict_skel(branch), item_price))
    return apparent_root

def get_index_of_key(dict_list, key_to_find):
    for i, val in enumerate(dict_list):
        if val['name'] == key_to_find:
            return i

def get_dict_skel(branch_name):
    daytaa = dict()
    daytaa['name'] = branch_name
    daytaa['children'] = list()
    return daytaa

def tree_builder():
    tree_root = spawn_branch('mayank.was.here.', get_dict_skel('tree_root'), 110)
    print tree_root

if __name__ == "__main__":
    tree_builder()
