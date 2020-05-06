def remove_from_list(items: list, item):
    for i in items:
        if i != item:
            yield i

def merge_lists(l1: list, l2:list):
    c = 0
    for i in l1:
        if i:
            yield i
        else:
            yield l2[c]
            c += 1
