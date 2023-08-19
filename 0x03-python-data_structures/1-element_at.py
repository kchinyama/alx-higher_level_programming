#!/usr/bin/python3
def element_at(my_list, idx):
    k = my_list.index(idx)

    if k < 0:
        return None
    elif k > range(len(my_list[idx])):
        return None
    else:
        return k


