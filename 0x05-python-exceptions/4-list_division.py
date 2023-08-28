#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    divList = []
    for k in range(0, list_length):
        try:
            divis = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
            divis = 0
        except ZeroDivisionError:
            print("division by 0")
            divis = 0
        except IndexError:
            print("out of range")
            divis = 0
        finally:
            divList.append(divis)
    return divList
