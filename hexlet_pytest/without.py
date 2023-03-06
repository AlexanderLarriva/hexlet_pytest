def without(coll, *values):
    for i in values:
        coll = [x for x in coll if x is not i]
    return coll


print(without([1,2,2,3,4,5,3,6], 'f'))