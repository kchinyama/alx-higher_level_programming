#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for k in range(list_length):
        try:
            result.append(my_list_1[k] / my_list_2[k])
            continue
        except TypeError:
            print("wrong type")

        except ZeroDivisionError:
            print("division bt 0")

        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
